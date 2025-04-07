import logging
import os
from datetime import datetime

# Get the parent directory of the current file (which will be your project root)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create logs directory outside src
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(ROOT_DIR, "logs")
os.makedirs(logs_path, exist_ok=True)

log_file_path = os.path.join(logs_path, log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


