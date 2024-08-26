import pandas as pd

n_data = pd.read_csv(
    r"confocal_raytracer\data\n_intensity_500_800_new.csv",
    index_col=0,
)
