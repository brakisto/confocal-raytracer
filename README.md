# Chromatic Confocal Sensor Ray Tracer

Specialized ray tracing engine designed for simulating and optimizing chromatic confocal sensors. This repository provides a powerful toolset for researchers and engineers working on precise optical measurement systems, enabling the accurate modeling of light interactions within chromatic confocal setups.

## Defining the setup

The optical setup is defined inside the setup.py file. If, for example, an achromatic doublet is defined each face of both lenses should be defined as follows:


``` doublet = {
    "AC500-150-A-ML_1": {
        "Front Face": dict(
            curvature=96.85, konic=0, z_0=0, aperture_radius=50 / 2
        ),
        "Back Face": dict(
            curvature=-73.74,
            konic=0,
            z_0=9.5,
            aperture_radius=50 / 2,
        ),
        "Material": "BAK4",
        "Calibration": False,
    },
    "AC500-150-A-ML_2": {
        "Front Face": dict(
            curvature=-73.74, konic=0, z_0=9.5, aperture_radius=50 / 2
        ),
        "Back Face": dict(
            curvature=-241.63,
            konic=0,
            z_0=13.5,
            aperture_radius=50 / 2,
        ),
        "Material": "SF10",
        "Calibration": False,
    },
    "AC500-150-A-ML_1_R": {
        "Front Face": dict(
            curvature=241.63,
            konic=0,
            z_0=0,
            aperture_radius=50 / 2,
        ),
        "Back Face": dict(
            curvature=73.74, konic=0, z_0=4, aperture_radius=50 / 2
        ),
        "Material": "BAK4",
        "Calibration": False,
    },
    "AC500-150-A-ML_2_R": {
        "Front Face": dict(
            curvature=73.74,
            konic=0,
            z_0=4,
            aperture_radius=50 / 2,
        ),
        "Back Face": dict(
            curvature=-96.85, konic=0, z_0=13.5, aperture_radius=50 / 2
        ),
        "Material": "SF10",
        "Calibration": False,
    },
    "Sensor": {
        "Front Face": dict(
            curvature=float("inf"),
            konic=0,
            z_0=170,
            aperture_radius=100,
        ),
        "Back Face": dict(
            curvature=float("inf"),
            konic=0,
            z_0=170,
            aperture_radius=100,
        ),
        "Material": "SF2",
        "Calibration": False,
    },
} ```

## Lens materials

The materials available with their refractive indexes should be specified in a CSV file in the *data* folder as follows:

| wl_nm|intensity|n_BK7|n_SF2|n_SF5|n_BAF10|n_SF10|n_BAK4|n_SF57                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 500.5|0.0851431638|1.5213856439764|1.6587264318676913|1.6847781738090497|1.67825|1.74315|1.57468|1.86746                                                |
| 500.7|0.08645302802|1.5213723632237195|1.6586929033319964|1.6847437966326086|1.6782202524647911|1.7430968741556505|1.574659846238762|1.8673847333525386 |
| 500.8|0.08502408117|1.5213657288620468|1.658676166909398|1.684726608044388|1.6782055071330022|1.7430704823647605|1.5746498284981434|1.8673473595993073  |