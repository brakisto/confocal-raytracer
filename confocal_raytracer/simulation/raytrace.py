from scipy.optimize import fsolve
import numpy as np
import pandas as pd
from confocal_raytracer.simulation.aspheric import AsphericLens
from confocal_raytracer.simulation.ray import Ray
import cProfile as profile


def surface_zr(y, R, z0, k):
    z = (1 / R) * y**2 / (1 + np.sqrt(1 - (1 + k) * ((1 / R) * y) ** 2)) + z0
    return z


def spherical_lens_prime(y, R, k, z0=0):
    return (1 / R) ** 3 * y**3 * (k + 1) / (
        np.sqrt(-((1 / R) ** 2) * y**2 * (k + 1) + 1)
        * (np.sqrt(-((1 / R) ** 2) * y**2 * (k + 1) + 1) + 1) ** 2
    ) + 2 * (1 / R) * y / (np.sqrt(-((1 / R) ** 2) * y**2 * (k + 1) + 1) + 1)


def merit_function_v2(x0, R, k, m, z0_ray, y0_ray, z0_lens):
    y, z = x0
    return [
        (z - z0_ray) * m - (y - y0_ray),
        z - y**2 / (R * (1 + np.sqrt(1 - (1 - k) * (y / R) ** 2))) - z0_lens,
    ]


def solver_v2(fun, R, k, m, z0_ray, y0_ray, z0_lens):
    sol_y, sol_z = fsolve(
        fun,
        x0=[y0_ray, z0_ray],
        args=(R, k, m, z0_ray, y0_ray, z0_lens),
        maxfev=100,
    )
    return sol_z, sol_y


def snell(n1, n2, theta1):
    return np.arcsin(n1 * np.sin(theta1) / n2)


class RayTrace:

    def __init__(
        self,
        optical_data: dict,
        n_data: pd.DataFrame,
        light_source_radius: float,
        n_rays: int,
        theta: int,
        z0: float,
        n_rays_height: int,
    ):

        self.optical_data = optical_data
        self.n_data = n_data
        self.light_source = (
            np.linspace(
                -light_source_radius, light_source_radius, n_rays_height
            )
            if light_source_radius != 0
            else np.zeros(1)
        )
        self.thetas = (
            np.deg2rad(np.linspace(-theta, theta, n_rays))
            if theta != 0
            else np.zeros(1)
        )
        self.z0 = z0
        self.elements = optical_data.keys()
        self.prev_n = 1
        self.surfaces = [
            (AsphericLens(**surface), item["Material"])
            for item in optical_data.values()
            for surface in item.values()
            if isinstance(surface, dict)
        ]

    def update_ray(self, ray, surface, n_inc, n_ref):
        # Get intersection point for surface and ray
        R, k, z0_lens, r, y0_ray, z0_ray = (
            surface.curvature,
            surface.konic,
            surface.z0_lens,
            ray.ray,
            ray.y0,
            ray.z0,
        )

        sol_z, sol_y = solver_v2(
            merit_function_v2,
            R=R,
            k=k,
            m=r[1] / r[0],
            y0_ray=y0_ray,
            z0_ray=z0_ray,
            z0_lens=z0_lens,
        )

        if np.abs(sol_y) > np.max(surface.aperture_radius):
            return ray.y0, ray.z0, ray.theta, ray

        # TODO: Check if normal and tangent are correct.
        # Tangent curve slope at sol_y.
        mtan = spherical_lens_prime(y=sol_y, R=R, k=k, z0=z0_lens)
        # Norm curve slope at sol_y
        # mnorm = -1 / mtan
        m1 = -mtan
        m2 = r[1] / r[0]
        # Refract the ray
        theta_r = np.arctan2((m2 - m1), (1 + m1 * m2))
        theta = snell(n_inc, n_ref, theta_r)

        # Convert from relative angle to absolute angle relative to horizontal
        # for the next surface refraction
        theta = theta - np.arctan2(-m1 - 0, (1 + (-m1) * 0))

        # Update ray
        ray.update_ray(sol_y, sol_z, theta)
        return sol_y, sol_z, theta, ray

    def snell(self, prev_n, n, prev_theta):
        return np.arcsin(prev_n * np.sin(prev_theta) / n)

    def getn(self, wavelength, material):
        return self.n_data.loc[wavelength, :][f"n_{material}"]

    def profile(self):
        profile.runctx("self.intersect_full_system()", globals(), locals())

    def intersect_full_system(self):
        # Initialize rays
        # TODO: Generalize if a non collimated light is needed
        frays = np.zeros(
            (len(self.n_data), len(self.light_source), len(self.thetas)),
            dtype=object,
        )

        print(
            f"Total number of rays is {len(self.n_data) * len(self.light_source) * len(self.thetas)}"
        )

        # Go trough all wavelengths
        for i, wl in enumerate(self.n_data.index):
            for k, y in enumerate(self.light_source):
                rays = [Ray(y0=y, z0=self.z0, theta=th) for th in self.thetas]
                # Go through  all rays
                for ray in rays:
                    # Go through all optical elements
                    for j, (surface, material) in enumerate(self.surfaces):

                        self.n = self.getn(wl, material) if j % 2 == 0 else 1

                        self.update_ray(
                            surface=surface,
                            n_inc=self.prev_n,
                            n_ref=self.n,
                            ray=ray,
                        )
                        self.prev_n = self.n

                frays[i, k, :] = rays
        return frays
