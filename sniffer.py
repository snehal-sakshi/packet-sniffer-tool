import socket

def sniff_packets():
    # Create a raw socket and bind it to the public interface
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    host = socket.gethostbyname(socket.gethostname())
    sniffer.bind((host, 0))

    # Include the IP headers
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # Enable promiscuous mode (Windows-specific, requires admin privileges)
    # On Linux, use `ifconfig <interface> promisc` before running
    try:
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    except AttributeError:
        pass  # Linux doesn't require ioctl for promiscuous mode

    print(f"Sniffer started on {host}...")
    
    try:
        while True:
            # Receive a packet
            raw_packet = sniffer.recvfrom(65565)
            print(raw_packet)
    except KeyboardInterrupt:
        print("\nStopping sniffer.")
        # Disable promiscuous mode (Windows-specific)
        try:
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        except AttributeError:
            pass

if __name__ == "__main__":
    sniff_packets()
