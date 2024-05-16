import matplotlib.pyplot as plt
import numpy as np 

class WaveGenerator:
    def __init__(self) -> None:
        pass

    def plot_wave(self, serie, w = 1024, label_hz = 'Hz', color='b'):
        f, ax = plt.subplots(1, 2, figsize=(8, 5))
        ax[0].plot(serie[:2*w], c=color, label=label_hz)
        ax[0].legend()
        ax[1].plot(np.log(np.abs(np.fft.fft(serie[:w])))[:int(w/2)], c=color, label=label_hz)
        ax[1].legend()
        plt.legend()