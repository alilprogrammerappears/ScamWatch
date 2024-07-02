# This is the main executable for ScamWatch.
import threading
import time
import sys
from process_blocking import monitor_process, one_time_connection
from elevate import is_admin, run_as_admin
from network_blocking import block_all_ports, check_ports_blocked, unblock_all_ports


def main():

    print("ScamWatch is running!")

    # Check if in admin mode. If not, restart as admin
    if not is_admin() and "--elevated" not in sys.argv:
        print("Attempting to restart with administrative privileges...")
        if run_as_admin():
            print("Restarted with administrative privileges.")
            sys.exit(0)  # Terminate the current process to restart as admin
        else:
            print("Failed to restart with administrative privileges.")
            sys.exit(1)
    
# --------------------NOT YET WORKING :(---------------------------------------------------
    # Check and block common remote connection ports
    # ports list listed in config.json
    """  try:
        # unblock_all_ports()
        if not check_ports_blocked():
            print("Some ports are not blocked. Blocking them now...")
            block_all_ports()
            check_ports_blocked()
 
    except Exception as e:

        print(f"Something went wrong! Here's the error info: {e}") """
 #------------------------------------------------------------------------------------------

    # Begin monitoring processes for common RCA App exes
    # Uses threading for a continuous process
    try:

        monitor_thread = threading.Thread(target=monitor_process)
        monitor_thread.start()

# --------------------test triggering the one-time connection -------------------------------

        # time.sleep(5)  # Wait for 5 seconds before pausing for testing purposes
        # print("Pausing monitoring for one-time connection.")
        # one_time_connection()

        # Wait for the monitoring thread to complete (it will run indefinitely)
        # monitor_thread.join()

# --------------------end of one-time connection test-----------------------------------------

    except KeyboardInterrupt:
        print("ScamWatch has been stopped by user!")

    except Exception as e:

        print(f"Something went wrong! Here's the error info: {e}")


# Run this script as an executable, not as a file to import
if __name__ == "__main__":
    main()