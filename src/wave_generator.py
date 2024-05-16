import numpy as np

class WaveGenerator:
    def __init__(self) -> None:
        pass
    
    def generate_time_series(self, quantity_time_series: int = 3, start: int = 0, stop: int = 10, data_number: int = 160000):
        time_series = []
        
        for i in range(quantity_time_series):
            time_series.append(np.linspace(start=start, stop=stop, num=data_number))
        return time_series
    