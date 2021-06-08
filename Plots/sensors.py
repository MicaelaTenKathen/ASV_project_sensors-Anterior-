import numpy as np
import matplotlib.pyplot as plt


def comparison(data, i):
    width = 0.2
    x = np.array([1, 2, 3, 4, 5, 6, 7])

    if i == 0:
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        fig.suptitle("Temperature")
        ax.bar(x, data["MEAN"][0], width, color='b', yerr=data["STD"][0], label='Temperature', alpha=0.6)
        ax.set_xlabel("Number of sample")
        ax.set_ylabel("Temp [ºC]")

    elif i == 1:
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        fig.suptitle("pH")
        ax.bar(x, data["MEAN"][1], width, color='c', yerr=data["STD"][1], label='Temperature', alpha=0.9)
        ax.set_xlabel("Number of sample")
        ax.set_ylabel("pH [mV]")

    elif i == 2:
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        fig.suptitle("DO")
        ax.bar(x, data["MEAN"][2], width, color='y', yerr=data["STD"][2], label='Temperature', alpha=0.7)
        ax.set_xlabel("Number of sample")
        ax.set_ylabel("DO [mg/L]")

    elif i == 3:
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        fig.suptitle("Conductivity")
        ax.bar(x, data["MEAN"][3], width, color='r', yerr=data["STD"][3], label='Temperature', alpha=0.6)
        ax.set_xlabel("Number of sample")
        ax.set_ylabel("Cond [us/cm]")

    elif i == 4:
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        fig.suptitle("ORP")
        ax.bar(x, data["MEAN"][4], width, color='g', yerr=data["STD"][4], label='Temperature', alpha=0.7)
        ax.set_xlabel("Number of sample")
        ax.set_ylabel("ORP [mV]")