chromatic_confocal = {
    "A1": {
        "Front Face": dict(
            curvature=57.7,
            konic=0,
            z_0=0,
            aperture_radius=25.4 / 2,
        ),
        "Back Face": dict(
            curvature=20.1, konic=0, z_0=2.5, aperture_radius=25.4 / 2
        ),
        "Material": "SF5",
        "Calibration": True,
    },
    "A2": {
        "Front Face": dict(
            curvature=20.1,
            konic=0,
            z_0=2.5,
            aperture_radius=25.4 / 2,
        ),
        "Back Face": dict(
            curvature=-23.7, konic=0, z_0=12.5, aperture_radius=25.4 / 2
        ),
        "Material": "BK7",
        "Calibration": True,
    },
    "Aspheric": {
        "Front Face": dict(
            curvature=float("inf"),
            konic=0,
            A=0,
            B=0,
            aperture_radius=160,
            z_0=50,
        ),
        "Back Face": dict(
            curvature=-329.767,
            konic=-0.604045,
            z_0=120,
            A=0,
            B=0,
            aperture_radius=160,
        ),
        "Material": "BK7",
        "Calibration": True,
    },
    "Aspheric Sequential": {
        "Front Face": dict(
            curvature=329.767,
            konic=-0.604045,
            z_0=1140 + 250,
            aperture_radius=160,
        ),
        "Back Face": dict(
            curvature=float("inf"),
            konic=0,
            aperture_radius=160,
            z_0=1200 + 250,
        ),
        "Material": "BK7",
        "Calibration": False,
    },
    "AC254-030-A-ML_1": {
        "Front Face": dict(
            curvature=20.9, konic=0, z_0=1255 + 250, aperture_radius=25.4 / 2
        ),
        "Back Face": dict(
            curvature=-16.7,
            konic=0,
            z_0=1267 + 250,
            aperture_radius=25.4 / 2,
        ),
        "Material": "BK7",
        "Calibration": False,
    },
    "AC254-030-A-ML_2": {
        "Front Face": dict(
            curvature=-16.7, konic=0, z_0=1267 + 250, aperture_radius=25.4 / 2
        ),
        "Back Face": dict(
            curvature=-79.8,
            konic=0,
            z_0=1269 + 250,
            aperture_radius=25.4 / 2,
        ),
        "Material": "SF2",
        "Calibration": False,
    },
    "AC500-150-A-ML_1_R": {
        "Front Face": dict(
            curvature=241.63,
            konic=0,
            z_0=1692,
            aperture_radius=50 / 2,
        ),
        "Back Face": dict(
            curvature=73.74, konic=0, z_0=1692 + 4, aperture_radius=50 / 2
        ),
        "Material": "SF10",
        "Calibration": False,
    },
    "AC500-150-A-ML_2_R": {
        "Front Face": dict(
            curvature=73.74,
            konic=0,
            z_0=1692 + 4,
            aperture_radius=50 / 2,
        ),
        "Back Face": dict(
            curvature=-96.85, konic=0, z_0=1692 + 13.5, aperture_radius=50 / 2
        ),
        "Material": "BAK4",
        "Calibration": False,
    },
    "Spatial filter": {
        "Front Face": dict(
            curvature=float("inf"),
            konic=0,
            z_0=1500 + 250,
            aperture_radius=10,
        ),
        "Back Face": dict(
            curvature=float("inf"),
            konic=0,
            z_0=1500 + 250,
            aperture_radius=10,
        ),
        "Material": "absorb",
        "Calibration": False,
    },
    "AC500-75-A-ML_2": {
        "Front Face": dict(
            curvature=51.88,
            konic=0,
            z_0=1810,
            aperture_radius=50 / 2,
        ),
        "Back Face": dict(
            curvature=-32.79, konic=0, z_0=1830, aperture_radius=50 / 2
        ),
        "Material": "BAF10",
        "Calibration": False,
    },
    "AC500-75-A-ML_1": {
        "Front Face": dict(
            curvature=-32.79, konic=0, z_0=1830, aperture_radius=50 / 2
        ),
        "Back Face": dict(
            curvature=-309.45, konic=0, z_0=1834.5, aperture_radius=50 / 2
        ),
        "Material": "SF10",
        "Calibration": False,
    },
    "Sensor": {
        "Front Face": dict(
            curvature=float("inf"),
            konic=0,
            z_0=1895.4,
            aperture_radius=200,
        ),
        "Back Face": dict(
            curvature=float("inf"),
            konic=0,
            z_0=1895.4,
            aperture_radius=200,
        ),
        "Material": "absorb",
        "Calibration": False,
    },
}


doublet = {
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
}
