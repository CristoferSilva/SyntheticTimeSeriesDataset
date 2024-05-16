import matplotlib.pyplot as plt
import numpy as np 

class WaveGenerator:
    def __init__(self) -> None:
        pass
    
    def generate_time_series(self, quantity_time_series: int = 3, start: int = 0, stop: int = 10, data_number: int = 160000):
        time_series = []
        
        for i in range(quantity_time_series):
            time_series.append(np.linspace(start=start, stop=stop, num=data_number))
        return time_series
    

    def plot_wave(self, serie, w = 1024, label_hz = 'Hz', color='b'):
        f, ax = plt.subplots(1, 2, figsize=(8, 5))
        ax[0].plot(serie[:2*w], c=color, label=label_hz)
        ax[0].legend()
        ax[1].plot(np.log(np.abs(np.fft.fft(serie[:w])))[:int(w/2)], c=color, label=label_hz)
        ax[1].legend()
        plt.legend()