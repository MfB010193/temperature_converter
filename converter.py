class Converter:
    def kelvin_fahrenheit(self, temp: float) -> float:
        return ((9/5) * (temp - 273.15)) + 32


    def celsius_fahrenheit(self, temp: float) -> float:
        new_temp = (temp * 9/5) + 32
        return new_temp


    def fahrenheit_celsius(self, temp: float) -> float:
        new_temp = ( 5 / 9) * (temp - 32)
        return new_temp

    def kelvin_celsius(self, temp: float) -> float:
        new_temp = temp - 273.15
        return new_temp

    def celsius_kelvin(self, temp: float) -> float:
        new_temp = temp + 273.15
        return new_temp

    def fahrenheit_kelvin(self, temp: float) -> float:
        new_temp = ((5 / 9) * (temp - 32)) + 273.15
        return new_temp