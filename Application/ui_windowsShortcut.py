import os
import winshell
from win32com.client import Dispatch

def check_and_create_shortcut():
    # Define the shortcut name and target file
    shortcut_name = "ScamWatch"
    script_file = "ui_design.py"
    
    # Get the absolute path of the script file
    current_directory = os.path.abspath(os.path.dirname(__file__))
    script_path = os.path.join(current_directory, script_file)
    
    # Define the path to the Python executable
    python_executable = r"C:\Users\chauh\Documents\GitHub\info4190\ScamWatch\Application\ui_design.py"
    
    # Define the path to the Start Menu
    startmenu_path = winshell.start_menu()
    shortcut_path = os.path.join(startmenu_path, f"{shortcut_name}.lnk")
    
    # Check if the shortcut already exists
    if os.path.exists(shortcut_path):
        print(f"Shortcut '{shortcut_name}' already exists.")
    else:
        print(f"Creating shortcut '{shortcut_name}'...")
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = python_executable
        shortcut.Arguments = script_path
        shortcut.WorkingDirectory = current_directory
        shortcut.save()
        print(f"Shortcut '{shortcut_name}' created successfully.")

# Run the function
check_and_create_shortcut()

