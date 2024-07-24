# This file is for the following ScamWatch functions: Monitor processes and block the exe from running.

# It additionally provides a pop up to the user. This pop up should be made much better in the future.

import psutil
import ctypes
import time
import json
import threading
import logging
from pause_manager import is_paused, set_pause
from external_alerts import send_alert_email
from ui_notification import show_custom_alert

# Load exe name list
def load_exe_names_from_json(file_path="config.json"):
    try:
        with open(file_path, "r") as file:
            config = json.load(file)
            exe_names = config.get("exe_names", [])
        return set(name.lower() for name in exe_names)
    except FileNotFoundError:
        logging.info("Configuration file not found. Using default settings.")
    except json.JSONDecodeError:
        logging.error("Error decoding configuration file. Using default settings.")

EXE_NAME_SET = load_exe_names_from_json()

# Check for process and return a Process object if found
def check_for_processes(process_names_set):
    
    found_processes = []

    for process in psutil.process_iter(['pid', 'name']):
        try:
            if process.info['name'].lower() in process_names_set:
                found_processes.append(process)
                logging.info(f"Found process: {process.info['name']} (pid: {process.pid})")  # Debug statement
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return found_processes


# Terminate the Process
def block_process(process, warned_processes):

    try:
        if process.info['name'].lower() not in warned_processes:
            process.terminate()
            logging.info(f"Terminated process: {process.info['name']} (pid: {process.pid})")  # Debug statement
            # Allow the process to terminate
            process.wait()
            threading.Thread(target=show_warning).start()
            trusted_contact_email = 'kassandra.montgomery@student.kpu.ca' # Testing purposes only!
            threading.Thread(target=send_alert_email, args=(trusted_contact_email,)).start()
            warned_processes.add(process.info['name'].lower())
    except psutil.NoSuchProcess:
        # In case the process has already been terminated
        pass
    except psutil.AccessDenied:
        # Handle the AccessDenied exception
        logging.error(f"Access denied for terminating process: {process.info['name']} (pid: {process.pid}). Scamwatch needs elevated privileges")

# Continiously monitor process list
def monitor_process():

    # Set to keep track of warned pids
    warned_processes = set()

    while True:
        if is_paused():
                logging.info("Monitoring paused.")
                time.sleep(30)  # Pause for 30 seconds for testing (change to 1800 for 30 minutes)
                set_pause(False)
                logging.info("Monitoring resumed.")
        else:
            processes = check_for_processes(EXE_NAME_SET)
            for process in processes:
                block_process(process, warned_processes)
            time.sleep(1)
            warned_processes.clear()  # Clear set each cycle to allow for new warnings

# allow a short connection by pausing monitoring
def one_time_connection():
    set_pause(True)

# temp notification window
def show_warning():

    def warning_message():
        ctypes.windll.user32.MessageBoxW(
            0,
            "WARNING! This may be a remote connection scam!\nDon't worry, however, we have blocked and you are safe!",
            "ScamWatch Alert",
            0x40 | 0x1 | 0x40000  # MB_ICONWARNING | MB_OK | MB_TOPMOST
        )

    threading.Thread(target=warning_message).start()