import pandas as pd
import os

this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "data", "n_intensity_500_800_new.csv")

n_data = pd.read_csv(
    DATA_PATH,
    index_col=0,
)
