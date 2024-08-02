# This file manages the pause state for monitoring. Pausing allows for a one-time connection
import os


# write pause state from shared file
# shared file used to communicate between GUI and backend
PAUSE_FILE = "pause_state.txt"

def set_pause(state):
    with open(PAUSE_FILE, 'w') as f:
        f.write("paused" if state else "active")

def is_paused():
    if not os.path.exists(PAUSE_FILE):
        return False
    with open(PAUSE_FILE, 'r') as f:
        state = f.read().strip()
    return state == "paused"