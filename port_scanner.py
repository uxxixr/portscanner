import socket
import sys

# Function to scan a specific port
def scan_port(target, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout of 1 second per port
        
        # Try to connect to the target host on the given port
        result = sock.connect_ex((target, port))
        
        if result == 0:  # If result is 0, the port is open
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        # Close the socket connection
        sock.close()
        
    except socket.error:
        print(f"Couldn't connect to {target}")
        sys.exit()

# Function to scan a range of ports on the target
def scan_ports(target, start_port=1, end_port=1024):
    print(f"Scanning target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}\n")
    
    try:
        # Resolve the hostname to an IP address
        target_ip = socket.gethostbyname(target)
        print(f"Resolved {target} to {target_ip}\n")
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit()
    
    # Scan each port in the specified range
    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

# Main entry point of the script
if __name__ == "__main__":
    # User input: target website and optional port range
    target = input("Enter the target website or IP address: ")
    
    # Ask user if they want to scan a specific range of ports
    start_port = int(input("Enter the starting port (default is 1): ") or 1)
    end_port = int(input("Enter the ending port (default is 1024): ") or 1024)
    
    # Scan the ports on the given target
    scan_ports(target, start_port, end_port)
