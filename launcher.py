import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from chromatic_confocal.simulation.setup import real_setup, test
from chromatic_confocal.simulation.raytrace import RayTrace
from chromatic_confocal.simulation._utils import (
    move_sample,
    plotter,
    get_detected_spectrum,
)

import copy
import time
import warnings
from collections import namedtuple
from chromatic_confocal.utils import save_pickle, normalize

warnings.filterwarnings("ignore")

plt.rcParams.update({"font.size": 22,
                     "font.family": "Arial"})


def main():

    n_data = pd.read_csv(
        r"chromatic_confocal\simulation\data\n_intensity_500_800_new.csv",
        index_col=0,
    )
    n_data = n_data[::5]
    # n_data = n_data.iloc[[0, -1]]
    n_data["n_absorb"] = np.inf

    optical_data = real_setup
    PINHOLE_SIZE = 25 / 1000  # milimeters
    N_RAYS = 3
    DISPLACEMENT = 20 / 1000  # milimeters
    N_DISPLACEMENTS = 400
    LIGHT_SOURCE_RADIUS = 0 / 1000  # milimeters
    THETA = 6.0
    N_RAYS_HEIGHT = 1
    Z0 = - 33.4

    displacements = np.arange(0, DISPLACEMENT * N_DISPLACEMENTS, DISPLACEMENT)
    spectra = np.zeros((2, len(displacements), len(n_data)))
    fig, ax = plt.subplots()
    for i, dist in enumerate(displacements):

        optical_data = move_sample(copy.deepcopy(optical_data), dist)

        raytrace = RayTrace(

            optical_data=optical_data,
            n_data=n_data,
            light_source_radius=LIGHT_SOURCE_RADIUS,
            n_rays=N_RAYS,
            theta=THETA,
            z0=Z0,
            n_rays_height=N_RAYS_HEIGHT)

        t0 = time.perf_counter()
        frays = raytrace.intersect_full_system()
        print("Elapsed time (s): ", time.perf_counter() - t0)
        n_data_updated = get_detected_spectrum(
            frays, copy.deepcopy(n_data), PINHOLE_SIZE
        )

        spectra[0, i, :] = n_data_updated.intensity
        spectra[1, i, :] = n_data_updated.index

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

    a = data(
        spectra=spectra,
        description=f"Sensor position:"
        f"{optical_data['Sensor']['Front Face']['z_0']}|"
        f"Pinhole size: {PINHOLE_SIZE}|Displacement:{DISPLACEMENT}|"
        f"Number rays:{N_RAYS}|n_data length:{len(n_data)}|"
        f"Light source radius:{LIGHT_SOURCE_RADIUS}|"
        f"Spatial filter radius:{optical_data['Spatial filter']
                                 ['Front Face']['aperture_radius']}",
    )

    save_pickle(a, r"chromatic_confocal\simulation\data\spectra_sensoratfocus_20um_10rays.pkl")
    plt.plot(n_data.index, normalize(n_data.intensity))
    plt.plot(spectra[1, 0, :], normalize(spectra[0, 0, :]))
    plt.show()


if __name__ == "__main__":
    data = namedtuple("data", "spectra, description")
    main()
