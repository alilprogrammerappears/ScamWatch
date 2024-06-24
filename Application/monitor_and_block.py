# This file is for the following ScamWatch functions: Monitor processes and block the exe from running.

# It additionally provides a pop up to the user. This pop up should be made much better in the future.

import psutil
import ctypes
import time
from exe_name_list import EXE_NAME_LIST
from pause_manager import is_paused, set_pause


# Check for process and return a Process object if found
def check_for_processes(process_name):
    process_name = process_name.lower()

    return [process for process in psutil.process_iter(['pid', 'name']) if process.info['name'].lower() == process_name]


# Terminate the Process
def block_process(process, warned_processes):

    try:
        if process not in warned_processes:
            process.terminate()
            # Allow the process to terminate
            process.wait()
            show_warning()
            warned_processes.add(process.info['name'].lower())
    except psutil.NoSuchProcess:
        # In case the process has already been terminated
        pass
    except psutil.AccessDenied:
        # Handle the AccessDenied exception
        print(f"Access denied for terminating process: {process.info['name']} (pid: {process.pid}).")
        print(f"ScamWatch needs elevated")

# Continiously monitor process list
def monitor_process():

    # Set to keep track of warned pids
    warned_processes = set()

    while True:
        if is_paused():
                print("Monitoring paused.")
                time.sleep(30)  # Pause for 30 seconds for testing (change to 1800 for 30 minutes)
                set_pause(False)
                print("Monitoring resumed.")
        else:
            for process_name in EXE_NAME_LIST:
                processes = check_for_processes(process_name)
                for process in processes:
                    block_process(process, warned_processes)
            time.sleep(1)
            warned_processes.clear() # Clear set each cycle to allow for new warnings

# allow a short connection by pausing monitoring
def one_time_connection():
    set_pause(True)

# temp notification window
def show_warning():
    ctypes.windll.user32.MessageBoxW(
        0,
        "WARNING! This may be a remote connection scam!\nDon't worry, however, we have blocked and you are safe!",
        "ScamWatch Alert",
        0x40 | 0x1 | 0x40000  # MB_ICONWARNING | MB_OK | MB_TOPMOST
    )


