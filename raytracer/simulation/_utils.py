import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aspheric import AsphericLens
import matplotlib


def get_detected_spectrum(
    final_rays: np.ndarray, n_data: pd.DataFrame, pinhole_size: float
) -> pd.DataFrame:
    n_data_updated = n_data
    # Go trough all rays
    for i, heights in enumerate(final_rays):
        cnt = 0
        for j, rays in enumerate(heights):
            # TODO: Think a better way to remove absorbed rays
            val = np.min([len(ray.path) for ray in rays])
            for ray in rays:
                if len(ray.path) != val:
                    continue
                if np.abs(ray.path[-1][0]) < pinhole_size:
                    cnt += 1
            p = cnt / len(rays)
            wavelenght = n_data_updated.index[i]
            n_data_updated.loc[wavelenght, "intensity"] = (
                n_data_updated.loc[wavelenght, "intensity"] * p
            )

    return n_data_updated


def plotter(
    optical_data: dict,
    final_rays: np.ndarray,
    fig: plt.Figure = None,
    ax: plt.Axes = None,
):
    if fig and ax:
        fig, ax = fig, ax
    else:
        fig, ax = plt.subplots()
    # Plot surfaces
    for optical_data_key in optical_data.keys():
        # Get element
        element = optical_data.get(optical_data_key)
        # Get element's material
        for surface in element.items():
            item = optical_data.get(optical_data_key)[surface[0]]
            # If item is dictionary, it is Front or Back surface.
            if isinstance(item, dict):
                surface = AsphericLens(**item)
                ax.plot(
                    surface.surface_zr(
                        surface.aperture_radius,
                        surface.curvature,
                        surface.z0_lens,
                        surface.konic,
                    ),
                    surface.aperture_radius,
                    color="b",
                )

    # Color
    rb = matplotlib.colormaps.get_cmap("rainbow")
    rb = rb(np.linspace(0, 1, len(final_rays)))
    # Plot rays
    for k, heights in enumerate(final_rays):
        for j, rays in enumerate(heights):
            for ray in rays:
                for i in range(len(ray.path) - 1):
                    ax.plot(
                        [ray.path[i][1], ray.path[i + 1][1]],
                        [ray.path[i][0], ray.path[i + 1][0]],
                        c=rb[k],
                        linewidth=0.1,
                    )

    return fig, ax


def move_sample(dicttoupdate: dict, displacement: float) -> dict:
    for key, values in dicttoupdate.items():
        if dicttoupdate[key].get("Calibration"):
            continue

        front_face = values.get("Front Face")
        back_face = values.get("Back Face")

        z_0f = front_face.get("z_0")
        z_0b = back_face.get("z_0")

        front_face["z_0"] = z_0f + displacement
        back_face["z_0"] = z_0b + displacement

    return dicttoupdate
