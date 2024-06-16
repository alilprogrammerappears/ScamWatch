# This file manages the pause state for monitoring. Pausing allows for a one-time connection

# Global variable to control the pause state
pause_monitoring = False

def set_pause(state):
    # false to resume, true to pause

    global pause_monitoring
    pause_monitoring = state

def is_paused():
    # bool: True if monitoring is paused, False otherwise.
    
    return pause_monitoring
