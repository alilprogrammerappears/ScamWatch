import psutil
import smtplib

from ports_list from suspicious_ports

def list_connections():
    # Here we can list all current network connection
    for conn in psutil.net_connections(kind='inet'):
        try:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
            status = conn.status
            pid = conn.pid
            process_name = psutil.Process(pid).name() if pid else "Unknown"
            print(f"Local: {laddr}, Status: {status}, PID: {pid}, Process: {process_name}")
        except Exception as e:
            print(f"Error processing connection: {e}")

def block_process_by_pid(pid):
    try:
        psutil.Process(pid).terminate()
        print(f"Terminated process {pid}")
    except Exception as e:
        print(f"Failed to terminate process {pid}: {e}")

def block_suspicious_connections():
    
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED':  # Considering active connections
            if is_suspicious_connection(conn):
                print(f"Blocking suspicious connection: {conn}")
                if conn.pid:  
                    block_process_by_pid(conn.pid)