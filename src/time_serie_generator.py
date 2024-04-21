import numpy as np
from matplotlib.pyplot import plot, legend

class TimeSerieGenerator:

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


   
