import pandas as pd
from Data_scripts.data_collected import data_collec
from Data_scripts.limits import *
from Data_scripts.mean_std import *
from Plots.sensors import comparison
from Plots.plot import *

total_data = pd.read_csv("Data/data_01_06_2021.csv", delimiter=",")

total_data["DATE"] = pd.to_datetime(total_data["DATE"])
total_sample = np.copy(total_data["SAMPLE_NUM"])

last_data = 0
init = 0
num_points = 7

data1 = np.copy(total_data["DATE"])
n_data = np.arange(1, num_points + 1, 1)
sensors = ["TEMP", "PH", "DO", "COND", "ORP"] #, "BAT"]
name_sensors = ['temp%s', 'ph%s', 'do%s', 'cond%s', 'orp%s']  #, 'bat%s']
mean_sensors = ['mean_temp%s', 'mean_ph%s', 'mean_do%s', 'mean_cond%s', 'mean_orp%s'] #, 'mean_bat%s']
std_sensors = ['std_temp%s', 'std_ph%s', 'std_do%s', 'std_cond%s', 'std_orp%s'] #, 'std_bat%s']


for k in range(len(sensors)):
     init = 0
     for j in range(len(n_data)):
          globals()[name_sensors[k] % n_data[j]], init = data_collec(total_data, init, sensors, k)

for j in range(len(n_data)):
     globals()['sample_points%s' % n_data[j]] = {"TEMP": globals()[name_sensors[0] % n_data[j]],
                                                 "PH": globals()[name_sensors[1] % n_data[j]],
                                                 "DO": globals()[name_sensors[2] % n_data[j]],
                                                 "COND": globals()[name_sensors[3] % n_data[j]],
                                                 "ORP": globals()[name_sensors[4] % n_data[j]]}
                                                 #"BAT": globals()[name_sensors[5] % n_data[j]]

     globals()['time%s' % n_data[j]] = np.arange(0, np.array(globals()[name_sensors[0] % n_data[j]]).shape[0], 1) * 13

min_sensors = []
max_sensors = []
shape_sensors = []

for k in range(len(sensors)):
    min_array = []
    max_array = []
    shape_array = []

    for h in range(len(n_data)):
        min_array, max_array, shape_array = min_max(globals()['sample_points%s' % n_data[h]], sensors, k, min_array,
                                                    max_array, shape_array)

    min_sensors, max_sensors, shape_sensors = limits_plots(min_array, max_array, shape_array, min_sensors, max_sensors,
                                                           shape_sensors)


for j in range(len(n_data)):
    plots(globals()['sample_points%s' % n_data[j]], globals()['time%s' % n_data[j]], n_data[j], min_sensors,
          max_sensors)
    histo(globals()['sample_points%s' % n_data[j]], n_data[j], min_sensors, max_sensors, shape_sensors)

for t in range(len(sensors)):
    me = list()
    st = list()
    h = 0
    print(n_data[h])
    for h in range(len(n_data)):
        m,  s = mean(np.array(globals()['sample_points%s' % n_data[h]][sensors[t]]), n_data[h])
        me.append(m)
        st.append(s)
    globals()['sensor%s' % sensors[t]] = {"MEAN": me,
                                          "STD": st}
    comparison(globals()['sensor%s' % sensors[t]], t, num_points + 1)