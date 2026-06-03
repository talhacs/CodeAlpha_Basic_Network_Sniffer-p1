import sys
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_callback(packet):
    """Parses and logs network layer traffic payloads."""
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = "UNKNOWN"
        details = ""

        if TCP in packet:
            protocol = "TCP"
            details = f"Src Port: {packet[TCP].sport} -> Dst Port: {packet[TCP].dport}"
        elif UDP in packet:
            protocol = "UDP"
            details = f"Src Port: {packet[UDP].sport} -> Dst Port: {packet[UDP].dport}"
        elif ICMP in packet:
            protocol = "ICMP"
            details = f"Type: {packet[ICMP].type}"

        print("-" * 75)
        print(f"[+] Packet: {src_ip} --({protocol})--> {dst_ip}")
        if details:
            print(f"    Info: {details}")

        # Capture and display raw payload strings
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            readable = payload.decode('utf-8', errors='replace').replace('\n', ' ')
            print(f"    Payload Snapshot: {readable[:90]}...")

def main():
    print("=" * 75)
    print("             CODEALPHA LINUX NETWORK TRAFFIC SNIFFER INITIALIZED           ")
    print("=" * 75)
    try:
        # store=0 prevents memory bloating during prolonged captures
        sniff(prn=packet_callback, store=0)
    except PermissionError:
        print("\n[!] Access Denied. You MUST run this script with 'sudo' privileges!")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[-] Sniffer halted safely by operator.")
        sys.exit(0)

if __name__ == "__main__":
    main()
