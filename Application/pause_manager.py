# This file manages the pause state for monitoring. Pausing allows for a one-time connection
import os
import logging

# Set up log file
log_file = 'ScamWatch.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)


# write pause state from shared file
# shared file is used to communicate between GUI and backend
PAUSE_FILE = "pause_state.txt"

def set_pause(state):
    try:
        with open(PAUSE_FILE, 'w') as f:
            f.write("paused" if state else "active")
    except Exception as e:
        logging.error(f"Something went wrong! Here's the error info: {e}")

def is_paused():
    try:
        if not os.path.exists(PAUSE_FILE):
            return False
        with open(PAUSE_FILE, 'r') as f:
            state = f.read().strip()
        return state == "paused"
    except Exception as e:
        logging.error(f"Something went wrong! Here's the error info: {e}")