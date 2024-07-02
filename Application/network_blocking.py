import json
import subprocess
from elevate import is_admin

# Load list of common remote connection ports
def load_ports_from_json(file_path="config.json"):
    try:
        with open(file_path, "r") as file:
            config = json.load(file)
            ports = config.get("ports", [])
        return set(config.get("ports", []))
    except FileNotFoundError:
        print("Configuration file not found. Using default settings.")
    except json.JSONDecodeError:
        print("Error decoding configuration file. Using default settings.")

PORTS_SET = load_ports_from_json()

# block all ports from the ports list in config.json
def block_all_ports():

    if not is_admin():
        print("ScamWatch requires administrative privileges to block ports.")
        print("Please restart ScamWatch with administrative rights.")
        return

    for port in PORTS_SET:
        if not check_port_rule_exists(port):
            try:
                subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule",
                                f"name=Block Port {port}", "dir=in", "action=block", f"protocol=TCP",
                                f"localport={port}", f"remoteip=any"],
                            check=True)
                subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule",
                                f"name=Block Port {port}", "dir=in", "action=block", f"protocol=UDP",
                                f"localport={port}", f"remoteip=any"],
                            check=True)
                print(f"Firewall rule added to block port {port}.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to block port {port}: {e}")
        else:
            print(f"Firewall rule for port {port} already exists. Skipping.")

# block a single port
def block_single_port(port):

    if not is_admin():
        print("ScamWatch requires administrative privileges to block ports.")
        print("Please restart ScamWatch with administrative rights.")
        return

    try:
        subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule",
                        f"name=Block Port {port}", "dir=in", "action=block", f"protocol=TCP",
                        f"localport={port}", f"remoteip=any"],
                       check=True)
        subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule",
                        f"name=Block Port {port}", "dir=in", "action=block", f"protocol=UDP",
                        f"localport={port}", f"remoteip=any"],
                       check=True)
        print(f"Firewall rule added to block port {port}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to block port {port}: {e}")


# unblock all ports from the ports list in config.json
# this is essentially just to fix things quickly if it gets fucked up.
# Maybe remove this in the final product and leave unblock_one_port()
def unblock_all_ports():

    if not is_admin():
        print("ScamWatch requires administrative privileges to unblock ports.")
        print("Please restart ScamWatch with administrative rights.")
        return

    try:
        for port in PORTS_SET:
            unblock_single_port(port)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while unblocking ports: {e}")


# Unblock a single port. Use if a legitimate remote connection is required
def unblock_single_port(port):
    
    if not is_admin():
        print("ScamWatch requires administrative privileges to unblock ports.")
        print("Please restart ScamWatch with administrative rights.")
        return

    try:
        subprocess.run(["netsh", "advfirewall", "firewall", "delete", "rule",
                        f"name=Block Port {port}", f"protocol=TCP", f"localport={port}"],
                       check=True)
        subprocess.run(["netsh", "advfirewall", "firewall", "delete", "rule",
                        f"name=Block Port {port}", f"protocol=UDP", f"localport={port}"],
                       check=True)
        print(f"Firewall rule removed to unblock port {port}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to unblock port {port}: {e}")


# check if a specific port is blocked
# Returns true if it is
def check_port_blocked(port):

    try:
        # Check TCP and UDP rules separately for the port
        tcp_rule = subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule", f"name=Block Port {port}",
                                   "protocol=TCP"], capture_output=True, text=True)
        udp_rule = subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule", f"name=Block Port {port}",
                                   "protocol=UDP"], capture_output=True, text=True)

        # Check if either TCP or UDP rule output indicates that the port is blocked
        return "Block" in tcp_rule.stdout and "Block" in udp_rule.stdout
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while checking port {port}: {e}")
        return False


# checks if all of the ports from the ports list in config.json are blocked
# prints result
def check_ports_blocked():

    print("Checking blocked status for ports in PORTS_SET:")
    for port in PORTS_SET:
        if check_port_blocked(port):
            print(f"Port {port} is blocked.")
        else:
            print(f"Port {port} is NOT blocked.")


# Function to check if a specific port rule exists
def check_port_rule_exists(port):
    try:
        # Check TCP and UDP rules separately for the port
        tcp_rule = subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule", f"name=Block Port {port}",
                                   "protocol=TCP"], capture_output=True, text=True)
        udp_rule = subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule", f"name=Block Port {port}",
                                   "protocol=UDP"], capture_output=True, text=True)

        # Check if either TCP or UDP rule output indicates that the port is blocked
        return "Block" in tcp_rule.stdout and "Block" in udp_rule.stdout
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while checking port {port}: {e}")
        return False