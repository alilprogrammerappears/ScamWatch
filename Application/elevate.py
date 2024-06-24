# An error can occur in which some processes require elevated privileges to be terminated, which
# ScamWatch does not have. This file checks if it is running with admin privileges and if not,
# tries to restart itself with privileges.

import ctypes
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        return True

    try:
        # Re-launch the script with admin rights and add a flag
        params = ' '.join([os.path.abspath(sys.argv[0])] + sys.argv[1:] + ["--elevated"])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1)
        return True
    except Exception as e:
        print(f"Failed to elevate process: {e}")
        return False
