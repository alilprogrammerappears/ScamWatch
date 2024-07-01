# This is the main executable for ScamWatch.
import threading
import time
import sys
from monitor_and_block import monitor_process, one_time_connection
from elevate import is_admin, run_as_admin
from network_blocking import block_suspicious_connections

def main():

    print("ScamWatch is running!")

    """ if not is_admin() and "--elevated" not in sys.argv:
        print("Attempting to restart with administrative privileges...")
        if run_as_admin():
            print("Restarted with administrative privileges.")
            sys.exit(0)  # Terminate the current process to restart as admin
        else:
            print("Failed to restart with administrative privileges.")
            sys.exit(1) """
    

    
    print("Running with administrative privileges.")
    try:
       # Start monitoring in a separate thread
        monitor_thread = threading.Thread(target=monitor_process)
        monitor_thread.start()

         # Start continuous blocking in a separate thread
        blocking_thread = threading.Thread(target=block_suspicious_connections)
        blocking_thread.start()

        # test triggering the one-time connection
        # time.sleep(5)  # Wait for 5 seconds before pausing for testing purposes
        # print("Pausing monitoring for one-time connection.")
        # one_time_connection()

        # Wait for the monitoring thread to complete (it will run indefinitely)
        # monitor_thread.join()

    # this may be temporary
    except KeyboardInterrupt:
        print("ScamWatch has been stopped by user!")

    except Exception as e:

        print(f"Something went wrong! Here's the error info: {e}")


# Run this script as an executable, not as a file to import
if __name__ == "__main__":
    main()