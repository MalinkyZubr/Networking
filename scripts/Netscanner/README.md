# Algorithm
1. Get network information (netmask, interface IP)
2. Create list of objects representing different connections and IPs
3. generate an ARP request packet for each possible IP on the network. Assign that packet to the IP object
4. break the request list into segments to multithread the requests
5. Broadcast ARP requests in parallel order to get the mac addresses using scapy and hostnames using socket, and maybe other system information
6. save received information into 