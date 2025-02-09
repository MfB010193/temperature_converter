import argparse
from converter import Converter
from logger import setup_logging, log_conversion

setup_logging()

parser = argparse.ArgumentParser(description="Temperature Converter")

parser.add_argument("temperature_value", type=float, help="Enter the temperature value")

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

print("Please select your input temperature scale:")
for index, unit in enumerate(temperature_units, start=1):
    print(f"{unit} --> {index}")

parser.add_argument("input_temperature", type=int, choices=[1, 2, 3], help="Select the input temperature scale (1: Celsius, 2: Fahrenheit, 3: Kelvin)")

print("\nPlease select your output temperature scale:")
for index, unit in enumerate(temperature_units, start=1):
    print(f"{unit} --> {index}")

parser.add_argument("output_temperature", type=int, choices=[1, 2, 3], help="Select the output temperature scale (1: Celsius, 2: Fahrenheit, 3: Kelvin)")

args = parser.parse_args()

temperature_value = args.temperature_value
input_scale = args.input_temperature - 1
output_scale = args.output_temperature - 1

new_temp = 0
converter = Converter()
if input_scale == 0:
    if output_scale == 1:
        new_temp =converter.celsius_fahrenheit(temperature_value)
    elif output_scale == 2:
        new_temp = converter.celsius_kelvin(temperature_value)
    else:
        new_temp = temperature_value
elif input_scale == 1:
    if output_scale == 0:
        new_temp = converter.fahrenheit_celsius(temperature_value)
    elif output_scale == 2:
        new_temp = converter.fahrenheit_kelvin(temperature_value)
    else:
        new_temp = temperature_value
elif input_scale == 2:
    if output_scale == 0:
        new_temp = converter.kelvin_celsius(temperature_value)
    elif output_scale == 1:
        new_temp = converter.kelvin_fahrenheit(temperature_value)
    else:
        new_temp = temperature_value
else:
    print("Please select the correct value")


log_conversion(temperature_value, temperature_units[input_scale], new_temp, temperature_units[output_scale])
print(f'accepted temperature value {temperature_value}, in scale {temperature_units[input_scale]}, needed to convert {temperature_units[output_scale]}, new scale {new_temp}')

