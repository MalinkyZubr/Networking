import sys
from datetime import datetime
from scapy.all import srp, Ether, ARP, conf
import socket


if __name__ == "__main__":
    try:
        interface = str(input("[+] Enter interface: "))
        ips = input("[+} enter range of ips to scan for: ")
    except KeyboardInterrupt:
        print("\n[+] Cancelling")
        sys.exit(1)
    
    print("[+] Scanning...")
    start_time = datetime.now()
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ips), timeout=2, iface=interface, inter=0.1) # returns two list, one of answered and unanswered packets
    print("MAC                         IP                         Hostname\n") # set up for result display
    for snd, rcv in ans:
        try:
            print(f"{rcv.hwsrc}       {rcv.psrc}                    {socket.gethostbyaddr(rcv.psrc)[0]}")
        except socket.herror:
            print(f"{rcv.hwsrc}       {rcv.psrc}                    NaN")

    stop_time = datetime.now()
    total_time = stop_time - start_time
    print(f"[+] Scan complete in {total_time} seconds")


