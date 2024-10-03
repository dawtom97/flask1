def convert_temp(f):
    def wrapper(initial_temp):
        if initial_temp < 0:
            raise ValueError("Temp. w kelvinach nie może być mniejsza od 0")
        celsius_temp =round(initial_temp - 273.15) 
        return f(celsius_temp)
    return wrapper