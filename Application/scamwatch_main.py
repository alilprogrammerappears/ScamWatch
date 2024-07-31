# This is the main executable for ScamWatch.
import threading
import sys
import logging
from process_blocking import monitor_process
from elevate import is_admin, run_as_admin
from port_blocking import block_all_ports
from ui_windowsShortcut import check_and_create_shortcut


def scamwatch_main():

    # Set up log file
    log_file = 'ScamWatch.log'

    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s'
    )

    logging.info(f"ScamWatch is running!")

    # Check if in admin mode. If not, restart as admin
    if not is_admin() and "--elevated" not in sys.argv:
        logging.info(f"Attempting to restart with administrative privileges...")
        if run_as_admin():
            logging.info(f"Restarted with administrative privileges.")
            sys.exit(0)  # Terminate the current process to restart as admin
        else:
            logging.error(f"Failed to restart with administrative privileges.")
            sys.exit(1)
    
    try:

        # Check and create a windows shortcut before ex
        logging.info("Checking for a Windows shortcut and creating one if needed")
        shortcut_thread = threading.Thread(target=check_and_create_shortcut)
        shortcut_thread.start()

        # Check and block common remote connection ports
        logging.info(f"Blocking remote connection ports if needed...")
        port_blocking_thread = threading.Thread(target=block_all_ports)
        port_blocking_thread.start()

        # Begin monitoring processes for common RCA App exes
        logging.info(f"Now monitoring for RCA applications. Don't worry, you're safe :)")
        monitor_thread = threading.Thread(target=monitor_process)
        monitor_thread.start()

        monitor_thread.join()

    except KeyboardInterrupt:
        logging.warning("ScamWatch has been stopped by user!")

    except Exception as e:
        logging.error(f"Something went wrong! Here's the error info: {e}")


# Run this script as an executable, not as a file to import
if __name__ == "__main__":
    scamwatch_main()