import matplotlib.pyplot as plt
import numpy as np 

class WaveGenerator:
    def __init__(self) -> None:
        pass
    
    def generate_time_series(self, frequency: float, start: int = 0, stop: int = 10, data_number: int = 160000):
        data_ponits = np.linspace(start=start, stop=stop, num=data_number)
        
        return np.sin(frequency*data_ponits) + 0.1*np.random.rand(len(data_ponits))
    

    def plot_wave(self, serie, w = 1024, label_hz = 'Hz', color='b'):
        f, ax = plt.subplots(1, 2, figsize=(8, 5))
        ax[0].plot(serie[:2*w], c=color, label=label_hz)
        ax[0].legend()
        ax[1].plot(np.log(np.abs(np.fft.fft(serie[:w])))[:int(w/2)], c=color, label=label_hz)
        ax[1].legend()
        plt.legend()