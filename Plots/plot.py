import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn")


def plots(data, time, num):

    plt.figure(figsize=(8, 14))
    plt.suptitle("Sample Point %i" % num)

    plt.subplot(511)
    plt.plot(time, data["TEMP"])
    plt.xlabel("time [s]")
    plt.ylabel("Temp ºC")

    plt.subplot(512)
    plt.plot(time, data["PH"])
    plt.xlabel("time [s]")
    plt.ylabel("pH [mV]")

    plt.subplot(513)
    plt.plot(time, data["DO"])
    plt.xlabel("time [s]")
    plt.ylabel("DO [mg/L]")

    plt.subplot(514)
    plt.plot(time, data["COND"])
    plt.xlabel("time [s]")
    plt.ylabel("Cond [us/cm]")

    plt.subplot(515)
    plt.plot(time, data["ORP"])
    plt.xlabel("time [s]")
    plt.ylabel("ORP [mV]")
    plt.tight_layout()

    #%% no consideramos las primeras diez muestras
    # ya que se están estabilizando las medidas


def histo(data, num):
    stable_data = data

    plt.figure(figsize=(8, 14))
    plt.suptitle("Sample point %i" % num)

    plt.subplot(511)
    plt.hist(stable_data["TEMP"][10:], bins=10)
    plt.xlabel("Temp ºC")

    plt.subplot(512)
    plt.hist(stable_data["PH"][10:], bins=10)
    plt.xlabel("pH [mV]")

    plt.subplot(513)
    plt.hist(stable_data["DO"][10:], bins=10)
    plt.xlabel("DO [mg/L]")

    plt.subplot(514)
    plt.hist(stable_data["COND"][10:], bins=10)
    plt.xlabel("Cond [us/cm]")

    plt.subplot(515)
    plt.hist(stable_data["ORP"][10:], bins=10)
    plt.xlabel("ORP [mV]")

    plt.tight_layout()
