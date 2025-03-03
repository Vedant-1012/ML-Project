import logging
import os
from datetime import datetime

# Get the current timestamp for the log file name
LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'

# Define the path for logs folder
logs_dir = os.path.join(os.getcwd(), 'logs')

# Create the 'logs' directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Define the complete path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Set up logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

logging.info("Logging setup completed successfully")
