# This file is for the following ScamWatch functions: Monitor processes and block the exe from running.

# It additionally provides a pop up to the user. This pop up should be made much better in the future.

import psutil
import ctypes
import time
from exe_name_list import EXE_NAME_LIST


# Check for process and return a Process object if found
def check_for_processes(process_name):
    process_name = process_name.lower()

    return [process for process in psutil.process_iter(['pid', 'name']) if process.info['name'].lower() == process_name]


# Terminate the Process
def block_process(process):

    try:
        process.terminate()
        # Allow the process to terminate
        process.wait()
        show_warning()
    except psutil.NoSuchProcess:
        # In case the process has already been terminated
        pass


# Continiously monitor process list
def monitor_process():

    while True:
        for process_name in EXE_NAME_LIST:
            processes = check_for_processes(process_name)
            for process in processes:
                block_process(process)
        time.sleep(1)


# temp notification window
def show_warning():

    ctypes.windll.user32.MessageBoxW(
        0,
        "WARNING! This may be a remote connection scam!",
        "Don't worry, however, we have blocked this program and you are safe!",
        1
    )

