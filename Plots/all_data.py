import pandas as pd
from plot import *
from Data_scripts.mean_std import *

total_data = pd.read_csv("../Data/data_01_06_2021.csv", delimiter=",")


plots(total_data, np.arange(0, np.copy(total_data["TEMP"]).shape[0], 1) * 13, 1)
histo(total_data, 1)