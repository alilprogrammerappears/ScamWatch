# This file is for the following ScamWatch functions: Monitor processes and block the exe from running.
# It additionally provides a pop up to the user. This pop up should be made much better in the future.

import psutil
import ctypes
import time
from exe_name_list import EXE_NAME_LIST

def process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'].lower() == process_name.lower():
            return True
    return False

