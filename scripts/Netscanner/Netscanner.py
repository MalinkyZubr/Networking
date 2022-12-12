import warnings
warnings.filterwarnings("ignore")
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=DeprecationWarning)
    import scapy.all as scapy
    import multiprocessing
    import socket
    import numpy as np
    from iterator_proto import get_ips
    import subprocess
    from getmac import get_mac_address as gma
    import re
    import json
    from OuiLookup import OuiLookup
    import datetime
    import sys
    import time


scapy.conf.layers.filter([scapy.Ether, scapy.ARP])


class Scanner:
    def __init__(self, network: str):
        self.responses = []
        arp_table = subprocess.check_output(['arp', '-a']).decode().strip()

        self.__network_ip = network
        self.ip_stripped = network.split("/")[0]
        self.__ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        today = datetime.datetime.now()
        self.__session = f"{today.year}_{today.month}_{today.day}"

    def generate_packets(self):
        ips = get_ips(self.__network_ip)
        packets = list(map(lambda ip: self.__ether / scapy.ARP(pdst=ip), ips))
        return packets

    def extract_data(self, result):
        for sent, received in result:
            information = {'ip': received.psrc, 'mac': received.hwsrc, 'hostname': None, 'device_distributor': 'Unknown'}
            try:
                socket.gethostbyaddr(received.psrc)
                information['device_distributor'] = list(OuiLookup().query(information['mac'])[0].values())[0]
                information['hostname'] = socket.gethostbyaddr(received.psrc)[0]
            except socket.herror:
                information['hostname'] = "NaN"
            #print(f'IP: {information["ip"]}\nMAC: {information["mac"]}\nHostname: {information["hostname"]}\n')
            return information

    def get_response(self, packet):
        result = scapy.srp(packet, timeout=1, verbose=0)[0]
        return self.extract_data(result)

    def generate_responses(self, packets):
        print("Generating responses...")
        start = time.time()
        pool = multiprocessing.Pool(processes=20)
        responses = list(pool.map(self.get_response, packets))
        end = time.time()
        print(f"Finished in {end-start} seconds.")
        return list(filter(lambda x: x is not None, responses))

    def write_file(self, information):
        with open(f"{self.ip_stripped}_{self.__session}.json", 'w') as f:
            f.write(json.dumps(information) + "\n")

    def format_data(self, information, file_write=True):
        if file_write:
            self.write_file(information)
        print("IP\t\t\tMAC\t\t\tHostname\t\t\t\t\t\tDistributor")
        for host in information:
            print(f"{host['ip']}\t\t{host['mac']}\t{host['hostname']}\t\t\t\t\t\t\t{host['device_distributor']}")

    def main(self):
        information = self.generate_responses(self.generate_packets())
        self.format_data(information)


if __name__ == "__main__":
    try:
        #IP = str(input("Enter your IP here: "))
        scanner = Scanner("10.2.30.0/24")
    except:
        print("Failed. See how to format IPs")
        sys.exit(0)

    scanner.main()





    
