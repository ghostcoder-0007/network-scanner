import socket
import sys
from datetime import datetime

def scan_host(target_ip, ports):
    print("-" * 50)
    print(f"Scanning target: {target_ip}")
    print(f"Time started: {str(datetime.now())}")
    print("-" * 50)
    
    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port}: OPEN")
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] Exiting script.")
        sys.exit()
        
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
        sys.exit()
        
    except socket.error:
        print("\n[!] Could not connect to server.")
        sys.exit()

if __name__ == "__main__":
    # Standard ports for infrastructure auditing
    target = "127.0.0.1"
    target_ports = [21, 22, 23, 25, 80, 443, 8080]
    scan_host(target, target_ports)
