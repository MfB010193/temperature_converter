# Temperature Converter CLI

A simple command-line interface (CLI) tool for converting temperatures between Celsius, Fahrenheit, and Kelvin. This project also includes logging functionality to track conversions and unit tests to ensure accuracy.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/temperature-converter.git
   cd temperature-converter
   ```

2. **Ensure you have Python installed** (Python 3 recommended). You can check by running:
   ```bash
   python --version
   ```


## Usage

To use the Temperature Converter CLI, run the following command:
```bash
python converter_cli.py <temperature_value> <input_scale> <output_scale>
```

### Example Conversions:
- Convert 100 Celsius to Fahrenheit:
  ```bash
  python converter_cli.py 100 1 2
  ```
  **Output:**
  ```
  Accepted temperature: 100° Celsius, Converted to 212.0° Fahrenheit
  ```
- Convert 32 Fahrenheit to Kelvin:
  ```bash
  python converter_cli.py 32 2 3
  ```
  **Output:**
  ```
  Accepted temperature: 32° Fahrenheit, Converted to 273.15° Kelvin
  ```

### Scale Mapping:
- **1:** Celsius
- **2:** Fahrenheit
- **3:** Kelvin

## Running Tests

To run unit tests and ensure the accuracy of the conversion functions, execute:
```bash
python -m unittest tests.test_converter
```

This will run all test cases in `tests/test_converter.py` and display results.

## Logging

This project includes a logging system to track conversions. The logger records each conversion made using the CLI and stores it in a log file.

- **Setup Logging:** The `logger.py` module initializes logging.
- **Log Conversion:** Each conversion is logged with details about the input and output temperatures.
- **View Logs:** Check the generated log file (`conversion.log`) for a history of conversions.