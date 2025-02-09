import logging

# Set up logging configuration
def setup_logging():
    logging.basicConfig(
        filename='temperature_conversion.log',  # Log file name
        level=logging.INFO,  # Log level (INFO will log all levels above it)
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
        datefmt='%Y-%m-%d %H:%M:%S'  # Date format for log entries
    )

# Function to log conversion details
def log_conversion(input_temp, input_unit, output_temp, output_unit):
    logging.info(f"Converted {input_temp} {input_unit} to {output_temp} {output_unit}")
