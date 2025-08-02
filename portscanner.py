import socket

# Function to scan a single port
def scan_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second

        # Try to connect to the port
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is closed")

        sock.close()
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

# Function to scan multiple ports
def scan_ports(ip, start_port, end_port):
    print(f"[*] Starting scan on {ip} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

# Get user input
target_ip = input("Enter target IP address: ")
start = int(input("Enter starting port: "))
end = int(input("Enter ending port: "))

# Start scanning
scan_ports(target_ip, start, end)


# Linux Pingu 