# Define the Gunicorn configuration
bind = '0.0.0.0:8000'  # Bind to all interfaces on port 8000

# Configure logging to ignore less severe log messages
loglevel = 'info'

# Disable Gunicorn's internal logging
errorlog = '-'  # Log to stdout/stderr

# Disable access logging
accesslog = '-'

# Configure the Gunicorn logger
logger_class = 'gunicorn.glogging.Logger'