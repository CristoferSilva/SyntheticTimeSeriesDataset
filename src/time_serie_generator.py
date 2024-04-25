import os
from random import randint
import numpy as np
from joblib import dump
from matplotlib.pyplot import plot, legend

class TimeSerieGenerator:

    def __init__(self) -> None:
        pass

    @property
    def last_generated_series(self):
        return self.multiple_time_series.copy()
    
    @property
    def last_generated_noisy_series(self):
        return self.time_series_with_noise.copy()

    def __get_shift(self,phase_shift, data_size):
        #using fic func to create shift
        shift = np.zeros(data_size)
        shift[phase_shift] = 1.0
        return np.fft.fft(shift)
    
    def generate_time_serie(self, size, shift_number = 4):
        values = np.linspace(0, 2*np.pi,size)
        sin = np.sin(values)
        piBy4 = size//shift_number
        shift = self.__get_shift(phase_shift=piBy4, data_size=len(values))
        shifted_sin_frequency_domain = np.fft.fft(sin)*shift
        time_serie = np.fft.ifft(shifted_sin_frequency_domain)
        return time_serie
    
    def generate_multiple_time_series(self,time_series_size, shift_numbers):
        multiple_time_series = []
        for shift_number in shift_numbers:
            multiple_time_series.append(self.generate_time_serie(size=time_series_size, shift_number=shift_number, ))

        return multiple_time_series
    
    def plot_time_series(self, time_series):
        count = 0
        y_axes = np.linspace(0, 2*np.pi, len(time_series[0])) 

        for time_serie in time_series:
            plot(y_axes,time_serie.real,label='Time Serie [{}]'.format(count))
            legend()
            count += 1

    def generate_multiple_time_series_with_noise(self, multiple_time_series):
        time_series_with_noise = []
        noise = np.random.normal(0,0.1, len(multiple_time_series[0]))
        for time_serie in multiple_time_series:
            time_series_with_noise.append(time_serie + noise)

        return time_series_with_noise

    def save(self, multiple_time_series_array: np.array, file_name: str = 'sts_dataset.csv'):
        filepath_extension_csv = os.path.join(os.getcwd(), file_name)
        np.savetxt(filepath_extension_csv, multiple_time_series_array, delimiter=',')

        #TO-DO: Apply import h5py
        # filepath_extension_h5 = os.path.join(os.getcwd(), 'sts_dataset.h5')
        # with h5py.File(filepath_extension_h5, 'w') as hf:
        #     hf.create_dataset('dataset', data=multiple_time_series_array)

    def put_anomaly_points(self, amount, time_serie):
        ts = time_serie.copy()
        anomaly_position = []

        for _ in range(amount):
            index = randint(200,len(time_serie)-1)
            anomaly_position.append(index)
            coefficient = randint(4,8)
            ts[index] *= coefficient

        return ts,anomaly_position
        
