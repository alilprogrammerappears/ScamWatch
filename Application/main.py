# This is the main executable for ScamWatch.
import threading
import time
import sys
from process_blocking import monitor_process, one_time_connection
from elevate import is_admin, run_as_admin
from network_blocking import check_all_ports_blocked, block_all_ports, block_single_port, unblock_all_ports, check_port_blocked

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
    
    try:

        # Check and block common remote connection ports
        print("Blocking remote connection ports if needed...")
        block_all_ports()

        # Begin monitoring processes for common RCA App exes
        print("Now monitoring for RCA applications. Rest assured, you're safe :)")
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