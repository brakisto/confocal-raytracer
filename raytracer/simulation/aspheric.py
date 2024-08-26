import numpy as np


class AsphericLens(object):

    def __init__(
        self, aperture_radius, curvature, konic, z_0, n=1.5, *args, **kwargs
    ):
        self.aperture_radius = np.arange(
            -aperture_radius, aperture_radius, 0.01
        )
        self.curvature = curvature
        self.konic = konic
        self.refractive_index = n
        self.z0_lens = z_0

    def surface_zr(self, y, R, z0, k):
        z = (1 / R) * y**2 / (
            1 + np.sqrt(1 - (1 + k) * ((1 / R) * y) ** 2)
        ) + z0
        return z

    def spherical_lens_prime(self, y, R, z0=0, k=0):
        return (1 / R) ** 3 * y**3 * (k + 1) / (
            np.sqrt(-((1 / R) ** 2) * y**2 * (k + 1) + 1)
            * (np.sqrt(-((1 / R) ** 2) * y**2 * (k + 1) + 1) + 1) ** 2
        ) + 2 * (1 / R) * y / (
            np.sqrt(-((1 / R) ** 2) * y**2 * (k + 1) + 1) + 1
        )
