import sys
import socket
import multiprocessing

# Function to probe a single port
def probe_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        sock.close()
        return port if r == 0 else None
    except Exception as e:
        return None

# Function to probe a single port using a wrapper function
def probe_port_wrapper(args):
    ip, port = args
    return probe_port(ip, port)

# Function to scan ports and detect services using multiprocessing
def scan_ports(ip, ports, num_threads):
    pool = multiprocessing.Pool(num_threads)
    open_ports = list(filter(None, pool.map(probe_port_wrapper, [(ip, port) for port in ports])))
    return open_ports

def main():
    ip = input("Enter the target IP: ")
    ports = range(1, 10000)  # You can specify a different port range
    num_threads = int(input("Enter the number of threads to use (e.g., 10): "))

    try:
        open_ports = scan_ports(ip, ports, num_threads)
        if open_ports:
            print("Open Ports:")
            for port in open_ports:
                print(port)
        else:
            print("Looks like no ports are open :(")
    except KeyboardInterrupt:
        print("\nScan canceled by user.")

if __name__ == "__main__":
    main()
