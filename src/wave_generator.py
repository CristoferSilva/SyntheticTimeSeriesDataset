import matplotlib.pyplot as plt
import numpy as np 

class WaveGenerator:
    def __init__(self, start: int = 0, stop: int = 10, data_number: int = 160000) -> None:
        self.data_ponits = np.linspace(start=start, stop=stop, num=data_number)
        pass
    
    def generate_time_series(self, angular_frequency: float):
        return np.sin(angular_frequency*self.data_ponits) + 0.1*np.random.rand(len(self.data_ponits))
    
    def mixing_time_series(self, first_time_series, second_time_series):
        sine_wave = np.sin(2*np.pi*self.data_ponits)
        return first_time_series*sine_wave + (1-sine_wave)*second_time_series

    def plot_wave(self, serie, w = 1024, label_hz = 'Hz', color='b'):
        f, ax = plt.subplots(1, 2, figsize=(8, 5))
        ax[0].plot(serie[:2*w], c=color, label=label_hz)
        ax[0].legend()
        ax[1].plot(np.log(np.abs(np.fft.fft(serie[:w])))[:int(w/2)], c=color, label=label_hz)
        ax[1].legend()
        plt.legend()