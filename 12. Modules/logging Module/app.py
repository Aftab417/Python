
#################------------------   logging   -----------------------#####################

#  This is python built-in  logging system that  keep track and record event that heppens when your program 
#  runs like (errors, warnings, or workflow updates)



# importing module
import logging


#  Configuring module
logging.basicConfig(level=logging.INFO)        # only show logs on console

# Creating instance of module
logger = logging.getLogger(__name__)



# Usage in code to show infor or error messages
logger.info('This is info message.')
logger.error('This is error message.')




##################-------------  Configuring logs in separate File  ----------------#######################

#  Above logging configuration show logs only on console. But this configuration also store logs in separate file.

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s",   # Logs formate showing on file and console
    handlers=[
        logging.FileHandler('log_file'),   # save logs to file
        logging.StreamHandler()            # still show logs on console
    ]
)


##################-------------  Log Levels  ----------------#######################


logging.basicConfig(level=logging.INFO)

 
# level=logging.INFO means:

# Only logs INFO, WARNING, ERROR, CRITICAL messages.

# It will ignore DEBUG messages.

# Example levels:

# DEBUG → Detailed info (for developers).

# INFO → General updates (normal operation).

# WARNING → Something unexpected, but still running.

# ERROR → A problem occurred.

# CRITICAL → Serious problem, program may crash.