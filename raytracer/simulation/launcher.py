import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from setup import chromatic_confocal
from raytrace import RayTrace
from _utils import plotter
import warnings

import time
from collections import namedtuple

warnings.filterwarnings("ignore")
plt.rcParams.update({"font.size": 22, "font.family": "Arial"})


def main():

    n_data = pd.read_csv(
        r"raytracer\data\n_intensity_500_800_new.csv",
        index_col=0,
    )
    n_data = n_data[::5]
    # n_data = n_data.iloc[[0, -1]]
    n_data["n_absorb"] = np.inf

    optical_data = chromatic_confocal
    PINHOLE_SIZE = 25 / 1000  # milimeters
    N_RAYS = 3
    LIGHT_SOURCE_RADIUS = 0 / 1000  # milimeters
    THETA = 6.0  # Degrees
    N_RAYS_HEIGHT = 1
    Z0 = -33.4  # Light source position same as
    # back focal length of the achormatic doublet

    fig, ax = plt.subplots()

    raytrace = RayTrace(
        optical_data=optical_data,
        n_data=n_data,
        light_source_radius=LIGHT_SOURCE_RADIUS,
        n_rays=N_RAYS,
        theta=THETA,
        z0=Z0,
        n_rays_height=N_RAYS_HEIGHT,
    )

    t0 = time.perf_counter()
    frays = raytrace.intersect_full_system()
    print("Elapsed time (s): ", time.perf_counter() - t0)

    # Plot setup
    fig, ax = plotter(
        optical_data=optical_data, final_rays=frays, fig=fig, ax=ax
    )
    plt.plot(
        [
            optical_data["Sensor"]["Front Face"]["z_0"],
            optical_data["Sensor"]["Front Face"]["z_0"],
        ],
        [-PINHOLE_SIZE / 2, PINHOLE_SIZE / 2],
        c="r",
    )
    ax.set(xlabel="z-position (mm)", ylabel="y-position (mm)")
    axins = ax.inset_axes([0.25, 0.1, 0.35, 0.35])
    plotter(optical_data=optical_data, final_rays=frays, fig=fig, ax=axins)
    axins.plot(
        [
            optical_data["Sensor"]["Front Face"]["z_0"],
            optical_data["Sensor"]["Front Face"]["z_0"],
        ],
        [-PINHOLE_SIZE / 2, PINHOLE_SIZE / 2],
        c="r",
        lw=3,
        label="PINHOLE",
    )
    x1, x2, y1, y2 = (
        optical_data["Sensor"]["Front Face"]["z_0"] - 0.1,
        optical_data["Sensor"]["Front Face"]["z_0"] + 0.1,
        -0.1,
        0.1,
    )
    axins.legend()
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)
    plt.gca().indicate_inset_zoom(axins, edgecolor="black")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    data = namedtuple("data", "spectra, description")
    main()
