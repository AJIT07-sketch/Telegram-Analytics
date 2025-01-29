import logging
import os

# Ensure the logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Log format
log_format = "%(asctime)s - %(levelname)s - %(message)s"

# Application log setup
app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)
app_handler = logging.FileHandler("logs/app.log")  # App logs
app_handler.setFormatter(logging.Formatter(log_format))
app_logger.addHandler(app_handler)

# Error log setup
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler("logs/error.log")  # Error logs
error_handler.setFormatter(logging.Formatter(log_format))
error_logger.addHandler(error_handler)

                            
