# This is the main executable for ScamWatch.

from monitor_and_block import monitor_process

def main():

    print("ScamWatch is running!")

    try:
        # monitor and block RCA processes based on exe_name_list.py
        monitor_process()

    # this may be temporary
    except KeyboardInterrupt:
        print("ScamWatch has been stopped by user!")

    except Exception as e:

        print(f"Something went wrong! Here's the error info: {e}")



# Run this script as an executable, not as a file to import
if __name__ == "__main__":
    main()