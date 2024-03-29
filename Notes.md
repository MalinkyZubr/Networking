# CCNA Networking full course

## Network Devices
A computer network is a digital telecom network which allows nodes to share resources

### Router
provide connection to the internet, usually connected to LAN switches. 
* fewer network interfaces than switches
* forward data between LANs

### Switch
Aggregates connections of large numbers of devices. Allows several devices to interface with one another on a local area network LAN

* usually have many ports to connect to, 24+
* Provide connectivity to hosts in the same LAN
* do not provide connectivity to the wider internet

### Firewall
Specialty network security devices that control network traffic. Can be placed outside of the network, or inside the network. PRovide protection to end hosts. Must be configured with security rules to determine what traffic to let in
can allow connections from designated addresses, and reject from elsewhere, or on some ports
* monitor and control network traffic based on configured rules
* Outside or inside the network
* Next gen firewalls when they include modern and advanced filtering capablities
* can either be software or hardware based (host or network firewalls)
* software and hardware firewalls should be used in tandem

### Server
Any client or computer can be a server. A server is a device that provides functions or services for clients

### Client
device which accesses a service that is made available by a server

## interfaces and cables
How do we connect networking components together?

RJ-45 Registered Jack is for ethernet connections

ethernet is a collection of network protocols, which makes it hard to define

### Network protocols and standards
Need common operations and system to communicate, protocols provide a common language
* connections on internet operate on a set speed, in bits per second. A bit is either a 0 or 1, binary code. These are sent over wires
* A byte is 8 bits. Wires operate one bit at a time, thus network speed is measured in bits/second
* data on a hard drive is measured in bytes
* all ethernet standards are defined in the IEEE 802.3 standards

### Copper ethernet standards
1. 10 Mbps, ethernet, 802.3i, 10BASE-T, maximum length 100m
2. 100 Mbps, fast ethernet, 802.3u, 100BASE-T
3. 1 Gbps, Gigabit Ethernet, 802.3ab, 1000BASE-T
4. 10 Gbps, 10 gig ethernet 802.3an 10GBASE-T 

BASE refers to baseband signalling
T is twisted pair

* Copper cable standard is UTP
* Unshielded: no metallic shield, vulnerable to interference
* Twisted: twisted, 4 cables twisted around each other (protects against EMI electromagnetic interference)
* Pair: all wires are in pairs, so 8 total wires. As such RJ-45 has 8 wires. Only 1000Base-T and 10Gbase-T use all 8 wires, however, the other use only 2 pairs

pins can be divided into 2 types:
* Tx: transmission
* Rx: receive whichever pins transmit on one end of the connection receive on the other end. This allows full duplex transmission. Both devices can send data at the same time
* a router, firewall or computer transmits on pins 1 and 2. A switch transmits on 3 and 6

A straighthrough cable connects port 1 to port 1, 2 to 2 etc.
When dealing with connecting switches however, you need to connect 1 to 3, 2 to 6, etc, this can be done with a crossover cable

most modern networking devices have developed with Auto MDI-X. Now devices can automatically detect the Tx and Rx ports of devices and adjust.

1000Base-T and 10Gbase-T use 4, 5, and 7,8. Each pair in these standards, however, is bidirectional

### Fiber Optic COnnections
Fiber-optic cables have much longer range. On fiberoptic capable devices you need an SFP transceiver, which can convert electrical signals to light, to be sent over fiberoptic cables. 

In fiberoptic cables, you need just one cable to send, and one to receive data

* single mode fiber: narrower core diameter, light enters at a single angle from a laser based transmitter. Much longer cable length. More expensive.
* multimode fiber cable: core diameter is wider than a single mode fiber. Allows multiple angles of light waves to enter the fiberglass core. Allows longer cables than UTP but shorter cables than single mode fiber. cheaper than single mode, but lower range
  
### Fiber optic standards
* 1000BASE-LX 802.3z 1 Gbps Multimode/single mode, 550m/5km range respectively
* 10GBASE-SR 802.3ae 10 Gbps Multimode 400m
* 10GBASE-LR 802.3ae 10 Gbps Single Mode 10km
* 10GBASE-ER 802.3ae 10Gbps Single Mode 30km

### UTP VS Fiber Optic
Copper:
* Lower cost
* Shorter range
* vulnerable to EMI
* Cheaper ports RJ45
* Emit a faint signal outsid ethe cable which can be copies (security risk)
Fiber Optic:
* Higher cost than UTP
* Lnger maximum distance than UTP
* No vulnerability to EMI
* SFP ports are more expensive
* Does not emit any signals

## OSI and TCP/IP model
Networking models categorize and provide structure for networking protocols and standards

protocol: a set of rules defining how a network device and software should work

networking model <- networking protocols and standards 

### OSI Model
* Open Systems interconnection model. Open standard, not proprietary
* categorizes and conceptualizes the diffrerent function in a network
* created by the ISO international organization for standardiation. 
* Divides functions into 7 layers
* work together to make the network work

Encapsulation: data added during transit through the OSI stack. De encapsulation is the stripping of this information while travelling up the stack. This is adjacent layer interaction. Same layer interaction is interaction between the same layer of 2 stacks.

Upper layers. Not really used by network engineers. These are for application developers to work with.
* application layer: Closest to end user. interacts with software applications for example web browser. HTTP and HTTPS are layer 7 protocols. Does not include the actual applications, btu controls the interaction with those applications. identifying communication partners, and synchronizing communication.
* presentation layer: data is in an application format. Needs to be translated to a different format to go over the network. Translate between application and network formats. For example, encryption of data as it is sent. Translates between different application layer formats. Translates data to appropriate format
* Session layer: controls dialogues between hosts. Establishes, manages, and terminates connections between the local application (web browser) and the remote application (youtube).
DATA IS PREPARED

DATA

The bottom 4 layers: do the job of sending data over the network. 
* Transport layer: Segments and reassembles data for comunication betwen end hosts. Breaks big data into small data which can be more easily sent over a network, and makes problems easier to deal with if errors happen. Provides host to host communication and process to process communication. ADDS THE LAYER 4 HEADER.

DATA | L4 HEADER <- Segment

* Network layer: Provides connectivity between end hosts on different networks outside of the LAN. provides logical addressing with IP addresses. provides path selection between source and destination. Where does data go? this layer decides. Layer 3 includes routers. ADDS LAYER 3 HEADER. Includes info on source and destination IP

DATA | L4 HEADER | L3 HEADER <- Packet

* Data Link Layer: Node to node connectivity and data tranfer, pc to switch, switch to router. Defines how data is formatted for transmission over a physical medium like UTP. Detects and may correct physical layer errors. uses layer 2 addressing, separate from layer 3. Switches operate at layer 2. ADDS LAYER 2 HEADER AND TRAILER. THIS IS THE SOURCE AND DESTINATION MAC ADDRESS

L2 TRAILER | DATA | L4 HEADER | L3 HEADER | L2 HEADER <- Frame

* Physical layer: transmission over wire or wireless system. Wires, transmission range, voltages. Digital bits are converted into electrical signals for wired and radio signals for wireless connections

after reaching the physical layer, de-encapsulation takes place
all layers are stripped away until only the data is left to be used by the end user and application

1. DATA: application, presentation and session layers
2. DATA | L4 HEADER <- Segment: Transport layer
3. DATA | L4 HEADER | L3 HEADER <- Packet: network layer: adds IP address
4. L2 TRAILER | DATA | L4 HEADER | L3 HEADER | L2 HEADER <- Frame: Data Link Layer: Adds MAC address

These are all PDU's, protocol data units. Packet is a unit 3 PDU for instance
at the physical layer, the PDU is the bit.

All
People
Seem
To
Need
Data
Processing

### TCP/IP Suite
* set of communication protocols
* Known as TCP IP because those are two of the central protocols
* Similar to OSI but with fewer layers. More practical model, actually used in networks

OSI             TCP/IP
Application
Presentation    Application
Session

Transport       Transport

Network         Internet

Data Link
Physical        Link

note: when people say `layer 2 problem,` for instance, they mean with respect to the OSI model


## intro to the CLI
How do you connect to a cisco device to manage it with the CLI? 

1. Connecting to console port, either via rj45 or usb mini-b. Requires a Rollover cable to interface.
   * then you need to open a putty session, which is a terminal emulator. From there you can go to serial to modify settings for the serial connection. By default they are the same as cisco devices
   * Baud rate should be 9600 bits/second. 8 data bits. 1 stop bit. Every 8 bits of data, 1 stop bit is sent to signify the stop of the bits. Parity set to none. Parity is for detecting errors. Flow control controls flow throuhg the device, set to none.
   * When entering the router you are by default in exec mode, singified by {hostname}>. all devices have hostnames. Exec mode is useless basically. Cant make any changes to the device
   * If you enter the `enable` command, you go into priveleged exec mode. {hostname}# is priveleged exec mode. Provides complete access to view the devices configuration, restart the device, etc. However you cannot change hte config here, but can change the time and save the config file, etc. To view all commands, do ?. Ifg you want to display all commands that start with a letter, do e? for example
   * to enter global configuration mode, enter `configure terminal`
   * Protect privileged exec mode with a password. `enable password {password}`
   * to see the detailed help for a command, do `enable password ?` for instance. Must have space between command and ? 
   * To show the running configuration file, `do show running-config`
   * To show the startup config, `do show startup-config`
   * this will show nothing until we save the running configuration as a config file
   * 3 ways to do this: `write`, `write memory`, and `copy running-config startup-config`. However, when we look at this it displays the password
   * we need to do a `service password-encryption` command within configuration terminal mode. The number 7 before the encrypted password means it is using the proprietary encryption. 
   * However, there are cisco password crackers. So this is not secure. There are better passwords with tougher encryption
   * Use the `enable secret {desired password}` this will enable the secrets of cisco
   * in order to run out of level commands in the config mode, use the `do` command. `do show run` for instance
   * how do you cancel a command you executed? do: `no {previous command you want to cancel}`

Commands:
1. `enable`: enter priveleged exec mode
2. `configure terminal`: enter global configuration mode
3. `enable password {password}`: create a password for priveleged exec mode
4. `service password-encryption`: encrypts all passwords
5. `enable secret {password}`: makes  a more secure password. If run with password, it is disabled
6. `do {priveleged exec level command}`: run exec commands from global config mode
7. `no {command}`: remove a command previously configured
8. `show running-config`: displays active configuration file
9. `show startup-config`: displays the saved configuration file which will be loaded if the device is restarted
10. `write`: saves configuration
11. `write memory`: saves configuration
12. `copy running-config startup-config`: saves configuration
13. `hostname {hostname}`: change hostname

## Ethernet LAN Switching
This is the Data Link layer

LANs, switches can expand an existing lan, routers connect lans together. How is data sent over lans?

Focusing on how switches transfer and use ethernet frames. Ethernet is the protocl used by almost all LANs

There are 5 fields in the fram header:
* preamble
* Start Frame Delimeter
used for synchronization to prepare device to receive data
* destination, destination mac address
* Source, Source mac address
* Type, Layer 3 protocol used for the address, IP address ( might also be length)

trailer:
* only the frame check sequence, to detect layer errors

### Preamble and SFD
#### Preamble
* 7 bytes long, 56 bits
* synchronizes the receiver clocks of 2 devices
* each byte is 10101010

#### SFD
* start frame delimeter
* 1 byte long
* each byte is 10101011
* end fo the preamble and the beginning of the rest of the frame

### Destination and Source 
* Indicates the devices sending and receiving the fram
* consist of the destination and source MAC address
* 6 byte address of the physical device assigned to the device when its made

### Type/Length
* 2 bytes
* represents type or length of encapsulated packet
* if the value is 1500 or less, it is measuring length
* A value of 1536 indicates the TYPE of the encapsulated packet, and the length is determined other ways
* 0x0800 is IPV4 in hexidecimal, or 2048, more than 1500
* 0x86DD is IPV6

### lengths in bytes
* Preamble: 7
* SFD: 1
* Destination: 6
* Source: 6
* Type: 2

### FCS (trailer)
* Frame checker sequence
* 4 bytes
* detects corrupted data by running a CRC algorithm over data
* Cyclic redundancy check 

header + trailer = 26 bytes

### Mac Addresses
* 6 byte physical address assignbed to device when made
* media access control addresses
* AKA BIA, burned in address
* Globally unique, no two devices have the same mac address, ideally
* First 3 bytes are the OUI, organizationally unique identifier. Assigned to company. 
* Cisco might have a set of OUIs only they can use
* THe last 3 bytes are unique to the device itself
* written as 12 hexidecimal characters
* 48 bits length

The first half of the address identifies the manufacturer, the second half identifies the device

* unicast frame: frame destined for a single destination
* after a switch receives the frame, it looks at the source address to learn where the PC is, and adds the MAC address to the mac-address-table. This is dynamic mac addressing, it learns mac addresses as they pass through.
* This is how switches and routers learn where devices are in a network
* But what if thde destination isnt in the mac-address-table yet? Because the switch doesnt know where the frame is going, it sends it to everyone on all of its interfaces, except the source mac address. This is an unknown unicast frame. Any PC that have non-matching mac addresses to the one in the frame ignore the frame. THIS IS CALLED FLOODING. 
* Flood: send to all devices on network if router or wswitch doesnt have destination mac address in table. 
* ONLY WHEN A DEVICE SENDS A FRAME TO SOMEONE ELSE WILL ITS MAC BE ADDED TO THE ADDRESS TABLE
* MAC addresses are usually removed from the table after some time of inactivity, 5 minutes in the case of cisco, in which case flooding is repeated when the MAC expires
* interface refers to one connection by a switch or router to a client. If a client is at address suffix .0001 and interface F0/1, that means it is connected on connection 1. Interface is wherever it immediately received the frame from, mac address is wherever the frame comes from originally
* If a switch sends an unknown unicast frame to another switch, the destination switch will input the mac address on the interface of the source switch, because it must go through the source switch to get to the source client

### Ethernet Frame
preamble and SFD are usually not ocnsidered part of the ethernet header. Thus the header is comprised of destination source type and fcs. Thus the header + trailer size is 18 bytes. 
* the minimum size of a frame is 64 bytes including the packet. The minimum payload size is 46 bytes. 
* If the payload is less than 46 bytes, padding 0's are added to make it 46 bytes

* In addition to MAC addresses, IP addresses are necessary for LANs to function
* each network has an all encompassing IP, like 192.168.1.0/24
* A PC on that network, as such would be 192.168.1.1, 192.168.1.2, etc
* Encapsulated in the frame is an IP packet, which contains a source and destination IP address
* to send data to another computer you must know its mac address. PC1, for instance, however, needs to find another computer's mac address using the IP
* MAC addresses must be used because switches are layer 2 devices. MAC addresses are layer 2, IP addresses are layer 1
* To find other mac addresses, client use ARP

### ARP
* Address resolution Protocol
* used to discover the layer 2 mac address of a known layer 3 address
* consists of 2 messages: the ARP request and the ARP reply
* ARP request is sent to find the mac address
* ARP reply is used to inform requesting device of mac address
* ARP request is sent as a broadcast ethernet frame, sent to all hosts in a network. The requester sends the data out to all devices through the switch or modem, and waits for a reply
* ARP reply is unicast, only sent to the host that made the request 
* to establish a connection, first the ARP request frame must be sent. Comprises of source and destination IP, source mac, and destination mac of FFFF.FFFF.FFFF. That is the broadcast destination  
* any client that receives an ip not matching its own drops the frame
* switches treat the arp frame much the same as unknown unicast frame. This is because the arp request does not contain a destination mac address. Since on the way bac, the desination mac is already entered in the mac tables of the network switch, there is no need for a flood, and the frame is instead forwarded as it is unicast.
* when the arp reply is received, the combined mac address and ip address of the target client is added to the ARP table. This can be accessed using arp -a. Static entries were not learned. Dynamic entries were learned by sending arp requests
* GNS is a good networking simulation tool to visualize this, and uses virtualized cisco machines to display network layouts and operations

### Ping
* network utility used to test reachability. Can 2 computers reach each other?
* Measures time for rount trip of a ping requests
* ping uses ICMP echo request and ICMP echo reply
* Similar to an ARP request, but it is broadcast directly with a unicast frame.
* Thus, to ping, you need to know the mac address of the target PC in the ARP-tables
* the command to ping is ping (ip-address) size (# of bytes per ping). If the size of the data in the packet is less than 46 bytes, it will add padding
* usually sends 5 100 byte ICMP requests. 5 ICMP replies should be received. ! indicates success, . indicates failed ping. Success rate represent how many requests received replies.
* If a mac address isnt in the ip tables, the first ping will always fail, because ARP must find the destination mac address. In the time of the ARP request and reply, the ping fails. All subsequent pings succeed however.
  
#### Cisco commands
* in cisco CLI, the equivalent of windows `arp -a` `show arp`. To see the mac-address-table of a cisco device, use `show mac-address-table`
* wireshark is a good way to inspect these procedures

### mac-address-table
* includes
  * vlan
  * mac addresses
  * type (dynamic or static)
  * ports/interfaces
* accessed via `show mac-address-table`

* mac addresses age, after about 5 minutes they are automatically removed to save space
* to clear mac-address-table of dynamic addresses, use `clear mac-address-table dynamic`
* to clear specific address, do ` clear mac-address-table dynamic address {mac address}`
* to remove by interface, do `clear mac-address-table dynamic interface (interface)`

## IPV4 Addressing
* forwarding frames between LANs through routers.
* this happens at layer 3, the network layer. Provides connectivity between hosts on different networks.
*  Provides logical addressing, IP addesses. THat is they are assigned during config
*  provdes path selection between source and destination
*  routers operate at layer 3

### Example
* take 2 networks connected through a router, at 192.168.1.0/24, and 192.168.2.0/24
* notice that the first 3 groups of numbers represent the network, the last set of numbers represent the clients
* each router needs its own IP address as well

* broadcast frames are limited to local networks. Routers will not forward frames in broadcast mode

### IPV4 Format
* comprises of a header (later)
* Contains source IP address and destination IP address. 
* IP addresses are 32 Bits in length, or 4 bytes
* thus each group of numbers represents 8 bits
* xxx.xxx.x.xxx is dotted decimal form
* however, ipv4 addresses are sent in binary over the network layer
* thus, an ipv4 address is really 32 bits, divided into octets, and then converted to decimal form

### /24
* what does the /24 mean?
* it means the first 24 bits of the IP address represent the network portion of the address, and the remaining 8 represent the end hosts
* IP addresses on the same network have the same network section of the IP address
* if it was /16, the first 16 bits only would represent the network. That means half of the address is dedicated to identifying hosts\

### IPV4 classes
Every IPV4 address has a class, determined by the first octet of the address. This refers to the binary octet. 

CLASS          FIRST OCTET      NUMERIC RANGE     PREFIX LENGTH      # hosts uysable
A              0xxxxxxx         1-126             /8                 16777214  2^(32-8) - 2
B              10xxxxxx         128-191           /16                65534  2^(32-16) - 2
C              110xxxxx         192-223           /24                253  2^(32-24) - 2
D              1110xxxx         224-239 # reserved for multicast addressing. Separated from unicast and broadcas
E              1111xxxx         240-255 # reserved for experiments

in Class A, 127 is reserved for loopback addresses. That is why the 127 is not included. 0 is also not included
Class D is reserved for multicast addressing. Separate from unicast and broadcast 
Class E is reserved for experimentation

* becase they determine the prefix length, it determines how many hosts can possibly be on a network
* The LAST address of a network is the broadcast address and cant be assigned. 254 is the broadcast address of class C for example

### netmasks
* netmasks are an alternative way of displaying ipv4 prefixes, instead of the / system
* uses the dotted decimal form

255.0.0.0 = /8
255.255.0.0 = /16
255.255.255.0 = /24

* anywhere there is a 0 is a host octet
* anywhere there is a 255 is a network octet

### Network and broadcast addresses
* network address
  * if the host portion of the address is all 0's it is the network address, the identifier for the network itself
    * when configuring  astatic route, this is the destination IP
  * network address is the first address of the entwork, but the first usable address is 255.255.255.1, in the case of a /24 network
* broadcast address
  * if the host portion of the address is all 1's (in binary) it is the broadcast address
  * broadcast address cannot be assigned to a host
  * for example, .255 in a /24 network
  * thus if a frame has a destination ip of 192.168.1.255, it will have unknown mac address destination because it is a broadcast frame
  
### Maximum hosts per network
Maximum hosts per network = 2^(# of bytes assigned to hosts in ipv4) - 2

add 1 to the network address and you get the first usable address. Subtract 1 from the broadcast address and you get the last usable address

### configuring IP on cisco devices
#### show all ip addresses
* from priveleged exec mode:
* `show ip interface brief`
* displays the ip address for each interface. If unassigned, you can assign it manually
* method indicates how the host was assigned an ip address
* status is the layer 1 status of the interface. Is there a cable connected?. Administratively down means it was disabled with the shutdown command. Cisco router interfaces are admin down by default
* Cisco switches do not behave the same. 
* the protocol field shows the layer 2 status of the interface

#### Set IPV4 Address
* enter configure terminal mode
* `interface (ethernet type, like gigabitethernet) (interface #, like 0/0)`. This enters interface config mode for a specified interface
* to change the address, enter `ip address (desired ip address) (subnet mask)`
* then enter `no shutdown` to activate the interface 
* when you set an ipv4 address of an interface through a router, it refers to the address of that LAN, not to the address of the router which is the first possible IP address of the network. Hosts adopt the IP address of the LAN they are connected to. You assign an IP to an interface connected to a switch so that other lans can connect and send data to that lan
* if a computer wants to interface with a router through a switch, it will do so using the interface IP

#### more show commands
* `show interfaces (interface) `shows all interface information
* `show interfaces description` shows interface descriptions which can be manually be configured. Good for organization
* to configure an interface description, enter the interface config terminal. Then run: `description ## (description) ##`

note you can manually set ip addresses for pc's in packet tracer it he config menu

## Switch Interfaces
### interfacing
1. enable priveleged exec
2. `show ip interface brief`
3. Switches do not have shutdown command applied by default. When you connect a device, they will be up up by default (status and protocol up)
4. Switches do not have assigned IPs because they are layer 2 devices. 
5. down down just means no connection. Routers are down by default, switches are not

### interface status
1. `show interfaces status`
2. contains port (interface)
3. name of interface (description)
4. status: shows whether interface is connected
5. vlan: Vlans are for dividing lans into smaller lans. Default is 1. Trunks are connected to other switches
6. duplex: Are the devices capable of sending and receiving data at the same time? Default is auto. Full duplex means they can
7. speed: shows speed of ethernet interface. Remember, in megabits. Auto means they negotiate speed based on fastest speed between devices for connection
8. type: shows type of interface. 10/100BaseTX for instance
   
autonegotiation usually works, but good idea to know manual configuration

### configuring speed and duplex
* enter interface configuration `interface (ethernet type) (interface number)`
* `speed (# speed based on network capability / auto for auto selection)` to change speed
* `duplex (auto/full/half)` to change duplex status
* `description ## (description) ##`
* any value that is autonegotiated will have a-(value)
* all of these commands also work on routers

however, it is a security risk to config each individually, so you can configure all of them in groups with range interfacing

* `interface range (interface speed) (interface start index) - (interface end index)`
* any configuration commands made now will apply to all selected interfaces
* if you want to specify several different ranges, you just do:
* `interface range (interface speed) (interface start index) - (interface end index), (interface speed) (interface start index) - (interface end index)`

### Full and half duplex
#### Half duplex
can only send or receive one at a time
#### Full duplex
Can send or receive one at a time. No waiting time 

* in old systems, lans were called collision domains, with half duplex capable hubs instead of switches to connect several hosts
* However, because they were half duplex, if 2 packets were ever going in the same direction to the same host, they collided and were destroyed
* This was solved with CSMACD, carrier sense multiple access with collision detection. Before sending frames, devices listen to the collision domain until they detect no other devices sending
* if collision did occur, devices sent jamming signal to inform the other devices that a collision happened, after which each device will wait a random time period before sending data again. The process then repeats.
* that process works, but kind of sucks and is very slow
* although collisions still do occur they are usually isolated errors due to bad setup. 
* In a switch based network each host is part of its own collision domain

### speed/duplex autonegotiation
* interfaces on routers and switches have speeds and duplex settings are automatic by default
* interfaces advertise their capabilkities to neighboring devices and negotiate the best speed and duplex settings they are both capable of handling
* If a gigabit ethernet interface with 1000 megabit capability on a switch is connected to a host capable of only fast ethernet interfaces, at 100 megabit capacity, the switch and host will autonegotiate for 100 megabit speed

#### what if autonegotiation is disabled on the device connected to the switch?
1. Switch will try to sense the speed the other device is operating at. 
2. If it cannot detect the speed it will default to minimum speed
3. if the speed is 10 or 100 megabits, it will default to half duplex. Otherwise full duplex
4. if the switch sets to half duplex on a host that is in fact full duplex, this is a DUPLEX MISMATCH. This will result in collisions occurring and poor network performance. 
5. Just use autonegotiation

### Interface errors
* `show interfaces (speed and interface)`
* shows some statistics at the botton of the data output. 
* You can see total packets received, and total bytes
* runts: smaller than minimum ethernet frame size, 64 bytes
* giants: frames bigger than max frame size at 1518 bytes
* CRC: frames that failed the CRC check (in ethernet FCS trailer)
* FrameL frames that have illegal or incorrect format
* input errors: total of various counters
* output errors: total frams the switch tried to send but failed due to an error

## IPV4 Header
This focuses on the layer 3 header. Thus the focus is on the packets

### parts of header
1. version: length 4 bits. Identifies the IP version, ipv4/ipv6 0100/0110 respecitvely
2. IHL: internet header length, 4 bits long. Final field of the ipv4 header (options) is variable in length so this field is necessary to show how long options is. Specifies the length of the header in 4 byte increments. If it says the length is 5, that means it is 5 * 4 bytes, or 20 bytes. The minimum length of an IPV4 header is 20 bytes or 5. Thus the minimum length of an ipv4 header is one with no options enabled. Maximum value is 15 * 4 bytes, 60 bytes, or size 15.
3. DSCP: Differentiated services code point: 6 bits. used for QoS, quality of service. PRioritize delay sensitive data, such as voice or video. Which traffic needs priority treatment
4. ECN: Explicit Conjestion Notification. 2 bits. End to end conjestion notification without dropping packets. Usually, when there is conjestion packets drop. Signifies conjestion without the drop. Requires both endpoints to support in order to function however.
5. Total length: 16 bits, 4 bytes. Total length of packet, l3 header + l4 segment. measures length in bytes instead of 4 byte increments. minimum value of 20, ipv4 header with no encapsulated data. Max value of 65635
6. identification: 16 bits. if a packet is fragmented due to being too large, it is used to identify which parent packet the fragment belongs to. All fragments have the same ipv4 header so they can be reassembled. Packets are fragmented if larger than the MTU, maximum transmission unit, 1500 bytes, same as maximum size of ethernet frame. Fragments reassembled by host
7. Flags: 3 bits: control and identify fragments. Bit 0: reserved, always 0. Bit 1, dont fragment, used to indicate packet that hsouldnt be fragmented. bit 2: more fragments bit. Set to 0 if the last fragment, set to 1 if there are more packets
8. fragmet offset: 13 bits: used to indicate position of fragment inside the original IP packet. Allow fragmented packets to be rassembled even if the fragments arrive out of order
9.  time to live: 8 bits. A router drops  apacket with 0 ttl. Used to prevent infinite loops. If a packet keeps getting sent around due to bad configuration, it causes congestion. This is a hop count. Each time the packet arrives at a router, it adds 1 to the ttl, until it reaches destination or runs out of ttl. Default is 64. 
10. Protocol: 8 bits, indicates the protocol of the layer 4 PDU. Value 6 for TCP. Value of 17 for UDP. Value 1 for ICMP. Value 89 for OSPF (open shortest path first).
11. Header Checksum: 16 bits, calculated chesum to check for errors in the header. When router receives packet, it calculates checksum of header and compares itto the one in the header. if they do not match, the router drops the packet. used to check for errors ONLy in the header. Data checksum is usually delegated to the TCP and UDP
12. Source/destination ip address fields: 32 bits each, since that is lenght of ipv4 address. Source IP, address of sender. Destination, IPV4 address of receiver
13. Options: 0-320 bits. If IHL is greater than 5, optins are present. Allows for more interfacing for special cases
    
Remember, an IP packet is enclosed in a layer 2 (ethernet maybe) protocol as well. Thus, it would also include the ethernet header and trailer

## static Routing 
WAN: a network spread over a large area

Every router interface has its own IP address to be accessed from the network it connects to

### routing
a host will ask these questions:
1. is the destination ip address in the same LAN as me?
2. if it is, you can forward directly to the client
3. if it is not in the same LAN, forward to the default gateway, the device the host forwards data destined for another network to. Routers are usually the gateway, through the interface IP
   1. default gateway is denoted by 0.0.0.0/0. It is usually mapped to another IP address in the network, the router, which is discovered using DHCP, mostly 
4. now the router has the packet, and it will compare the destination IP to the routing table. Each router has a routing table that stores a list of destinations and routes to those destinations. 
5. if it is already in the routing table, it will send the packet via an interface directly to the router, and via any hops in between the source and destination networks. 
6. The source router forwards the packet to the next router in the route. That router follows the same process as the first router, checks its IP table, and forwards to the next hop in the route. 

at each stage, the router compares the destination IP to its routing table, and ecides whether it needs a hop, or can directly connect to the destination IP network.

### what is the /32?
a /32 mask represents a single specific host on a network, like a PC. A pc on network 192.168.0.0/24 would have an IP of 192.168.0.54/32, but usually we just say 192.168.0.54.

To reiterate, local route is the actual IP address of the interface, and the connected route is the IP the network the interface is a member of

The ip address configured on a router interface will appear as a local route, /32. The IP address you assign the router is relative to the LAN, and thus is local. That is how clients will access the router?
### Managing routes with cisco systems
1. `show ip route` shows the ip routing table. L stands for local network, and C stands for connected network.  
2. if an address like 192.168.1.2 is a destination for a packet, and 192.168.1.0/24, the source router knows where to route because the network portions are the same
3. connected route: network the interface is connected to 
4. local route: the actual IP address on the interface
5. when you configure an IP, its connected and local routes are created

#### Configure gateway of last resort
1. to configure a gaeway of last resort you must configure a default route, which matches all possible destinations. It is used only if a more specific route match isnt found in the routing table. The default route is the least specifric route possible
2. it is used only if a more specifric (lan based) route is not found
3. the default route is the least specific possible, IP address of 0.0.0.0/0 and mask of 0.0.0.0. THis is what we should set the gateway of last resort. This is the range of all possible addresses
   
* this is because 0.0.0.0/0 has no network octets. All octets are variable. All btis are not fixed.

##### so how do we configure the static route?
* local and connected routes are automatic. 
* to configure a route, `ip route (destination-address) (mask) (next hop)`. I give this packet to you, you deal with the route. Usually the destination address is the network address, for instance, 192.168.1.0, where subnet mask is 255.255.255.0
* `ip route 0.0.0.0 0.0.0.0 (router interface IP address)` to configure default gateway. Represented by * in routing table
* the next hop will figure out how to get the packet where it needs to go
* ROUTERS WILL DROP PACKETS WITH UNKNOWN DESTINATIONS. THEY WILL NEVER FLOOD
* unless we configure our routes (or do dynamic routing, later), we cannot send packets to unknown destinations, eg dstinations not in the routing table
* How do we get around this? This command: `ip route (destination IP) (mask) (exit-interface)`. Instead of next hop we specify exit interface. where should we send packets as a route of last resort? to whatever is at the end of the interface. Gateway of last resort is not added however, because this is for specifric networks. But what does this mean? it is technically a direct connection to the destination IP. It is basically saying, "I will give this packet to whatever is connected on this interface, and they will route it where it needs to go". And so, when the packet gets to the router on the connected interface, its own routing will carry out the rest of the work.
  * appears as direct connection in routing table
* `via` usually refers to interface. Get to network IP via interface IP

there might be a problem however, one way reachability. Source can send packets, but without more static routing, the destination cannot send a reply. 

what does it mean when a router looks for most specific matching route. It looks for the destination with longest prefix length.  

in short, if a router can route to 192.168.4.254 through either 192.0.0.0/8 or 192.168.4/24, it will do soi through the latter, because it is more specific (more network octets)

at every stage of the routing process, a new ethernet frame with a new src mac address is added. IP header, however, remains unchanged
 
THIS IS VERY IMPORTANT FOR CCNA TEST

remember, you can use scapy for manual packet crafting

## Subnetting
huge topic for ccna, and network engineering

### CIDR Classification
Dynamic, instdead of static IP class ranged.
* previously we had a b c d and e class IP addresses.
* We are doing away with that, in favor of CIDR
* With the older, static ip classification system, how does an organization get an assigned IP? the IANA internet assigned numbers authority helps out. Assigns ipv4 addresses to companies based on size
* for example, very large company might receive a class A or class b network, while a small company might receive a class C network
* this was wasteful, so new methods are available. Even point to point networks, that include 2 nodes need their own network IP address, which means lots of addresses in that network range go unused. 2 nodes with their own IP, you waste 252 addresses
* take company x, which needs 5000 end hosts. Problem? Class C network doesnt provide enough addresses, so class B network must be assigned. 60000 addresses are wasted
* there are manby more examples. Total ipv4 address space is 4 billion. This seemed like a lot, but creators did not predict the size of the internet
* The IETF (internet engineering task forc) introduced CIDR
  
#### With CIDR...
* class A /8, Class B/16, class C/24 requriements were removed
* thus larger networks could be split into smaller networks, subnetworks, or subnets
* with CIDR, we can say a network has a /25 or /30 network portion of the address, so that we dont use so much address space per network

say we have a network of netmask 255.255.255.0

in binary, that is

11111111.11111111.11111111.00000000

if we want to use cidr, and have the network portion be 25 bits, we just do this to the netmask

11111111.11111111.11111111.10000000

the new netmask in dotted decimal is 255.255.255.128

since there are now only 7 bits in the host portion of the address, the number of usable addresses according to the 2^n - 2 formula is 126

for instance, a /30 network has only 2 usable host addresses

the remaining addresses in the address block are available to be used in other subnets! we can break down large networks into smaller ones.

#### More efficient?
* a .254 address has 0 usable host addresses. Used to be impossible to use, however for a point to point network, you can do this!
* it contains only the network address and the broadcast addresses. 
* when there is just a connection between two addresses, however, there is just a point to point connection, the broadcast and network addresses are dropped, and the two remaining addresses become host addredsses
* /31 masks are more efficient for p2p connections

#### what of the /32 mask?
* -1 usable addresses?
* probably you will never use these. What if you cant to create a static route to a single host however?
* a /32 mask can be used to identify a static host IP address

### Chart of CIDR notation subnet masks
Dotted Decimal          CIDR Notation   Subnets     num hosts     num borrowed bits
255.255.255.128         /25             1           126           1
255.255.255.192         /26             4           62            2
255.255.255.224         /27             8           30            3
255.255.255.240         /28             16          14            4
255.255.255.248         /29             32          6             5
255.255.255.252         /30             64          2             6
255.255.255.254         /31             128         0(2)          7
255.255.255.255         /32             254         0(1)          8

we will also look at subnetting for class b and a addresses

number of subnets = 2^x
x = number of borrowed bits, bits of the last octet assigned to the subnet address

remember when configuring subnets, the lowest address in the network is the network address. The highest address is the broadcast address. THese are not usable as addresses

### Subnetting trick:

the last octet of a /26 address can be represented as such:

NET  Host
00 | 000000
the value of the last bit in the network portion of the octet is 64. So to find the next subnet's network address, just add 64.

Thus the network addresses of the subnets on this octet are 0, 64, 128, and 192

the same process can be used for class A and B networks

### VLSM
variable length subnet masks

so far we have used fixed length subnet masks. This means that all subnets use the same prefix length

* VLSM is the proces of creating subnets of different sizes to make your use of netwiork addresses more efficient
* we can assign different subnet sizes to different lans, to maximize space efficiency
* VLSM steps

1. assign the largest subnet at the start of the address space
2. assign the second largest subnet after it
3. repeat process until all subnets have been assigned

remember, wehn subnetting the binary form of the address is much more important than the decimal form 

## VLANs
extremely important

### What is a lan?
* LAN is local area network
* group of devices all connected in a location
* A LAN is a single broadcast domain including all devices in that broadcast domain
* a broadcast domain is the group of devices which receive a braodcast frame of the broadcast mac address sent by any one of lan members
* usually broadcast domains are contained in the interface of a router
* broadcast domains also exist in p2p networks, with only 2 clients.

So what is a VLAN???

* what if you want to break up a broadcast domain into several smaller broadcast domains?
* if we od this, we can limit access to different segments of that broadcast domain to improve security
lots of unecessary broadcast traffic also reduces network performance

this can all be done with subnets, so where do VLANs come in?

* subnets each require their own router interface. Thus, for every subnet, we need an additional connection to the router.
That means that if we try to send a message from one subnet to another, it goes through the network switch, into the router interface, out another interface, and to the desired subnet

but what if we send a broadcast frame? The switch still broadcasts it on all interfaces. A switch is only aware of layer 2 information, and doesnt care about the subnets. The subnets are not seperated at layer 2, the broadcast domain.

One option is to buy a switch for every department. Thats expensive and inefficient

we can use vlans to seperate subnets at layer 2

### How do we assign VLANs?
switch interfaces

1. configure switch interface to a vlan
2. each vlan will be considered a separate lan, and so traffic will not be forwarded between them
3. if a broadcast packet comes from vlan10, it will only broadcast to vlan10 
4. the router performs all inter vlan routing. The router still needs one interface for vlan/subnet
5. if a frame is destined for another vlan, it goes to the default gateway first

so: vlans seperate hosts at layer 2

they are configured on a per interface basis

switches do not forward traffic directly between hosts in different vlans

### VLAN configuration
remember, vlans are configured by interface
the 5 default cisco vlans are 1, 1002, 1003, 1004, 1005
vlan 0 and 4095 are reserved, not possible to use!

process:
to see vlan configs, do `show vlan`
1. show vlan brief, shows vlans and their interfaces
2. `interface range g1/0,g2/0(example)` to enter configuration to configure several interfaces at once
3. then run command `switchport mode access` to set the interface as an access port. This means that it belongs to a single vlan, and connects to end hosts. This is as opposed to a trunk port, which carries multiple vlans. Good to explicitly specify port type
4. then run `switchport access vlan (vlan number)`. if the select vlan doesnt exzist, it will create the vlan
5. You can also change the default name of a vlan
6. `vlan (vlan number)` accesses a vlan. You can then do `name (name)`. will create vlan if the vlan number doesnt exist

remember, there are 5 default vlans in each switch that cant be deleted

There is still much more needed to use vlans effectively, however

if you have two switches which have some shared VLANs, the inter switch vlan connection needs a cable for each interface

on smaller networks, using a separate interface for each vlan is possible. However, as networks scale up and number of VLANs also increases, this is impractical

you can use trunk ports to operate several vlans on one interface

### Trunk Ports
* a trunk port allows for multiple vlan's traffic to travel over an interface. Good for communicating with a router, or between switches using vlans
* how does the switch or router knows which vlan a packet is part of?
* switches will tag all frames they send over a trunk link. This allows the receiving switch to know which vlan the frame belongs to
* trunk ports = tagged ports
* access ports = untagged ports

### Vlan tags
2 main types:
* ISL: old cisco proprietary protocol
* IEEE 802.1Q INdustry standard protocol
* 802.1Q is inserted between the source mac address and type/length field of the ethernet frame header.
* the tag is 4 bytes, or 32 bits in length
* the tag consists of the tag protocol identifier, and the tag control information, TPID and TCI
* TCI consists of 3 sub fields: PCP, DEI, and VID
* TPID Field: 2 bytes, always set to 0x8100, indicates that the frame was 802.1Q-tagged
* PCP, priority code point, 3 bits in length, class of service which prioritizes important traffic in congested networks
* DEI: drop eligible indicator. If network is congested, can this frame be dropped?
* VID: VLAN ID: 12 bits, identifies VLAN the frame belongs to. because this is 12 bits, there can be a total of 4096 vlan. the first and last vlans are reserved, thus the range is 1-4094
* anything past 1006 on the vlan list is an extended vlan, some older devices cant use the extended vlan list

### Native VLAN
* only a feature of 802.1Q
* VLAN 1 by default on all truk ports, however this can be manually configured on each trunk port
* The switch does not add an 802.1Q tag to frames in the native vlan
* when a switch receives an untagged frame on a trunk port it assumes the frame belongs to the native VLAN. Very important the native VLAN matches
* basically, it sets a default vlan. If this frame does not have a VLAN id, by default you should send it to this vlan. 
* when vlan mismatching, the frame isnt forwarded because the target doesnt exist in the desired vlan
* if a switch receives a frame that is tagged for the native vlan, it is dropped, since native vlan frames should not have a VID attached

### configuration
1. enter interface mode
2. `switchport mode trunk`
3. if you get a trunk encapsulation error, you must first set encapsulation to 802.1Q to manually change encapsulation type
4. `switchport trunk encapsulation dot1q`, to set 802.1Q
5. `switchport mode trunk` (to set the mode to trunk)
6. `show interfaces trunk` to see trunk interfaces that are trunked
7. `switchport trunk allowed vlan 10,30` (tells the switch what vlans to trunk)
   `switchport trunk allowed vlan add 20` (add a vlan to the list of allowed trunk vlans)
8. `switchport trunk allowed vlan all` to allow all vlans
9.  `switchport trunk allowed vlan except 10` (all vlans except this one)
11. `switchport trunk allowed vlan none` (no vlans allowed)
12. for security purposes it is best to change the native vlan to an unused vlan. This must match between switches
13. `switchport trunk native vlan 1001`
14. remember, to make a vlan a native vlan, you must create it first

### Router on a stick ROAS
* what is this? A new method of inter-vlan routing
* only one interface connected to the network router for all vlans
* one physical interface to function as multiple. WE are basically making sub interfaces
* first, enable interface with no shutdown
* `interface g0/0.(vlan number)`
* `encapsulation dot1q (vlan number)`
* `ip address (sub-net sub-interface address) (netmask)`
* remember, this needs trunk port on the connected switch, which trunks all vlans

### Using native vlan on a router
#### 2 methods
1. `encapsulation dot1q (vlan-id) native`, tells the router this is a native vlan, assume untagged frames belong to native vlan. Then assign ip address to the subinterface
2. dont use a subinterface, just use the physical interface for the native vlan

### Multilayer switch
* a multilayer switch can operate at layer 3, the ip layer. the symbol looks like the sun, with arrows pointing out
* multilayer switch can route and switch
* you can configure routed ports which act like router interfaces
* you can create virtual interfaces for each vlan and assign ip addresses to those interfaces
* you can configure routes
* can be used for inter-vlan routing
* SVI: switch virtual interface, virtual interfaces you can assign IPs to in a multilayer switch. Configure each pc to use the SVI not the router as gateway
* to send traffic to diffrerent subnets, send frames to the multilayer switch.
* we can also configure physical ports on the multilayer switch to have IPs, and configure a static route. Thus, we can redirect extra-lan bound traffic to the router, and the internet

### Configuring multilayer switch
#### Router side
* `do show run` to show sub interfaces, and then `do show ip interface brief`
* get rid of all router subinterfaces using `no interface (interface).(subinterface)`
* then do `default interface (interface)` to specify default routing interface
* then enter interface configuration mode, and set the ip for the p2p connectio between the multilayer switch and router. The subnet mask should be 255.255.255.252
* multilayer switches do not work with ROAS
#### Switch side
* enbable default interface to the router using default interface (interface connected to router)
* enable ip routing using `ip routing` which allows to build IP table. without this intervlan routing wont work
* enter selected interface
* then in the interface, run `no switchport`, so that the port becomes a layer 3 routed port
* configure the ip address as you would on any router to correspond with the p2p connection
* then on the switch, set the default route, `ip route 0.0.0.0 0.0.0.0 (router ip)`
* thyen do `show interfaces status`, in order to check the interface works

### SVI config
* on the switch
* `interface vlan (vlan number)`
* assign ip address to the vlan like normal, `ip adddress x.x.x.x subnetmask`
* then run `no shutdown` to enable the interface
#### conditions to work
* vlan must be created first, it must exist on switch. Switch doesnt automatically create vlan when you make an svi for it
* the switch must have at least one access port in the vlan in an up up state and or one trunk port that allows the vlan that is in an up up state
* the vlan must not be shutdown. You cannot use the shutdown command to disable vlans
* SVI must not be shutdown
* remember to use no shutdown after creation!

## DTP and VTP 
#### what are these?
* DTP: Dynamic Trunking Protocol
* VTP: VLAN trunking protocol

### DTP
* Cisco proprietary protocol used to allow sswitches to dynbamicaly determine their interface status without manual config
* DTP is enabled by default on all cisco switch interfaces
* so far we have been using mnaual switchport configuration
* however, for security, manual configuration is recommended, since DTP can be exploited by attackers
* to enable dtp, do `switchport mode dynamic auto/desireable` when in interface config mode
* In dynamic desireable mode will actively try to form a trunk with other cisco switches. It will form a trunk if connected to another switchport when it is in trunk mode, or dynamic desireable/auto mode. This is DTP negotiation. It will do its best to form a trunk, unless the other switch interface is in access mode, in which case it will autonegotiate to access
* `show interfaces (interface) switchport` shows the settings for a selected interface switchport
* in dynamic auyto mode, it will not actively try to form a trunk with other switches. However, it will form a trunk if the connected switch port is in trunk mode, or is seeking actively to form a trunk connectiuon. If it encounters another auto mode, it will form an access connection.
* if there is a mode mismatch, the traffic will nto flow
* dtp will not trunk with a router or pc. Trunks for ROAS must be manually configured
* to disable autonegotiation, you can say `switchport nonegotiate`
* remember, manual configuration is always better for this!

* another feature of DTP is negotiation of encapsulation type. THis is enabled by default
* to set autonegotiation for encapsulation, run `switchport trunk encapsulation negotiate`
* DTP frames are sent in vlan1 when using isl, or in native vlan when using 802.1q
* if both cisco switches suppoort ISL, isl is preferred, so manual configuration is better
* do this with `switchport trunk encapsulation dot1q`

### VTP
* VTP allows configuration of VLANs on a central VTP server switch, whereafter other switches, VTP clients will synchronize their VLAN datrabase to the server
* designed for large networks with vlans to reduce burden of manual configuration
* not recommended to use, rarely used
* 3 versions, 1 2 and 3
* most modern cisco switches support all 3
* 3 vtp modes, server, client, and transparent
* switches operate in server mode by default
* vtp servers: add modify and delete vlans. Store vlan database in non volatile ram, nvram, so changes save when shutdown. Increase revision number every time vlan database changed. will advertise latest version of vlan database on the trunk interfacesm, and the vtp clients will synchronize to it
* VTP servers also function as VTP clients. VTP servers will synchronize to other VTP servers with a higher revision number
* VTP clients: cannot add modify or delete vlans. do not store vlan database, except in vtpv3. Synchronize their vlan database to the sergver with the highest number in their vtp dfomain
* advertize their vlan databse and forward vtp advertisements to other clients over the trunk ports
* to change mode, do vtp mode (server/client/transparent)

### How does this work?
* show vtp status to show vtp information. by default switches run vtp version 1.
* If we want to synchronize switches in VTP, we must put them all under same vtp domain name
* to change vtp domain name, do `vtp domain (name)`
* if vtp switch with null domain receives advertisement, it automatically joins that domain
* if a swith receives a vtp advertisement in the same vtp domain witha higher revision number, it will update its vlan database to match
* danger of VTP: If you connect an old switch with a higher revision number to your network and the vtp domain name mathes, all switches in the domain will sync their vlan databases to that switch, and destroy everything

### VTP Transparent mode
* does not participate in the vtp domain, and does not sync to the database
* maintains its own vlan database in nvram it can add, modify, delete vlans but they wont be advertised on other switches
* will forward VTP advertisements to other VTP switches, if its in the same domain

### VTP version configuration
* to change vtp version, use vtp version command
* `vtp version (1-3)`
* vtp1 v vtpv2. only major difference is that v2 has support for token ring vlans, otherwise there is no reason to use v2
* token ring is an old technology
* v3 has quite a few new features, but not that important

remember, whoever has highest revision number will push changes 
to reset revision number to 0, you can:
* change vtp domain to unused domain name
* change the switch to vtp transparent mode

## Spanning Tree Protocol, STP
extremely important

### Redundancy
* essential, nonrenduntant networks are not acceptab;le
* modern networks must run all the time. Even a short downtime can be disastrous
* if one network component fails, you must ensure that other component will take over with little or no downtime
* as much as possible you must implememtn redundancy to remain resilient to failure
* you should reduce the danger of POF, points of failure. Chokepoints in a network are not good
* unfortuantely, most PCs only have a single network interface card, NIC, so they only have one available point of failure

Spanning tree allows network redundancy, a layer 2 protocol

### danger of not using STP
#### Broadcast storms
* when you send an ARP request, it is a broadcast frame. Thus, switches will broadcast this frame. If 3 switches are arranged in a triangle, as is a good idea for redundancy, flooded packets will go into an infinite loop in the triangle.
*  ethernet frames dont have a ttl field, so the frames will cycle indefinitely. Eventually the network will be clogged
*  traffic isnt the only problem, when a switch continuously receives a frame from the same source, it causes mac address flapping. The source address is continuously updated in the mac address table
*  STP is *an* answer to the problem

### What is stp?
* classis STP, IEEE 802.1D
* switches from all vendors run STP by default
* STP prevents layer 2 loops by placing redundant ports in a blocking state. This means interface is disabled., These interfaces act as backups that can enter a forwarding state if an active (currently forwarding) interface fails
* interfaces in forwarding state behave normally, they send and receive traffic
* interfaces in blocking state only send or receive STP messages, BPDUs, bridge protocol data units
* Bridges are an old intermediary technology between hub and switch, that is why stp refers to switch as bridge. BRidge and switch are interchangeable in this case
* if a link between two switches is in a blocked state, it basically doesnt exist
* basically, STP will keep an interface disabled, until another one is detected to be down, in which case the interface will go back up to support new traffic

### Deeper into stp
* by selecting which ports are forwarding and which are blocking, stp creates a single path to/from each point in the network. This prevents layer 2 loops
* There is a set process that STP uses to determine which ports should be forwarding and which should be blocking
* STP enabled switches send/receive hello BPDUs out of all interfaces every 2 seconds by default. 
* If it receives a response it knows the interface is connected to another switch
* switches send outthe hello BPDUS to learn of other switches

### BPDUs
* bridge protocol data units
* switches use the one field in the STP BPDU, bridge ID to elect a root bridge. The switch with the lowest bridge id becomes root bridge
* all ports on the root bridge are put in a forwarding state, and other switches on the topology must have a path to reach the root bridge
* traditionally, this takes 2 fields, bridge priority and source mac address
* default bridge priority is 16 bits, and set to 32768. iF all priority fields are equal, whoever has lowest mac address will become root bridge
* in modern stp however, the bridge priority field is extended to comprise of the bridge priority, and extended system id (VLAN ID) in order to support vlan operations
* why does it have a vlan ID? because cisco uses PVST, per vlan spanning tree. Each vlan has its own stp instance, so each vlan has different interfaces which can be forwarding or blocking
* the default rbidge priority is the sum of the vlan ID and the bridge priority. Thus if a switch is in vlan 1, its actual bridge value is 32769. 
* because the last 4 bits comprise the bridge priority, and the extended system id is everything up to 2048, you must increase the total bridge priority by a value of 4096 every increment if you want to change the priority without changing vlan
* valid bridge priority can be between 0 and 61440, at intervals of 4096
* the **LOWEST** bridge id is the root bridge

### Root switch
* the root switch with the lowest bridge priority will have all ports forwarding
* all root ports are designated ports
* when a switch is powered on, it assumes it is root bridge.
* It will only give up that position if it receives a superior BPDU, lower bridge ID
* once the topology has converged and all switches agree on the root bridge, only the root bridge send bpdus
* other switches in the network will forward bpdus, but not generate their own

### Steps
1. the switch with lowest id becomes root. All ports on that switch are forwarding, designated
2. each remaining switch will select one of its interfaces to be its root port, the interface with the lowest root cost will be root port. Root ports in forwarding states.
    * each speed has an stp cost. 10 MBPS has cost 100, 100 mbps 19, 1 gpbs 4, 10 gbps, 2
    * the cost on all root ports of the root bridge is 0
    * say switch 1 isthe root bridge, and all ports are 1 gbps. switch 2 will say, "I was advertised a cost of 0 on my g0/1 (connected to root bridge), my interface costs 4, total is 4". I was advertized cost of 4 on g0/0, my interface cost = 4. total cost = 8. the root port of that switch will be whichever one has the lowest cost, the one connected to the root bridge.
    * if a switch has multiple ports with the same root cost, the interface connected to neighbor with lowest bridge id wil be the root port
    * what if two switches have two connections between them? the interface connected to the lowest port id is the root port. TO identify this do `show spanning-tree`. STP port id = port priority (def 128) + port number. the NEIGHBOR switch's port id is used to identify root port in this case
3. block ports to prevent layer 2 loops
   * every collision domain has a single STP designated port. Thus on blocked connections, we need to specify the designated port. 
   * to find the designated port:
     * the switch with lowest root cost will make its port designated
     * if the root cost is the same the switch with the lowest bridge id will make its port designated  
     * the other switch will make its port non designated, or blocking

* when you have an STP path that involves intermediate connections through other switches to get to the root bridge, you add up the sum of root connections to get total cost

### STP commands 
* `show spanning-tree`, show vlan information and vlans
* `show spanning-tree vlan (vlan number)`. Root id shows data about the root, bridge id shows information about the selected bridge
* `show spanning-tree detail`, more details

### STP Port states
* blocking: stable. nn designated ports in this state
  * disabled to prevent loops
  * do not send or receive traffic on blocking state interface
  * interfaces in blocking state receive and process STP BPDUs, if they need to change to forwarding
  * do not forward these BPDUs
  * do not learn mac addresses

* Listening: transitional
  * After the blocking state, interfaces with the designated or root role enter listening state
  * only designated or root ports enter listening state
  * lasts 15 seconds by default, determined by forward delay timer
  * only forwards and receives STP BPDUs
  * does not do the same for regular traffic
  * does not learn mac addresses
* Learning: transitional
  * 15 seconds, after listening state, determined by FDT (forward delay timer)
  * same as listening, but this one learns mac addresses. Prepare for regular traffic by gathering some mac addresses
* forwarding: stable
  * pot operates as normal sends and receive BPDUs 
  * normal traffic
  * learns addresses

* listening and larning are transitional states which are passed through when an interface is activated or when a blocking port must transition toa  forwarding state due to change in network topology

### Timers
* Hello timer, 2 seconds. How often root bridge sends the hello bpdu
* forward delay, 15 seconds, how long the switch will stay in listening and learning states (each state is 15 seconds, total 30)
* max age: how long an interface will wait to changew the stp topology after ceasing to receive hello bpdus. The timer is reset every time a bpdu is received. THis is basically network failure detection. If the failure doesnt recover, stp re-evaluation, and designated/non designated ports are changed. If blockign port selected to go to forwarding, it will go from blocking to listening, then learning, and finally forwarding. Thus it can take up to 50 seconds for a blocking interface to transition to forwarding
* these times are in place to 

### STP BPDU
* uses destination mac address of 01:00:0c:cc:cc:cd for PVST+ (cisco)
* what is pvst plus? PVST only supports ISL trunk encapsulation
* PVST+ supports 802.1q encapsulation
* regular stp uses 01:80:c2:00:00:00
  
* STP BPDU
  * protocol identifier: 0x0000
  * version id: spanning tree (0)
  * bpdu type: configuration (0x00) (there are other types, but not important now)

* flags
  * signal topoligy changes
  
* Root bridge identifier
  * root bridge priority
  * root bridge system id extension 10
  * root bridge system id aa:aa:aa:aa:aa:aa
  * root path cost

* bridge identifier (currently selected switch)
  * bridge priority
  * systemid
  * system mac

* port ID: 0x8002 default
* message age
* max age
* hello time
* forward delay

### Improvements
* portfast
  * enabled on interfaces connected to end host, designated ports in forwarding state
  * when first connected, they need to do the listening and learning states
  * no risk of loops with end hosts, so why go through the entire process?
  * allows to bypass listening and learning. Must be enabled only on ports connected to end hosts. If enabled on port connection it will cause layer 2 loop
  * to enable portfast, enter the interface on the switch, and do `spanning-tree portfast`. This will only work if the port is not in trunking mode
  * portfast can cause loops if network cabling is changed
  * risk to using portfast, but there is an additional method we can use to prevent this

* BPDU Guard
  * if an interface with guard enabled receives a bpdu from a switch, the interface will shut down to prevent a loop from forming
  * to enable, enter interface, then do, `spanning-tree bpduguard enable`
  * to enable bpduguard by default on portfast, from config mode, do, `spanning-tree portfast bpduguard default`
  * to enable a port disabled by bpduguard, just do `shutdown`, then `no shutdown` to reset the interface.
  * even if it receives a superior bpdu, the port is disabled
  * this basically protects against loop from forming if portfast enabled port connects to another switch

* loop guard
  * even if the inhterface stopes receiving bpdus, it will not start forwarding, THe interface will be disabled

### Spanning tree mode
* to change spanning tree mode, do `spanning-tree mode (mst/pvst/rapid-pvst)`

### Configure root priority
* to make an arbitrary bridge the root bridge
  * `spanning-tree vlan (num) root primary/secondary`
  * this makes the selected switch have lowest priority 
* we can also have a backup root bridge
* priority configurations only apply in the vlan on which they are configured. This allows spanning tree load balancing
  * if you have several vlans, you can have a different root bridge for different vlans. Thus, different vlans will have different disables interfaces, and will leverage resources more efficiently 

### interface configuration
* to configure cost of an interface, enter the interface conig mode
* `spanning-tree vlan (num) cost (cost)` to change cost manually
* `spanning-tree vlan (num) port-priority (priority num)` to change port priority

## Rapid Spanning Tree Protocol
Old spanning tree can take up to 50 seconds to chagne topology. RSTP Responds in a few seconds. Default on most devices. CCNA only has RSTP

### Standard vs Cisco
* Standard IEEE
  * original STP
  * all VLANs share one STP instance
  * cannot load balance using classic STP
  * 802.1w, rapid spanning tree protocol
    * much faster than original standard, all vlans still share one stp instance
    * cannot load balance
  * Multiple spanning tree protocol
    * modified rstp mechanics
    * group multiple vlans into one instance to perform load balancing. Superior to cisco. Very easy to configure and manage
    * not paralleled by cisco yet
    * best for very large networks with lots of vlans, overkill for smaller networks however
* Cisco STP, PVST+, per vlan spanning tree plus
  * cisco upgrade tot eh IEEE version
  * each vlan has an STP instance
  * can load balance by blocking ports for each vlan
  * rapid pvst+
    * upgrade to 802.1w
    * each vlan has own stp instance
    * load balancing and high speeds

### RSTP
* not timer based
* improvement over 30 seconds older methods take to move a port to forwarding 
* RSTP serves same purpose as STP, elects root bridge with same rules, elects root ports with same rules, and elects designated ports with same rules as STP
* RSTP costs are expanded versions of STP

speed     RSTP COST
10 mbps   2000000
100 Mbps  200000
1 Gbps    20000
10 Gbps   2000
100 Gbps  200
1 Tbps    20

* RSTP has only a few states as well

1. Discarding: Administratively disabled, or enabled but blocking traffic
2. learning 
3. designated

root port role remains unchanged in RSTP 

non designated was split into alternate and backup port role in RSTP

### Alternate and Backup ports
* alternate
  *  discarding that receives a superior bpdu from another switch
  *  functions as backup to root port
  *  if root port fails, the switch can imediately move its best alternate port to forwarding
  *  this happens very quickly, using UplinkFast. This is automatically enabled
  *  backbonefast is another optional feature. 
     *  if a switch is disconnected from root, and has lowest ID, then it becomes the root and starts sending bpdus. This means some switches might be receiving bpdus from two or more switches. BackboneFast ensures that other switches quickly forward higher priority hellos from the old root bridge to fix the issue
  * These are all enabled by default 
* backup
  * discarding port that receives superior BPDU from anotehr interface on the same switch. Only happens when two interfaces are connected to thed same collision domain through a hub. Hubs are never used, so it isnt very useful

### Configuration commands
* spanning-tree mode rapid-pvst 

### BPDU
* protocol version 2 (rstp version)
* bpdu type 2
* uses all 8 bits of the BPDU flags
* in RSTP all switches send out BPDUs. They all send hellos every 2 seconds
* the bpdu info ages much quicker. In RSTP a switch considers a neighbor lost if it misses 3 bpdus, 6 seconds. Then it will flush, or remove all mac addresses learned on that interface

### Link Types
* RSTP distinguishes between three different link tyoes
* EDGE: a port connected to an edge host. Moves directly to forwarding without negotiation
  * works like a portfast stp port
* P2PL direct connection between two switches
* SharedL a connection to a hub

## Ether Channel
* allows to group multiple physical interfaces into a group which operates as one interface
* thsi relies on LACP, link aggregation control protocol
* a layer 3 etherhcannel is agroup of routed ports that operate as one, a layer 2 etherchannel is a group of switch ports

### Layer Switches
* access layer switch
  * end hosts connect here
* distribution layer switch
  * other switches connect here

* so what if we want to speed up a connection between an access switch and a distribution switch by adding more interfaces? that doesnt help, because STP
  * STP will select a single port interface to connect the two switches. All except one are disabled by spanning tree
  * the rest are considered as backups
  * if all of the links were enabled, it would cause a broadcast storm. This is what etherchannel can solve
  * we will have redundancy and bandwidth increase
  * we represent this by drawing a circle around grouped connections
  * these will now act as a single interface, and STP will treat them as such
  * no broadcast storm because it is a single interface
  * 4 physical interface acting as one
  * this does not mean copies of data are sent on each channel. Traffic is load balanced
  * algorithm determines which traffic uses whcih interface
* when bandwidth of the interfaces on the access switch to clients > bandwidth on distribution switch to access switch, this is oversubscription

### Load balancing
* etherchannel balances usig flows
* a flow is a communication between two nodes in the network
* in this calculation, source/destination mac, or both addresses

### configuration
* `show etherchannel load-balance`
  * this will show which method it uses to determine which physical interface is used to transmit data. 
  * src-dst-ip means it determines this using source and destination ip addresses
  * traffic that flows from one source to one destination will always flow on the same interface
  * what if there is no ip packet or ip address? use mac address
* `Port-channel load-balance src-dst-mac`
  * change the method to source and destnation mac address. more stable
* 3 methods of etherchannel configuration
  * PAgP (port aggregation protocol)
    * cisco proprietary, only cisco
    * dynamically negotiates creation and maintenance of ether channel, like dtp does for trunks
  * LACP (link aggregation control protocol)
    * Industry standard IEEE 802.3ad
    * dynamically negotiates creation and maintenance of etherchannel
    * this is on exam, but all methods should be known
  * static etherchannel
    * static configuration of etherchannel
    * etherchannel isnt dynamically formed
    * usually avoided, because you want to dynamically manipulate the etherchannel. If one interface fails, then the etherchannel will stop working when statically specified

* with etherchannel, only 8 interfaces max can be used
* to configure etherchannel:
* `interface range g0/0,g0/3`
  * `channel-group (group num) mode (mode)`
  * mode can be desirable or auto
    * mode determines how the etherchannel protocol is negotiated
    * active: enables LACP unconditionally
    * auto: enable PAgP if PAgP device is detected
    * desirable: Enable PAgP unconditionally
    * on: enable etherchannel only. Static etherchannel
    * passive: enable LAC if LACP device detected
* after you complete the port grouping, you can work on it like you would any single interface
  * `interface Port-channel (group number)` [usually something like po(num)]
  * now you can run any port commands on it, like switchport mode trunk
* interfaces in group need same configrations, like speecd and duplex

* `show etherchannel summary`

### Configuration
* load balancing
  * `show etherchannel load-balance` to see load balance method
    * src-dst-ip or src-dst-mac
  * `port channel load-balance (src-dst-mac/ip)` to change the load balance 
* etherchannel configuration
  * 3 modes, PAgP, LAcP, Static
  * `interface range (range of ports to be etherchanneled)`
  * `channel-group (group num) mode (mode)`
    * auto and desirable for PAgP
      * desirable tries to form etherchannel
      * auto only forms a channel if the other side is desirable
    * active and passive for LACP
      * respectively the same as the previous 2
    * on is for static
      * only works with on
  * `channel-protocol (static/pagp/lacp)`
    * not needed, only if you need to reconfigure the etherchannel
  * with etherchannel, all ports in the channel must have the same speed, duplex, vlans, otherwise the ports that do not match the rest will be excluded
  * `show etherchannel summary` shows all the channels
* layer 3 etherchannel
  * uses layer 3 connection vs layer 2
  * routed ports better because NO STP NEEDED AT ALL
  * routing doesnt broadcast, so there is no chance of a storm
  * `interface range (range)`
  * `no switchport`
  * `channel-group (num) mode (mode)`
  * `interface port-channel (num)`
  * configure IP address and routes
**WHENEVER YOU DO ANYTHING WITH ETHERCHANNEL, DO CONFIGURATIONS ON THE PORTS FROM THE PORT-CHANNEL INTERFACE!!!!!**
* also remember to enable routing with `ip route` on multilayer switches when they are routing to one naother
## Dynamic Routing
* in contrast to static routing. Static routing is manual configuration of routes with the ip route. 
* This involves configuring a dynamic routing protocol. Dynamic, because it isnt fixed

### Types of routes
* network route
  * to a network/subnet (mask length </32>)
  * host route: to a destination with mask length of /32

### Dynamic Routing
* when dynamic routing is enabled, the router connected to the lan address being advertised send out an advertisement, saying
* "this ip can be reached via me"
* the router advertised to will then tell its neighbors the same thing, and the route is added to the route table. 
* This continues, and the route is told to every following router

* in dynamic oruting, invalid routes are auto-removed
  * when a route is lost, it can automatically change its route to compensate
  * the dynamic routing protocol will always automatically use the fastest connection.
  * Same as STP cost

* routers can use DRP to advertise information about the routes they know to other routers
* they form adjacencies, neighborships with adjacent routers to exchange information
* if multiple routes to a destination are learned, the router determines which is superior and adds it to the routing table. It uses metric to determine which this is

### Types of DRPs
* IGP
  * interior gateway protocol
    * share routes within a single autonomous system whgich is a single organization
    * algorithm type
      * distance vector
        * routing information protocol RIP
        * Enhanced Interior Gateway ROuting Protocol EIGRP
      * link state
        * OSPF Open shortest path first (main focus of CCNA)
        * ISIS Intermediate system to intermediate system
* EGP
  * exterior gateway protocol
    * used to share routes between different autonomous systems
    * algorithm type
      * path vector
        * Border gateway protocol is the only protocol used, running on path vectors

* algorithm: process to choose the routes. All want to share route information

### Distance Vector Protocols
* invented before link state 
* ripv1 and IGRP/EIGRP are examples
* operate by sending known destination networks and metric to reach known destination networks.
* THis is routing by rumor. The router doesnt know the network beyond neighbors, because it only knows what neighbors tell it
* called distance vector because the router only knows the vector, direction, and distance, number of hops to destination

### link state routing protocol
* every router makes  aconnectivity map of the network
* to allow this, each router advertises information about its interfaces to its neighbors. These advertisements are passed along to other routers until all routers in the network develop the same network map
* every router independently uses the map to calculate the best routes to each destination
* use more CPU because more information is shared
* link state protocols tend to be faster in reacting to changes in the network than distance vector protocols

### Metric
* if a router learns 2 routes to same destination, it uses metric value to determine which to use. Low metric is the best. same as root cost. 
* if a router learns two or more routes via the same routing protocol to the same de3stination with the same metric, both will be added to the routing table and traffic will be load balanced
  *  ECMP load balancing, based on the metric, equal cost multipath.  

IGP      |    METRIC       |     Explanation                                                                                                      |
_________|_________________|______________________________________________________________________________________________________________________|
RIP          Hop Count          Each router in the path is one hop, total hops to destination, regardless of speed. Doesnt work so well
EIGRP        Bandwidth          Complex formula taking into account many things. Bandwidth of slowest link in route
OSPF         Cost               The cost of each link is calculated based on bandwidth. Total metric is total cost of each link in route
ISIS         Cost               Total metric is total cost of each route link. The cost of each link is not automatically calculated by default

* sometimes 2 routing protocols are used
* remember, different routing protocols use different metrics so they cannot be compared. For example, ospf route might have metric of 30, and an EIGRP route to the same place might have a metric of 33280. Which is better? we dont know.
* Thus, we need administrative distance to determine which route will be used
* lower AD is preferred, and indiicated the routing protocol is considered more trustworthy. 

protocol                Administrative Distance
Directly Connected      0
Static                  1
External BGP            20
EIGRP                   90
IGRP                    100
OSPF                    110
ISIS                    115
RIP                     120
EIGRP                   170
Internal BGP            200
Unusable Route          255

* lower ad number is preferred, and will be used
* you can also set a static route to have a higher ad number, by adding a number to the end of the ip-route command
* this is a floating static route, it is inactive and not in the routing table unless dynamically routed route is removed
* do show ip route
  * administrative distance/metric cost
  
## RIP and EIGRP
* RIP: Routing Information Protocol
* EIGRP: Enhanced Interior Gateway ROuting Protocol 

### RIP
* industry standard
* distance vector interior gateway
* routing by rumor logic to learn and share routes
* uses only hop count as metric, without taking into consideration bandwidth
* maximum hop count is 15, anything beyond that is considered unreachable, and any route beyond 15 will not be used in the routing table
* RIP is almost never used in large networks, but can be used in some small ones
* 3 versions
  * ripv1 and ripv2 used for ipv4
  * ripng (rip next generation) used for ipv6
* 2 message types
  * request: to ask RIP enabled neighbor routers to send their routing table
  * Response: to send the local router's routing table to neighboring routers
  * rip enabled routers will share routing table every 30 seconds.
* with so many updates, router heavy networks will get clogged

#### V1 vs V2
* RipV1
  * only supports classful addresses, doesnt support VLSM and CIDR
  * this makes it useless for modern networking, as it cannot use subnets
  * messages broadcasted to 255.255.255.255
* RipV2
  * supports vlsm and cidr
  * includes subnet mask information in advertisements
  * multicast to 224.0.0.9
* what is multicast?
  * broadcast delivered to all connections
  * multicast only received by devices included in a multicast group

### RIP configuration
1. `router rip (rip config mode)`
2. `version 2`, (to set to version 2)
3. `no auto-summary `
   * auto summary automatically converts networks to classful networks, and advertises those networks as such
   * This is bad, disable it with this command
4. `network (network ip)`
   * look for interfaces with an IP address that is in the specified range
   * active RIP on the interfaces that fall in the range 
   * form adjacencies with connected RIP neighbors
   * advertise the network prefix of the interface
   * OSPF and EIGRP operate the same
   * if we do network 10.0.0.0, it is assumed to be /8. 172.16.0.0 is assumed to be /16, etc
     * router will look for any interfaces with an IP address that matches 10.0.0.0/8
     * because /8 only needs to match first octet
     * any interface with a matching IP will be added as an adjacency
     * then it will send and receive route information on these interfaces
     * it will advertise the source interface IP address instead of the network ip given
   * if it is an interface with no rip neighbors, no new adjacencies are formed
     * afterwards that router still advertises the interface address to all RIP neighbors 
   * EVEN THOUGH THERE ARE NO NEIGHBORS, advertisements will still be sent out of this interface.
     * Thus, configure it as a passive interface
     * from rip config, do:
       * passive-interface (interface)
       * stop sending advertisements out of the specified interface, however, it will continue to advertise the interface to neighbors
       * EIGRP and OSPF both have this function as well
   * what if we want to give all of our known neighbors a route to something like the internet?
     * we have a static route to 0.0.0.0 0.0.0.0 on interface 203.0.113.0/30
     * to share this, do:
       * default-information originate
     * rip treats all routes as equal, given same num hops. Thus it load balances on all routes with equal hops
  5. do `show ip protocols`
      * shows IP protocol information 
      * shows protocols, version information, and protocol specific characteristics
      * maximum paths refers to the max number of paths used for load balancing
      * to change maximum paths, do:
        * maximum-paths (num paths)
        * in rip configuratiuon mode
      * in rip you can also see rip neighbors, and the administrative distance
      * you can change distance with:
        * distance (distance number)
        * in rip config mode

### EIGRP
* Enchanced interior gateway routing protocol
* Proprietary to cisco originally, but now published so other vendors can implement it on their equipment. Not used much outside cisco.
* Advanced hybrid DVRP
* much quicker than rip
* no hop count limit, better for large network
* send messages with multicast address 224.0.0.10
* can perform unequal cost load balancing. By default it does ECMP over 4 paths, but can be configured to do so over unequal cost routes
  * it can be configured to send more traffic over high volume interfaces, and less over lower volume interfaces, with lower speeds
* still not as widespread as OSPF

### EIGRP configuration
* `router eigrp (autonomous system number)`, enter router config mode
  * autonomous system number basically is a grouping number. All routers with the same autonomous system number for EIGRP will be able to form an adjacency and share route information 
  * thus routers that want to communicate must have the same number
* `no auto-summary`
  * same as RIP, always do this to prevent advertisement of classful advertisement
* `passive (interface)`
  * do this on any interface that has no EIGRP routers connected
  * also do this on loopbacks, because if the loopbacks are not passive, router advertisements will be sent out of them, to nobody
    * waste of resources
* `network (ip)`
  * activate EIGRP on any interface that matches the IP range
  * command assumes classful, and looks for any IPs that match its network octets 
* we can also do something like 
  * `netowrk 172.16.1.0 0.0.0.15`
  * when 172.16.1.0/28 is connected to interface g0/2
  * this will make g0/2 an EIGRP interface
  * what is 0.0.0.15??? why is it used as the subnet mask?
  * EIGRP uses a wildcard mask instead of a subnet mask

### Wildcard mask
* inverted subnet mask
* all 1s in the subnet mask are 0 in equivalent wildcard mask
* 255.255.255.0 subnet has a 0.0.0.255 wildcard
* what if we have 255.255.255.240
* inverting the bits gives us 0.0.0.15, a /28 prefix using a wildcard
* we can conclude then, that 0.0.0.15 represents a /28 subnet mask
* easy shortcut: subtract each octet in subnet mask from 255, and you will get the wildcard mask
* a 0 in the wildcard mask means that the bits must match
* a 1 means that the bits dont have to match
  
* so lets say we have the 0.0.0.15 wildcard mask
* 00000000.00000000.00000000.00001111
  * the first 28 bits are 0, so the first 28 bits must match 
  * thus, if the first 28 bits of any address on any interface of the router matches the ip given by the network command, EIGRP is enabled on that interface
  * usually best to use same prefix length as the ip address specified
* /32 wildcard mask? subnet is 255.255.255.255, thus wildcard is 0.0.0.0
* OSPF uses wildcard as well

### EIGRP continued
* `do show ip protocols`
* eigrp uses delay and bandwidth by default
* shows router ID as well to identify it within the AS, autonomous system
* Router ID is determined by:
  * manual configuration 
  * highest IP address on a loopback interface (virtual internal interface)
  * highest IP address on a physical interface
  * to change, do :
    * `eigrp router-id (ip address to set as ID)`
  * in the routing table:
    * `do show ip route`
    * EIGRP routes are indicated by D
    * RIP is indicated by R
    * metrics get very high, harder to understand

### EIGRP metric
* uses bandwidth and delay to calculate metric
* metric = bandwidth (of slowest link in path to destination) + delay(in path to destination) basically 
* this is used to calculate which route packets will take
* this is takes into account the whole route

### Terms
* feasible distance: this routes metric value to the route destination. whole route metric
* reported distance: advertised distance. neighbor's metric value to reach destination
* `show ip eigrp topology` shows all known routes by EIGRP
  * the first number in the () is the feasible distance, the second is reported
* successor: best route, lowest metric to destination
* feasible successor: alternate route, not the best, but meets feasibility condition
* feasibility condition: a route is a feasible successor if its reported distance is lower than the successor routes feasible distance
  * why? loop prevention
* unequal cost load balancing: allow load balancing even if one route has different metric from another
* `show ip protocols`
  * if eigrp maximum metric variance is 1, ECMP load balancing. No unequal cost. Load balancing only over equal metric routes
* `variance 2`
  * feasuble successor routes with a feasible distance up to 2x the size of the successor route can be used for UCLB

 
## first hop redundancy protocol FHRP
* when we have multiple connections to the internet with several routers, you can have a backup when failures occur
* what if a router is configured as a default gateway? anything destined for outside the lan will go there. If that router fails, how do clients know what the new default gateway is??
* an FHRP is desgiend to protect the network by allowing two or more routers to provide backup for that router. If an active router fails, the backup takes over.
### Function
* First hop, becase default gateway is first hop in whatever route the client is sending to.
* Both routers share a VIP, virtual IP address. You can configure the clients to use that virtual IP
* routers must negotiate their roles, so they send multicast hellos to each other
* one router is active, others are standby
  * active: working always
  * standby: failsafe, works if main fails
* if the client sends an ARP request to the VIP address? mac address of gateway necessary to send data to the internet
* the ARP request is broadcast, so it sends to all connected devices.
* Both routers in the VIP will receive the request. The active router will send the reply to the requesting client
  * each FHRP also uses a virtual mac address!

### Loopback COnfiguration
* virtual interface on router
* `interface loopback (number)`
* `ip address x.x.x.x 255.255.255.255` (usually something like 1.1.1.1)
* why? this is the default router ID if not manually configured. Used for routing
* to configure default id, `eigrp router-id (ip address)`
### Failsafe
* when standby router doesnt receive any hello, it goes to active
* since both routers shared a mac address and ip, with the VMAC and VIP, all that needs to be changes are the switch mac address tables. The clients already know where to send things
* when this happens, the standby, now active router sends gratuitous arp replies.
  * these are ARP replies sent without being requested. All switches will receive the ARP frames and update their mac address tables to forward to the now active router
* what if R1 Comes back online? it will become the standby router. The backup router wont auto give up its role. You can configure the original active router to take back the active state. This is called preemption

NOTE THAT ALL GROUP NUMBERS ARE IN HEXIDECIMAL

## OSPF
* Link State protocol
  * very different than rip and EIGRP
    * routing by rumor
  * link state:
    * routers have a complete network map
    * each router advertises interface and route information. 
    * repeated until all routers have the exact same network map
    * each route uses the map to calculate the best route
    * more resources shared, more reosurce heavy
    * faster, more efficient when responding to changes
### OSPF function
* Open Shortest Path First
* Dijkstras algorithm
* 3 versions
  * v2 uses ipv4. Most important for the exam
  * v3 for ipv6
* information stored in LSDB (link state database), collected from LSA (link state advertisements)
* routers flood LSAs until all routers have same map in the LSDB
  * LSA: 
  * contains
    * router ID: loopback
  1.  LSA floods all network interfaces
  2.  all routers share same LSDB (full of LSAs)
  3.  each router uses SPF (dijsktra) algorithm to calculate best route
  4.  LSA re-flooded every 30 minutes

### OSPF Areas
* routers flood everything in an OSPF *Area* 
  * use areas to divide network
  * if a network is huge, 500 networks with many subnets each, this is bad because:
    * SPF takes more time to calculate routes
    * much more processing power
    * large database
    * every smallest change causes a flood on all routes.
  * dividing the network into smaller areas prevents these issues
  * take a network which has trees of routers branching off a central branch (backbone) of network infrastructure
  * each router at the border of this backbone and their branches get their own area
  * the backbone is area 0. All other areas must connect to this. You cannot nest layers
  * if a router's interfaces are all inside an area, they are internal to that area
  * if the router is on the border between two areas is an area border router, ABR
    * abr can only connect to maximum of 2 areas
  * any router connected to the backbone area is also a backbone router
  * ASBR: autonomous system boundary router. connect backbone to outside network using a default route
  * intra area route: route to a network in the same area
  * interarea route: route to destination in another OSPF area
* every area must be contiguous. Two areas cannot be separated by another area
* you cannot nest one area under another. All areas must have an ABR to the backbone
* OSPF interfaces in the same subnet must be in teh same area

### Basic Configuration
* to enter OSPF config mode
  * `router ospf (process id)`
  * one router can have many of these, note
  * routers with different PIDs can become neighbors. PID doesnt make a difference. Unrelated to area
* to apply OSPF area to subnet
  * `network (network ip) (network wildcard) area (area number)`
  * look for any interface with the IP address in the range specifies
  * activate OSPF on that interface
  * become OSPF neighbors to any routers connected on that interface 
* `passive (interface)`
  * configure passive OSPF interface
  * no OSPF hello messages on this interface
  * the passive interface will tsill be advertised to other routers
* advertise default route
  * `ip route 0.0.0.0 0.0.0.0 (next hop to ISP)`
  * from router config mode
    * `default-information originate`
* `show ip protocols`
  * routing protocol: ospf (pid)
  * router ID:
    1. manually configured
      * from ospf config
        * `router-id (id)`
        * `clear ip ospf process` to restart the ospf process for change to take effect. VERY BAD IDEA. this will take the router down and reset all ip routes
    2. otherwise highest IP on loopback
    3. else highest IP on physical interface
  * contains OSPF router type (internal, ABR, etc)
  * number of areas in router
  * maximum path: 4 by default. 
    * no unequal cost load balancing
    * support ECMP load balancing over 4 paths by default
    * `maximum-paths (1-32)` to change maximum paths to load balance over
  * routing for networks:
    * what networks is OSPF routing for?
  * routing information sources:
    * list neighbors and their router IDs
  * distance: 110 by default
    * `distance (number)` to make OSPF higher priority

### OSPF metric
* cost
* auto calculated based on bandwidth of interface
* dividing reference bandwidth by interface bandwidth
* reference is 100 mbps
* 10mbps interface would have cost of 10
* lowest cost is 1, all numbers lower than 1 round up to 1
* from router config mode `auto-cost reference-bandwidth (megabits per second)` to change the reference
  * if you dont change it to be higher, a 10000 mbps connection will have the same cost as a 1000 mbps connection. One is significantly faster but isnt regarded as such
* reference should always be higher than the hgihest speed interface
* the cost must be consistent over all the ospf routers
* entering loopbacks costs 1 always

#### manual interface cost
* to configure the cost of an interface, enter interface config mode
* `ip ospf cost (1-65535)`
* you could also change the official bandwidth of an interface
  * changing bandwidth doesnt change speed
  * bandwidth is an abstract value used to calculate routes
  * used in other calculations. Best to not change this
  * `bandwidth (kilobits)`
* use the change cost command!
* to see ospf information, `show ip ospf interface brief`

### OSPF Neighbors
* neighboring is how network map data is shared
* main task of ospf configuration
* upon neighboring, they automatically do the work of sharing network information
* upon OSPF activation, router sends OSPF hello messages every interval, defined by the hello timer
  * by default the hello timer is 10 seconds
  * sent on multicast 224.0.0.5 for OSPF 
  * remember, multicast is like broadcast, but it is only received by devices with the same multicast address
* OSPF messages in the IP header, with protocl field value of 89

### neighbor states
1. down state
   1. activated
   2. send hello message to 224.0.0.5
      1. includes the sender router ID
      2. also neighbor RID
         1. this is 0.0.0.0 on first hello, since it doesnt know its neighbor
2. init state
   1. hello message received
   2. add entry for sender to OSPF neighbor table
   3. relationship in init state
   4. hello packet received, but the router that received the packet doesnt see its own RID in the packet
3. two way state
   1. the hello packet is sent back, container both router RIDs
   2. the first router adds the RID in the table
   3. the first router sends back its own RID
   4. in other words, router received hello packet with its own RID in it
   5. if both are in two way state, all conditions are met to be ospf neighbors. Can share LSAs to build the common LSDB
      1. designated router and backup designated router DR BDR will be set up here
4. Exstart state
   1. prepare to exchange LSAs
   2. choose which router starts exchange: which router is the master, and which is the slave
   3. higher RID will become master
   4. then exchange database description packets
      1. one router sends a DBD saying it will be the master
      2. if the receiving router has higher RID, it will deny and say it will be the master. Otherwise it accepts
5. exchange state
   1. exchange DBDs containing LSAs in the LSDB
   2. no detailed information, just basics
   3. routers compare DBD information against their own LSDB 
      1. during comparison, they determine what LSAs theyre missing from teh LSDB, and ask for those LSAs
6. Loading state
   1. link state request LSR to request the missing LSAs
   2. "give me the LSAs"
   3. "ok"
   4. LSAs sent in Link State Update messages, LSUs
   5. on receiving the LSU, the router returns an LSAck to acknowledge reception
7. full state: 
   1. routers have the same LSDB
   2. fully adjacent
   3. continue to send and receive hello packets
   4. every time the hello is received, the dead timer, 40 seconds, is reset
   5. if dead timer runs out, the neighbor is removed
   6. continue to share LSAs as network evolves to ensure accurate, complete network maps in the LSDB

### Overarching workflow for OSPF
1. become neighbors with routers in the same area
2. exchange LSAs with neighbors
3. calculate the best routes and insert to routing table

### OSPF commands
* `show ip ospf neighbor`
  * shows state, dead time, address, interface, and neighbor id
* `show ip ospf interface`
  * default hello and dead timers
  * neighbor counts
  * neighbor list
* activate OSPF on interface directly
  * from interface config mode
  * `ip ospf (pid) area (area)`
  * this way we dont need to know network ID or wildcard, we just need to know what interface to activate on
* `passive default`
  * set interfaces to ospf passive (router config mode)
  * `no passive (interface)` to make ospf active

### Loopback Interfaces
* virtual router interface
* always up, unless manually shut down
* not reliant on physical interface status
  * when a physical interface goes down, the IP connected to it is gone. How to other routers reach the router using OSPF if its IP disappears?
* provides consistent IP address to identify the router, and route traffic
* if R1 has the ip address 1.1.1.1, even if a physical interface goes down, routers can send packets to it via another interface

### Network Types
* type of connection between neighbors
* types
  * broadcast
    * default on ethernet, FDDI (fiber distributed data interfaces, unimportant)
    * routers dynamically discovber neighbors using multicast address 224.0.0.5
    * designated router dr, and backup designated router bdr must be elected on each subnet
      * only DR with no neighbor
      * all subnets need DR
    * routers not dr or bdr are drother
    * in other words, on a subnet, one router must be DR, another must be BDR, all others are DROther
  * point to point
    * PPP (point point protocol), HDLC (high level data link control)
  * non broadcast
    * default for frame relay and x.25  interface
    * neighbors manually configured
* all ethernet OSPF are broadcast network types

### DR and BDR election
* order of priority
1. highest OSPF interface priority
2. highest OSPF router IDs

* first place becomes DR, second place becomes BDR
* default OSPF interface priority is 1 for ALL interfaces
* `show ip ospf interface (interface)` for interface OSPF information
* to change priority, `ip ospf priority (1-255)`
  * the `nbrc f/c` field shows ratio of full connections to total connections
* this is not pre-emptive. When DR and BDR are selected, they will keep the role until OSPF is reset
* if the DR goes down, BDR takes its place and elects a new BDR
* DROther routers will only go to full state with DR and BDRs
  * with other DROthers, they are in the two way state
* DROthers only exchange LSAs with the DR and BDR
* this prevents LSA congestion on the network, while allowinh gfull LSDB coverage
  * DR and BDR are mutlicast using 224.0.0.6

### Point to Point connection
* enabled on serial interfaces using PPP or HDLC encapsulations
* ethernet for serial connections
* send and receive OSPF hello on 224.0.0.5
* DR and BDR not elected. No need
* in a point to point connection, its just one router connected to another
* very old technology
* what is serial interface?

#### Serial interfaces
* `interface s(interface num)` 
* one side functions as DCE, data communications equipment
* the other sepcifies DTE, Data terminal equipment
* DCE side needs to specify clock rate of the connection
* `clock rate (number)`
* then configure IP like any other

* on routers, default is HDLC protocol for the serial connection
* layer 2 encapsulation
* `encapsulation ppp/hdlc` must match on both ends of connection
* which side is DTE and DCE?
  * `show controllers (interface)`

### OSPF network type config
* `ip ospf network (broadcast, non broadcast, point to point, point to multipoint)`
* manually configure what network type to use
* if one router is connected to antoher, even by ethernet, you can make it point to point

### potential problems
* two OSPF routers in different areas cannot connect
* must be in same subnet to be neighbors
* OSPF process must not be shutdown
* to remove router id, `no router-id` 
  * this will not require an OSPF reboot if the router isnt a neighbor of anything
* hello and dead timers must match among all the routers
  * from interface config mode
  * `ip ospf dead/hello-interval (seconds)`
  * `no ip ospf dead/hello-interval`
* authentication settings must match
  * OSPF can be configured to have a password
  * `ip ospf authentication-key (password)` to set password
  * `ip ospf authentication` to enable authentication
  * only ospf routers with the same authentication key configured will be able to be neighbors
* IP MTUs must be the same
  * maximum transmission unit
  * if they are different, they can become neighbors, but wont communicate properly
  * `no ip mtu` to reset ip mtu settings
* OSPF network types should match

### LSA Types
* 11 types
* 3 important ones
  * type one (router lsa)
    * all routers generate this
    * identify router using ID
    * list networks attached to OSPF interfaces
  * type two (network lsa)
    * generated by DR of the multi-access (broadcast) networks
    * lists routers attached to network
  * type five (as-external LSA)
    * gneerated by ASBRs to destinations outside the AS
* `show ip ospf database` to see lsdb

## FHRP
* first hop redundancy protocols
* HSRP hot standby router protocol
* VRRP virtual router redundancy protocol
* GLBP gateway load balancing protocol

### What do they do?
* router failures happen
* where STP provided switch redundancy, FHRP provides router redundancy to external networks
* this creates a challenge, since each router has its own IP address
* each host will have only ONE default gateway, so how do they know to change their default gateway on failure?
* how do we fix this? assign a VIP, virtual IP address to the router group, and set that VIP as the default gateway for hosts
* the backup router takes over the address when the main router fails

#### FHRP process
1. routers join the same VIP
2. send multicast hello's to one another
3. determine which router is active, or standby
   1. active routers are the ones routing for the network
   2. standby will step in if active router fails
4. when a host uses ARP on the VIP, the active router returns the FHRP virtual mac address
5. if the active router goes down, it stops sending hello's to the standby routers
   1. if the standby routers stop receiving, they decide the same way as originally who becomes active
   2. when this happens, switches must be updated to reflect the change
   3. new active router sends gratuitous ARP replies (ARP replies without requests, bradcast), to tell the switches where the VMAC is
   4. the switches relearn what interfaces will let them reach the VMAC
6. if the former active router returns, by default FHRPs are non pre-emptive
   1. the new active router stays as the active router
   2. they can be configured to be pre-emptive so the previous active router takes back control

* so briefly:
  1. virtual IP configured on two routers, virtual mac generated for virtal IP
  2. active and standby routers are elected
  3. end hosts configured to use VIP as gateway
  4. active router replies to ARP using VMAC
  5. if router fails, standby takes control, and sends gratuitous arps. now default gateway
  6. if old active router comes back, it wont take the active role back
     1. this is unless preemption is configured

### HSRP
* hot standby router protocol
* cisco proprietary
* active and standby routers elected
* versions 1 and 2, for ipv4 and 6 respectively
* use multicast 224.0.0.2 and 224.0.0.102 for HSRP hello messages on v1 and 2 respectively
* virtual mac addresses are 0000.0c07.acXX and 0000.0c9f.fXXX are the VMACs used, where XXX are the group numbers
* you can also configure a different active router for each subnet/vlan to load balance

* for separate subnet/vlan balancing:
  * each subnet shares the same VIP address
  * however, on the separate subnets, the active router is set to be different

### VRRP
* virtual router redundancy protocol
* open standard
* nearly identical to HSRP
* master and backup instead of active and standby
* 224.0.0.18 for ipv4 multicast
* VMAC 0000.5e00.01XX where XX is vrrp group number
* each subnet has a different master router
* note: hosts in same vlan should be ont eh same subnet. THis isnt necessary per se, but its the best convention

### GLBP
* gateway load balancing protocol
* cisco proprietary
* load balances on routers IN THE SAME SUBNET!
* single AVG, active virtual gateway is elected
* four AVFs assigned by AVG, max 4
* each avf acts as a default gateway for some hosts in subnet
* multicast ipv4 is 224.0.0.102
* vmac is 0007.b400.XXYY
  * XX = GLBP group number
  * YY = AVF number

### HSRP configuration
1. enter interface config mode on network connected interface
   * `interface (interface)`
2. `standby (group number)` to confiugre HSRP
   1. best to match vlan group number to the HSRP group
   2. must be the same between both routers
3. `standby version (1/2)` to configure version
4. `standby (group number) ip (VIP)`
   1. configure the virtual IP
5. `standby 1 priority (0-255)`
   1. set the priority so routers can decide which will be active
   2. highest priority gets active
   3. if both routers have same priority, highest IP address is active
6. `standby (group number) preempt` 
   1. enable preemption
7. `show standby` shows standby information
## TCP and UDP
### Layer 4 
* the transport layer
* encapsulates packet with transport header
* provides (or not provide) various services to applications
  * reliable data transfer
  * error recovery
  * data sequencing
  * flow control (dont send data faster than can be received)
  * provide layer 4 addressing (port numbers). completely different than layer 2 ports
    * identify application layer protocol
    * session multiplexing
    * session? exchange of data between two or more communicating devices
      * must handle multiple communications at once
      * communicate with server 1 and server 2 at the same time
### TCP packet:
* destination port: what application layer protocol is being used? eg port 80 = http
* source port: randomly selected by pc1, helps identify the session
* when a server for instance receives a request from port 50 destined for port 80, when it replies those values are reversed. Source is 80 and destination is 50.
* you can do this for as many sessions as your computer has capacity for. You can have multiple sessions with one client as well

### port numbers
* IANA assigns what ports are used by applications
  * well known ports: 0-1023, strictly regulated, important
  * regeistered: 1024 - 49151, less regulated, must be registered to be used
  * ephemeral/private/dynamic port: 49152 - 65535, private operations, not registered. these are the randomly selected source ports

### TCP
* briefly
  * connection oriented protocol
  * before sending data the two hosts communicate to establish connection. Data excahnge begins after start of connection
  * reliable communication
    * destination must acknowledge it received each TCP segment.
    * segment is name of layer 4 PDU
    * if segment isnt acknowledge, it is sent again
  * provides sequencing
    * allows destination hosts to put segments into correct order, even if they arrive out of order
  * tcp provides flow control
    * the destination host can tell the source host to make data transfer go faster or slower

### TCP header
* l4 header
  * source port: 16 bits, 65536 port numbers for source port
  * sequence number/acknowledgement number: sequencing and acknowledgement
  * flag bits: 
    * ack: acknowlege connection
    * syn: synchronize connection
    * fin: finish
  * window size: flow control

### 3 way tcp handshake. Create connection
* 3 messages must be sent to establish connection
  1. establish connection with the SYN flag set to one, sending tcp segment
  2. reply from target with syn and ack flag set to 1
  3. first client sends an ack segment, and all connection is ready

### 4 way tcp handshake. Terminate connection
1. send segment with fin flag set to 1
2. receive response with ack flag set to 1
3. receive response with fin flag set to 1
4. send segment with ack flag set to 1

### TCP Sequencing and acknowledgement
exchange between 2 pc
1. pc1 do 3 way handshake, assign random sequencing number (10)
2. pc2 do 3 way handshake, also assigns a random sequencing number (50). Also acknowledges the sequence number by replying with ACK of 11, 10+1. Responds with ack of the sequence it expects next
3. pc1 finishes the 3 way handshake, with sequence 11, and acknowledgement of 51, because it received a sequence number of 50

this continues on along
* hosts set random initial sequence number
* forward acknowledgement is used to indicate what sequence it expects to receive next

#### retransmission
* pc1 sends sequence number 20
* there is an acknowledgement from pc2 of 21
* pc1 sends segment with no acknowledgement
* resends the request to ensure it is received
### TCP control flow
* acknowledging every single size is inefficient if size is not considered
* TCP header window size allows data to be send before acknowledgement is required
  * what does this mean? pc1 can send 3 segments at a time before requiring acknowledgement
* sldiing window can be used to dynamically adjust how big the window is.

### UDP
* much simpler
  * not connection oriented
  * the sending host doesnt need connection to send data
  * no reliable communication assurance
  * acknowledgements are not sent 
  * if data is lost, no way to retransmit it
  * segments are sent best effort
  * UDP doesnt sequence
  * udp doesnt control flow

##### If TCP is a rifle, UDP is a shotgun

* 4 fields in the segment
  * source and destination ports
  * length
  * checksum so receiving host can check for errors

### comparing tcp and udp
* tcp is more stable and has more features
  * more overhead
* for reliable communication you want TCP
* for applications like real time voice and video, UDP is preferred
  * dont want tcp slowing stuff down

both provide layer 4 addressing with ports and layer 4 multiplexing

### port numbers
* TCP ports:
  * FTP data 20
  * FTP control 21
  * SSH 22
  * Telnet 23
  * SMTP 25
  * HTTP 80
  * POP3 110
  * HTTPS 443
  * OSPF 89
* UDP
  * DHCP server 67
  * DHCP client 68
  * TFTP 69
  * SNMP agent 161
  * SNMP manager 162
  * Syslog 514
* both
  * DNS 53

## IPV6
* improved ipv4
* written in hexidecimal
* 6 in version field of ip header
  
### why ipv6?
* not enough ipv4 addresses in existence!
* there are only 4294967296 addresses. Not enough!
* when ipv4 was made, the designers didnt expect internet to get so big
* VLSM has allowed ipv4 addresses to be preserved on ipv4, along with nat
* ipv4 addresses are assigned by IANA
  * IANA distributes htem to RIR (regional internet registries) which can assigned them to companies that need them
  * the North american ARIN RIR delcared exhaustion of ipv4 in 2015
* An ipv6 address is 128 bits, quadruple of ipv4
* that means it has 340 undecillion addresses. That should be plenty
* an ipv6 address looks like:
  * xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/64
  * 4 times as much information in an ipv6 address than ipv4
  * uses the slash subnet mask convention, no dotted decimal subnet masks

### shortening IPV6 address
* they are pretty long, so they are hard to remember
* but we can make them simpler in a few ways
* remove the leading 0's
  * remove any segments of the address that start with 0
* replace quartets of 0s can be replaced by ::
* 2001:0DB8:0000:0000:0000:0000:0080:34BD thus becomes
  * 2001:0DB8::0080:34BD
  * how do we know thsi works? there are 8 quartetes in the ipv6 address. Thus we see only 4 quartets, we know 4 are 0's
  * the limitation is that only one set of consecutive 0's can be removed
  * if we had an address with this issue, we could do this:
    * 2001::20A1:0:0:34BD
    * make each other sequence of 0s outside the main sequence a single 0
* when both methods are applies:
  * 2001:DB8::80:34BD

### IPV6 Prefix
* works the same as with ipv4
* change all host bits to 0, whats left over is the global unicast address, or prefix
* typically an enterprise requesting an address gets a /48 block
* typically, ipv6 subnets utilize /64
* thus the company has 16 bits to do subnetting
* remaining 64 bits used for hosts
* 2001:0DB8:0000:0000:0000:0000:0080:34BD/64
  * first half of the address is the network portion
  * the last quartet in the network portion is used for subnetting
  * in this case, the first 3 quartets are the global routing prefix, the 4th quartet is the subnet identifier
  * last 64 bits is the host portion of subnet
  * remember, each character in hexidecimal if 4 bits
  * /64 refers to how many bits are in the network portion
  * if you have a mask that isnt a multiple of 4, you must break down individual hex characters into binary, and set all bits not included in the mask to 0. The value converted back to hex is the value in the network address

### configuration
1. `ipv6 unicast routing (enable routing for ipv6)`
2. `interface (interface)`
3. `ipv6 address (ipv6 address)`
4. `no shutdown`

* note that every interface has 2 ipv6 addresses. On eof these is auto generated link local address. learn about them later
  * ipv4 has these, but not automatic

### EUI configuration
* extended unique identifier
  * `Modiefied` EUI64
  * convert 48 bit mac address into a 64 bit interface identifier
  * this interface identifier can become the host portion ofa  /64 ipv6 address
* procedure
  * partition the mac address in half
  * you now have 2 halves
  * insert hex FFFE in the middle
  * then invert the 7th bit. 1 -> 0 
  * this becomes the host portion of the ipv6
* config
  1. from config mode, enter` int (interface)`
  2. `ipv6 address (/64 address network portion)/64 eui-64`
  3. `no shutdown`
* why invert the 7th bit?
  * UAA
    * universally administered address
      * uniquely asigned to the device by manufacutrer
  * LAA
    * locally administered address
      * manyually assigned mac-address assigned by admin
  * the 7th bit represents whether the mac is UAA or LAA, called the U/L bit
    * 0=UAA
    * 1=LAA
  * this means that when ipv6 address is made using EUI-64, the address U/LAA bit is flipped
* This is just a generation method
### IPV6 Address types
#### Global UUnicast Address
* public address that can be used over internet
* must register to use them, because they arre public it is expected they are globally unique
* originally defined as 2000::/3 block
* now all unreserved addresses are global unicast
* structure
  * first 48 bits global routing prefix, ISP identifier
  * next 16 bits subnet identifier to make subnets, the network identifier
  * the last 64 bits are the interface identifier, the host portion of the address

#### Unique Local Addresses
* private addresses not used on internet
* no need to register, used freely within networks. Cannot route over internet. ISP drops packets destined for unique local addresses
* FC00::/7 is reserved for unique local
* the 8th bit of the address must be set to 1, thus the first two digits must be FD. FD Indicated unique local address
* structure
  * first 8 bits are FD
  * next 40 bit global identifier, autogenerated to keep companies isolated. Avoid duplicate subnects
  * next 8 bits subnet identifier
  * last 64 are the interface ID, host portion

#### Link local addresses
* autogenerated on IPV6 enabled interfaces 
* this is what is generated automatically by ipv6 enable
* uses FE80::/10
* standard states the 54 bits after should all be 0. Only FE8 is allowed
* Interface id is generated using EUI64 rules
* link local are used for single subnet communication. No routing between subnets
* common uses
  * routing protocol peerings (ospfv3 uses link local addresses for neighbor adjacencies)
  * next hop addresses for static routes
  * neighbor discovery protocol uses link local addresses

#### Other address types
* Unspecified: all 0. ::
  * `i dont know my ipv6 address
  * same as 0.0.0.0
* Loopback: ::1
  * test stack on device. 
  * IPV4 equivalent is 127 family of addresses
  * doesnt waste space for all addresses in the same range, however.
#### Casts
* Unicast addresses have one source and one destination
* Broadcast addresses are from one to everyone
* multicast are from one to several, but not all
  * FF00::/8 for multicast
* Anycast: one to one of many
  * multiple clients have same address
  * they use protocol to advertise address
  * when sending packets, routers will forward it to the nearest router configured with that IP address
  * has no defined IP range. 
  * to configure it, just do the ipv6 address (address) anycast

* IPV6 does not use broadcast, but this can be replicated with multicast

#### Multicast addresses
* Broadcast: FF02::1
  * ipv4 version 224.0.0.1
* all routers: FF02::2
  * 224.0.0.2
* all OSPF routers: FF02::5
  * 224.0.0.5
* all OSPF DRs/BDRs: FF02::6
  * 224.0.0.6
* All RIP routers: FF02::9
  * 224.0.0.9
* all EIGRP routers: FF02::10
  * 224.0.0.10

KNOW THESE FOR THE EXAM

* ipv6 defines mutlicast scopes which indicate how far the packets should be forwarded
* these all use the link local scopes

### Scopes:
* interface local: FF01: Localhost, stay in local device
* link local: FF02: Stay in local subnet
* site local FF05: can be forwarded on WAN, but shouldnt. Designed for individual physical space liek office
* organization local FF08: For whole organizations
* Global FF0E: no boundaries. Over internet

generally you have to configure boundaries yourself, beyond link local

## IPV6 routing
##### Standardization of representation
RFC5952
* leading 0 must be removed
* :: required to shorted longest string of 0 quartets
  * if there are two of equal length, shorten the leftmost string
  * if there is one that is only one quartet of 0, dont shorten it
* hexidemial characters a b c d e and f must be in lowercase

### IPV6 Header
* much simpler than ipv4
  * because fixed header, not variable size
* contains payload length
* the header is always 40 so it is easier to process

#### fields
1. version field: 4 bits. Version used. Always set to 6
2. traffic class field: 8 bits. Quality of service to specify high priority traffic, so high consumption traffic gets more bandwidth (video calls and stuff)
3. Flow label: 20 bits, define traffic flows, communications between source and destination
4. payload length: 16 bits, indicated length of payload, the encapsulated segment in bytes. 
5. next header: 8 bits, header of encapsulated segment. Same as protocol field ipv4
6. hop limit: 8 bits. Decremented by one every hop. When this reaches 0 the packet is dropped
7. source address: 128 bits
8. destination address: 128 bits 

### NDP NEighbor Discovery Protocol
#### Solicited node multicast address
* ipv6 address from unicast address
  * ff02::1:ff + last 6 hex digits of unicast address

#### NDP Protocol as replacement for ARP
* ARP equivalent for IPv6
* uses ICMPv6 packets and solicited node multicast addresses to learn macs of other hosts on a LAN
* two message types:
  * neighbor soliciation message: NS, ICMPv6 request (type 135)
  * Neighbor advertisement: NA ICMPv6 Type 136
* destination address is the solicited node multicast address. 
  * since I typed in the address of the target host, we can autogenerate the solicided node multicast address 
  * then the target ip sends back its mac address

#### IPV6 neighbor table
* show ipv6 neighbor
* this command shows a table of IPv6 addresses and their mac addresses as learned by NDP

#### NDP as a routing protocol
* NDP can also automatically find orutes on LAN
* Two messages used:
  * Router solicitation (RS) icmpv6 type 133
    * send to FF02::2 (all routers)
    * asks routers to identify themselves
    * sent when an interface is enabled, host connected to network
  * router advertisement (RA) ICMPv6 type 134
    * sent to FF02::1
    * announces its presence as well as other information about link
    * send in response to RS
    * sent frequently even when no RS received
  * all IPV6 hosts send RS when they connect
  * ` Any routers here ? ` ` IM A ROUTER! `

#### SLAAC
Stateless address autoconfiguration
* hosts use RS and RA to learn IPV6 prefix of the local link then create an IPV6 address
* using ipv6 address eui-64 requires manual prefix entry
* ipv6 address autoconfig uses NDP to learn prefix instead and then use eui-64 to generate the password

#### DAD
duplicate address detection
* NDP uses DAD to identify if any local link devices are using duplicat addresses
* any time ipv6 initializes or ipv6 is confured, it performs DAD
  * uses the NS and NA
  * if it gets a reply, that means it is a duplicate address
  * otherwise there is no duplicate

### IPV6 routing
* static routes work the same in ipv6 as in ipv4
* ipv6 and ipv4 routing and routing tables are separate 
* show ipv6 route to get routes
* ipv4 enabled by default, ipv6 disabled by default

* network route is added for each connected network
* local host route automatically added for each address configured on the router 

#### route configuration
ipv6 route destnation/prefix length {next hop | exit interface (next hop)} (ad)
* direct attach
  * only exit interface is specified
  * ipv6 route destnation/prefix length exit-inteface 
* recursive static route
  * only the next hop is specified
  * ipv6 route destination/prefix-length next-hop
  * 
only recursive works to ipv6
 
#### types of routes
* network route: to another router in the network
* host route: route directly to a host connected to an interface of the router
* default route: if the target ip is ::/0, send to this address. Needed for OSPF
  * AD must always be higher than 90 for EIGRP
* fully specified: requires both exit interface and next hope, used only when you need to use local interface for routing

## Standard ACLs
This is a security fundamental
### what are these?
* access control lists have several uses
* specifies who can access what in a network
* primarily these are for security
* some other uses
* function
  * packet filter. allow or drop some traffic
  * even when a route for a packet exists, the ACL might drop it if told to do so
  * ACL can filter based on IP, and port numbers

### example
* policy: network x hosts should be able to access network z, but network y should not
* ACL made up of ACEs, access control entries
  * if source ip = network x, allow
  * if source ip = network y, block
* it will block packets even if the route exists
* acls are configured globally
* after creation the acl must be applied to an interface
  * inbound or outbound
    * inbound means into the interface from the lan it is connected to, outbound means into the lan from the interface
    *  in other words, inbound is relative to the interface, facing towards its lan. 
* The ACL is basically an if elif else chain, it goes through each option until it meets one that is true, and if it finds none it runs else
* each interface can only have 2 acls, one inbound and one outbound. Specifying a 3rd one will override

### implicit deny
* what if a packet doesnt match any acl entries? The packet is denied. 
* If there is no ACE matching the packet, it is denied
* this is why if you want to allow non-specified traffic to pass through you should have a passthrough ACE for 'any' source IP

### ACL types:
#### Standard ACL
match only by source IP

##### NUMBERED
* standard numbered: identified by number
  * can use the numbers 1-99 or 1300-1999
  * from config:
    * method set 1
      * `access-list (number) deny | permit source_ip wildcard-mask`
      * `access-list 1 deny 1.1.1.1 0.0.0.0`, where 1.1.1.1 is the ip and 0.0.0.0 is the wildcard mask, specifying it as a /32 ip
      * you could also use `access-list 1 deny host 1.1.1.1`
      * if you just enter `access-list 1 deny 1.1.1.1`, it will block that specific ip, since the wildcard mask defaults to 0.0.0.0.
      * in order to permit all other connections, you would add:
        * `access-list 1 permit any`
        * or, `access-list 1 permit 0.0.0.0 255.255.255.255` (ip wildcard combo is the same as any)
      * to add a comment, you can add a remark
        * `access-list 1 remark ## (description) ##`
      * to see list of access lists:
        * ip lists: `do show ip access-lists`
        * all lists: `do show access-lists`
      * do `show running-config | include access-list` to only show access list entries
    * method set 2
      * enter the config mode for the ACL
        * `ip access-list standard 1`
        * example:
          * `deny 192.168.1.1`
          * `permit any`
  * applying the ACL
    * `interface (interface number)`
    * `ip access-group (number) (in | out)`

##### NAMED
* standard named: identified by name
  * to config named ACLs, you must enter named acl config mode
      * `ip access-list standard (acl-name)`
    * once in the config mode, you can add the ACEs
      * `deny | permit source_ip wildcard-mask`
      * add remarks the same as with the numbered acls
      * `interface (interface)`
      * `ip access-group (acl name) in | out`
      * `show access-lists`
      * `show running-config | section access-list`

##### Advantages of config mode
* easily delete ACEs with the no command
  * if you try to delete a specific entry when in global config mode, it will just delete the whole acl
  * `no (entry number)`
  * this easily deletes 
  * on the other hand if you try to delete from global config mode, you can only delete the entire ACL
* you can insert new entries between other entries by specifying sequence number
  * in global config, if you add an ACE, it just gets appended to the end of the ACL with a number 10 higher than the previous
  * this is why the incrememnt on the numbered acls is 10, if it was just 1 you could insert a new number between 3 and 4. Dont take for granted python datastructures man!

##### Resequencing ACLs
* `ip access-list resequence (acl-id) (starting-sequence-nuber) (increment)`
* example:
  * ip access-list resequence 1 10 10
    * 1 = acl id
    * 1st 10 = what to replace 1st ace index with
    * 2nd 10 = what is the increment value for each index from ACE to ACE


#### Extended ACLs
remember: extended ACLs should be applied as close to the source as possible 
same as standard, but can match packets based on source OR destination ip, or source/destination port
* numbered have the ranges 100 -199 and 2000 - 2699
* command:
  * `access-list (number) (permit | deny) (protocol/port) (src ip) (dest ip)`
* config mode:
  * `ip access-list extended {name | number}`
    * `(sequence number) (permit | deny) (protocol) (src ip) (dest ip)`
  * you can see all the metrics for filtering with deny ? from config mode 
  * protocol number: remember, encapsulated field of ipv4 packet which specifies protocol, like tcp or udp
  * you can also just use the name, like tcp or eigrp
    * 1: icmp
    * 6: tcp
    * 17: udp
    * 88: eigrp
    * 89: ospf
    * ip: use this if you want to block all IP packets regardless of encapsulated protocol
  * source IP: You must include the wildcard like with standard ACL, or you can use the host style. You cant do neither
  * source `ip any` blocks all
  * destination ip:
    * same a ssource IP
  * port numbers
    * to specify sourc eport, specify it after source host and wildcard
    * likewise, for destination port specify it after the destination host and wildcard
    * `deny tcp (src ip and wildcar) eq (source port number) (destination ip) (destination wildcard) eq (destination port number)`
    * eq: equal to
    * gt: greater than
    * lt: less than
    * neq: all except 
    * range x y: specify port range from x to y
  * other options after the ip and wildcard:
    * ack: match tcp ack
    * fin: match tcp fin
    * syn: match tcp syn
    * ttl: match packets with specific ttl
    * dscp: match packets with certain dscp value

## CDP and LLDP
Layer 2 discovery protocols
### Layer 2 Discovery Protocols
* share with and gather information from neighbors. 
* no ip packets in the frames, since this is layer 2.
* They can however be configured to share layer 3 information
* includes host name, ip address, device type
* CDP is Cisco Discovery Protocol, proprietary
* LLDP, link layer discovery protocol, is industry standard IEEE 802.1AB
* since these share information about devices they can be security risks and are not often used

### basic overview
* device 1 frequently sends information to device 2, like interface and device specs
* device 2 does the same

### CDP
* enabled on cisco devices by default
* CDP messages are periodically sent to multicast mac address 0100.0CCC.CCCC
* despite using multicast, the message is not sent to several devices
  * neighbors dont forward the packets, its a one stop message
* by default these messages are sent once every 60 seconds out of all interfaces with an up state
* The CDP neighbor table holds for 180 seconds. If a device doesnt receive a message from a device in 180 seconds it drops the value from cdp table
* 2 versions of cdp, cdpv2 by default. cdpv1 is very old and obsolete

### CDP Commands
* `show cdp`: show cdp information
* `show cdp traffic`: show cdp history
* `show cdp interface`: show what interfaces have active cdp on them
* `encapsulation`: shows type of ethernet being used
* `show cdp neighbors`:
  * lists device ID, like switch1 or router4
  * connected interface, what interface is the device ID connected to?
  * holdtime, how much time is left to receive a new CDP advertisement?
  * capability, what these letters mean is on the top when command output
  * platform: model of neighboring device.
* to get additional information, do:
  * `show cdp neighbors detail`
  * shows vlan, and duplex setting
  * helps show vlan mismatch
* to get filtered output, do
  * `show cdp entry (name, like R2)`
* CDP overall is useful for debugging network structures
* to enable cdp
  * `cdp run`
* to disable cdp
  * `no cdp run`
* to enable or disable cdp on an interface
  * from interface config mode
    * `cdp enable`
    * `no cdp enable`

### LLDP
* industry standard
* disabled by default
* devices can run CDP and LLDP
* LLDP messages use the multicast address 0180.C200.000E
* lldp messages send by default every 30 seconds
* hold time is 120 seconds
* lldp has reinitialization delay. If lldp is enabled, the timer will enable actual initialization by a time. 
  * why? prevent rapid switcing of lldp on and off. dont need to know this

### LLDP Commands
* LLDP is usually globally disabled
* disabled on each interface by default
* to enable, you must enable it globally then on each interface
* enable globally
  * `lldp run`
* disable globally
  * `no lldp run`
* on interface
  * enable transmission 
    * `lldp transmit`
  * enable receiving
    * `lldp receive`
* for lldp you need to enable both transmission and reception
* lldp time config
  * `lldp timer (seconds)`
  * `lldp holdime (seconds)`
  * `lldp reinit (seconds)`
* show commands
  * `show lldp`, basic statuses
  * `show lldp` traffic: show traffic info
  * `show lldp` interface: show lldp info for each interface 
  * `show lldp` neighbor: the lldp connection table
  * `show neighbors detail`: show detailed table information
  * `show lldp` entry (name):  get detailed information for just one device name

## NTP
### Network Time Protocol
* its necessary that all devices have an accurate clock synchronized with other devices
* in cisco ios you can see the time with the `show clock` command, by default in UTC
* `show clock detail` shows the source of the time and date. If there is an asterisk by the time, the device isnt certain. Individual device clocks drift over time.
* why important to have accurate time?
  * accurate logs for troubleshooting
  * networks are relationships between devices. If log times differ, its hard to debug problems that occur between two devices.

* note, a hacker might try to screw up time so system administrators would have a harder time figuring out what they did
### Logging
* `show logging` shows device logs

### Clock config
* you can set the clock time using `clock set (hh:mm:ss) (DAY) (MONTH (DECEMBER)) (YEAR)`
* done from priveleged exec mode
* hardware and software clocks are separate, and can be configured separately
* hardware clock is calendar, software clock is clock
* hardware clock can be manually configured using `calendar set`
  * exactly the same as clock set 
* you can also sync the calendar and clock using `clock update-calendar` (set calendar time to clock) or `clock read-calendar`
* you can configure clock timezone using `clock timezone (timezone name) (hours offset from UTC)`
  * the timezone name doesnt do anything, just a label, thats why you need to specify time offset
  * must do it in the global config mode
* to configure daylight savings, do: `clock summer-time (time zone name) recurring (start date, week, week day, month, time) (end date in same format)`

**cool command**: `nslookup (url/ip)` shows information regarding dns server ip addresses, and hostname aliases (url names)
### NTP
* manual configuration is not scalable. Allows automatic time synchronization
* NTP clients request time from the NTP servers
* a device can be a server and client at the same time
* NTP allows accuracy of time within 1 milliseconds if the NTP server is in the same lan, or 50 milleseconds if connected via wan
* the further away from the reference clock, the higher the stratum, distance, and the larger the update delay
* NTP hierarchy:
  * a stratum is a layer in the higherarchy, it represents distance from the source of the time
  * atomic clocks or gps clocks are reference clocks, the origin. Stratum 0, these are the references
  * NTP servers directly cnnected to reference clocks are stratum 1, like military/ government supplied ntp server clocks. These are primary servers
  * the levels above stratum 1 are secondary servers
  * the chain keeps going until stratum 15, anything beyond that is unreliable
  * devices can get reference from other servers at the same stratum as a backup, or to increase accuracy. This is peering, symetric active mode
* the 3 modes for ntp are server, client, and symmetric active

### NTP configuration
* connect to an NTP server using `ntp server (server ip)`. get server ip using `nslookup (url)`. this enables client mode
* you can have multiple NTP servers at once, it is best to specify several in case there is a failure in one.
* to make a device prefer one server, you can add `prefer` to the end of the `ntp server` command
* to show all ntp saervers, run `show ntp associations`
  * `*` means that the host is currently using this server
  * `+` means the server is a candidate but not actively being used
  * `- and x` mean the server isnt reliable and wont be used
  * `st` field displays stratum of server
* `show ntp status` shows synchornization status, and the stratum level of the hosts
* what if I have some other routers nested deeper that I want to use a central router as an NTP server?
  * configure a loopback interface on the central router (see OSPF)
  * loopback interface is an address you can use to reach a device that is independent of physical interfaces
  * even though it is a loopback, the source ntp server will share it to connected routes, so any ntp client can reach it if their physical interface failed, just with an intermediary

### NTP server configuration
* suppose there is no longer access to a clock outside the network, you still should configure synchronization within the LAN
* `ntp master (stratum)` will make the host the master clock in the network
  * this will set the ntp connection to be a loopback, with a stratum of 8 by default, or whatever stratum you specify
    *  show ntp associations will show a stratum of stratum -1 for the master server
  * Loopback interfaces are virtual interfaces that can be advertised, loopback addresses are totally internal to the local device.

### Symmetric active configuration
* `ntp peer (ip address)`. This will sync two hosts at the same stratum

### NTP Authentication
* defend against hackers messing with time to cover their tracks
* `ntp authenticate` to enable ntp authentication
* `ntp authentication-key (key number) md5 (key)`, where key number is just an identifier and key is the password
* `ntp trusted-key (key number)` to trust the key with the select identifier
* these 3 commands must be done on all of the devices, clients and server
  * you must manually add the same key to all devices
* then on the clients, you must run
  * `ntp server (server ip) key (key number)` to add the authentication key to the server connections
  * `ntp peer (peer address) key (key_number)` to add the authentication to peer connections

## DNS
`ipconfig /all` shows all information about interface, including DNS server IP. nslookup does the same 
### Purpose
Domain name system
* Resolve, or convert, human readable names to ip addresses
* DNS Servers map DNS hostnames to ip addresses. When you search a url, you send a request to DNS and it returns the IP so you can connect
* you can discover DNS servers via DHCP
* if you nsloopkup a url, it will return a DNS server authoritatively. It will ask the dns server what the actual IP is

### Operations
* workflow:
  * I ask DNS server what is the IPv4 of a url
  * DNS server responds with the A record, ipv4 address
  * I ask DNS server what is the IPv6 of a URL
  * DNS server responds with the AAAA record, IPv6 address
* often there is no need to do dns config on routers, since for pc hosts they are usually just forwarding DNS requests
* DNS usually uses UDP for short messages, and TCP is for messages larger than 512 bytes. Port 53 is used

### DNS Cache
* `show hosts` displays DNS cache on cisco
* devices save DNS server responses to a local DNS cache, so they dont have to query DNS every time they want to visit a URL
* to see this, do ipconfig /displaydns on windows
* sometimes DNS cache records have a CNAME record
* CNAME records map one URL name to another URL name.
* usually the CNAME url maps to the ip
* you can clear the dns cache using ipconfig /flushdns

### Hosts file
* The host file contains mappings of hostnames to ips. If you put the statement `(ip address) (desired hostname)` in that file (on windows this is c:/system32/drivers/etc/hosts), you can ping that IP just by pnging the hostname. EG, if you assign the name R1, you can just do `ping R1`. This is a simple alternative to DNS usually for small networks

### Local DNS Servers
* if you want to have domain name routing only within a LAN, you can configure a router as a DNS server
* `ip dns server` enables DNS server operations
* `ip host (domain name) (ip)` maps a domain name to an IP
* with both of these commands, if the router receives a DNS request, it will return a DNS reply with mapped IP address to the requester
* `ip name-server (external dns server IP)` this will specify an external DNS server, like google's to query if the local DNS server doesnt have a mapping for a specific hostname
* `ip domain lookup` enable the server to query the external DNS server
* if you only do the last two commands, it configures the host as a dns client, and it will not handle requests from connected clients
* lastly, you can configure the default domain name
  * this will append the default domain name to the end of any hostnames without specified domain.
  * `pc1` becomes `pci.default_domain_name` 

## DHCP
Dynamic host configuration protocol
### Purpose
* allows to automatically figure characteristics of network config, such s ip, subnet mask, default gateway, dns server without manual config
* this is why when we connect to wifi, we dont have to manually set a default gateway
  * DHCP tells a host what ip, subnet mask, and interface to use when it connects to a nework
* mostly used for client services
* routers, servers, and stuff are usually manually configured because they need static IPs, and other things. 
* In small networks the router is usually the DHCP server, in larger ones its a dedicated machine
* using `ipconfig /all` we can see DHCP enabled.
  * we can also see ipv4 address, if it is 'preferred' it means the ip was previously assigned
  * dhcp lease
    * DHCP lease IP addresses to clients. These are not permanent and the client must give up the address at the end of the lease
    * without DHCP leasing, every individual device that connects and disconnects will get a new special IP address, not good because there are limited addresses, and to re-allocate an IP, a lease would need to be manually released
    * if connection is maintained after lease ends, the lease is auto-renewed and 
  * default gateway, dhcp server, and dns servers are also displayed. On home network, these are usually the same device, the router
* the windows command to release a lease is `ipconfig /release`
* `ipconfig /renew` will send a DHCP discover message to get a new address

### 4 message DHCP leasing process
* dhcp server use UDP port 67, DHCP clients use UDP port 68
* DHCP message includes message options. some of these are:
* * magic cookie (demarcates the start of the options field in a DHCP packet)
  * DHCP message type
  * DHCP server identifier (ip)
  * DHCP client identifier
  * End

#### DHCP discover
* broadcast message from client asking if there are any DHCP servers in the network
  * DHCP server learns the IP and mac of the client connecting
  * client IP address (0.0.0.0 if the client is asking for a new ip, and as such doesnt have one yet)
  * bootP flags field, important for next step. This will tell DHCP server to use either unicast or broadcast when communicating with the client
  * requested IP address (ip address the client wants, only requested if the host was previously connected to the server. Otherwise the DHCP will handle ip assignment alone)

#### DHCP Offer
* message from DHCP server to the client offering it a specific IP Address, sent as unicast to the mac address
* whether unicast or broadcast is determined by the bootP flag of the discover message
  * why would broadcast be used? some devices dont accept unicast before they have an IP configured. Thus the DHCP server must broadcast to the whole network 
* options
  * lease time
  * domain name server
  * router

#### DHCP Request
* broadcast message that tells all dhcp server on a network which server it is accepting the offer of, so that other DHCP servers know that they are not being accepted, and so the client can continue the process with the server it wants to communicate with
* if there are multiple DHCP server in a network, the client broadcasts to all of them when doing discover. Thus it needs to tell the DHCP server it is requesting from that it is accepting that DHCP offer
* client usually accepts the first offer it gets
* options
  * dhcp identifier: this is how the client knows which DHCP server IP to communicate with when it accepts an offer

#### DHCP ACK(nowledgement)
* response from server to client telling the client it may use the requested IP address

you should check out the DHCP wikipedia page

remember, the sequence acronym **DORA**
and remember what the release does

### DHCP relay
* for small networks routers can be DHCP servers
* For large ones its better to have one big central DHCP server from which routers can gather information
* however, if the dhcp is centralized, DHCP discovery broadcast messages wont reach the DHCP server. Recall, broadcast messages dont leave the local subnet. If there is a router between the DHCP server and client, the messages wont go through
* thus routers should be configured as DHCP relay agents
* DHCP relays will forward broadcast DHCP messages to the DHCP server as a unicast message
* the DHCP message process works the same just with a middleman router
  
### Router as DHCP server
* `ip dhcp excluded-address (ipv4 address range)`: this specifies IP addresses that wont be allocated to DHCP clients. These excluded are called the reserved addresses
  * if you just include a single address only that address will be blocked from entering dhcp pool
  * global config mode
* `ip dhcp pool LAB_POOL` to create DHCP pool and enter DHCP config mode
  * remember dhcp pools only go on the server
  * subnet of addresses to be assigned to DHCP clients
  * also includes DNS server address and default gateway
* to configure this range of addresses for the DHCP pool: `network (network address) (network mask / prefix length)`
* `dns-server (ip)` configures what IP the dhcp will use as the default DNS server
* `default-router (router ip)` configures what IP dhcp will use as the default gateway IP by clients connected to the network
* `domain-name (domain name)`
* `lease (num days) (hours) (minutes)` configures the standard lease time for DHCP or `lease infinite` (BAD IDEA)
* last 3 must be done in DHCP config mode
* `show ip dhcp binding` shows all current DHCP clients with DHCP addresses
* `show ip dhcp pool` shows pool information
* also, to get specific section from command, use |
  * `do show running-config | section dhcp`

### Router as DHCP Relay Agent
* enter interface config mode for interface connected to subnet with clients that want DHCP
* `ip helper-address (DHCP server address)` to say what the dhcp server address is. For this, you need to have a route, either static or dynamic to the dhcp server
  * should the configured on the interface closest to the clients that want to use the dhcp
* remember, there is a special field in the DHCP message called CHADDR, client hardware address. This is a representation of the MAC address. This is necessary because if the DHCP request is forwarded on a relay, the source mac becomes the mac of the relay

### Router as DHCP client
* from interface config mode
  * `ip address dhcp`
* then the router sends out a DHCP discover message on that interface
* this will determine the interface's ip address

## SNMP
### Overview
* industry standard protocol, simple network management protocol
* structuring and identification of managemet information fro tcp ip based internets
* not very simple anymore
* Monitor device status, make config changes etc
* 2 device types:
  * managed: being managed by SNMP
  * Network management station/system (NMS): devices managing the devices mentioned above

### Operations
NMS might be configured to notify sysadmins of events
* managed devices can notify the NMS of events
* NMS can ask the managed devices for information about their current status, like CPU usage and stuff
* NMS can send new configurations to network devices 

### Components
#### NMS
* probably not a machine dedicated to SNMP, it could just by the sysadmins pc
* the SNMP manager interacts with managed devices, handles notifications, requests, and configurations
* SNMP application: interface for the network information

#### SNMP Agents
* SNMP agent is the software running on the managed device
* sense notifications and receives requests from the NMS\
* MIB: Management information base, sturcture containing variables managed by SNMP
  * each is an object identified by object ID, OID.
  * device temperature, cpu usage, etc

#### OID
* organized hierarchically
* format:
  * .iso.identified-organization.dod.internet.mgmt.mib-2.system.sys_name, for example is the oid for hostname
  * oid-info.com

### 3 Versions
* SNMPv1: original
* SNMPv2c: allows the nms to retrieve large amounts of information in a single request
  * c refers to community strings used as passwords.
* SNMPv3: The best
  * much more secure, supports strong encryption and authentication

### Message Types
* read
  * messages sent by NMS to get info from managed device
    * Get: retrieve the value of an oid, or list of oids. Agent will return these values
    * GetNext: request to get a list of available variables in agent MIB
    * GetBulk: more efficient GetNext introduced v2
* write
  * messages sent to Agent from NMS to change information on managed devices
    * set: set an oid to a select value
* notification
  * message sent by devices to notify NMS of an event
    * Trap: sent from agent to manager, no response
      * unreliable because no response, UDP
    * inform: notification acknowledge with a response. 
* response: messages sent in response to previous request
* snmp agents listen on port 161, snmp managers on 162

### Configuration
* Only for agents
* `snmp-server contact (email)`: send information to email in case of error
* `snmp-server location (location)`: tell where the server is, just a descriptor
* `snmp-server community (community string) ro | rw`: community string is a password. ro means read only, rw means write only. the ro/rw means that if an NMS uses the community string, it will have either of these permissions
* `snmp-server host (host ip) version (version, like 2c) (community string)`: specify the IP of the NMS, which the snmp agent will connect to. The community string specified determines what the NMS can do, read or write
* `snmp-server enable traps snmp linkdown linkup`: send trap notifications if there is a change in interface state
* `snmp-server enable traps config`: enable notifications for config changes

## Syslog
### Purpose
* protocol to keep logs of events
* logs can be shown in realtime on CLI, or stored in a server to be examined later 
* industry standard
* syslog works with SNMP usually to troubleshoot devices. They complement each other with very different functions

### message format:
* sequence number:time stamp: %facility-severity-MNEMONIC:description
* sequence number: indicating the place in the sequence of saved messages
* time stamp: when the log was generated
* facility: what process generated the mssage? like OSPF
* severity: how bad was whatever happened?
  * debugging 7
  * informational 6
  * notice/notification 5: normal but important notification
  * warning 4
  * error 3
  * critical 2
  * alert 1
  * emergency 0
* mnemonic: short code for the message indicating what happened 

### Send Locations
where do syslog messages go?
* console line: messages sent to the CLI
* VTY lines: messages will be displayed when connected to device via telnet or ssh. disabled by default
* buffer: syslog messages to be saved to ram. All messages displayed 
  * view using `show logging`
* external server: send syslog messages to external server
* syslog server listen for messages on UDP 514

### Configuration
* `logging console (level, 0-7)` to enable logging for the level and all levels above
* `logging monitor (level)` enables logging to VTY lines
  * even if this is enabled, by default the messages will not be displayed to telnet or ssh users. To enable you must enter `terminal monitor`
  * that command must be used every time you connect using ssh or telnet. That creates a vty syslog session that expires after disconnection
* `logging buffered (buffer size)` sets a buffer size for logging to the specified size, and enbales buffer logging
* `logging (logging server ip)` or `logging host (server ip)` enable a logging server for log messages
* `logging trap (level)` specifies logging level for the external logging server
* if you get a log message while typing a command, this messes everything up, since the log appears in the middle of what youre typing
  * to fix this, enter line config mode with `line console 0`
  * then run `logging synchronous`
  * then `exit`
* `service timestamps log datetime/uptime`: tell syslog to log times. datetime specifies to log exact time, uptime specifies to log how long since the device was turned on 
* `service sequence-numbers` enables sequence numbers

### Syslog VS SNMP
* complementary
* syslog
  * message logging, categorization
  * system management analysis and troubleshooting
  * server cant actively pull logs from devices
* SNMP retrieve and organize deevice information
  * ip addresses, current interface state, all variables
  * supports get requests to get information, and set to set variables

## SSH
* alternative, remote way to configure devices without a console port

### Console Port Security
* by default no password is needed to access a cisco device via console port
* you can configure a password to make this more secure
  * enter console config mode with `line console 0`
  * `password (password)` to create password
  * `login` will enable password requirement
  * `exit`
* you can also configure users for a device, like with a shared linux machine
  * `username (username) secret (password)`
  * `line console 0`
  * `login local` to require user to login using on eof the configures users on device
  * `end`
  * `exit`
* `exec-timeout (minutes) (seconds)` sets inactivity timeout for console

### Remote management of layer 2 switch
* no packet routing, no routing table. Only forward lan frames
* you can assign IP to SVI, switch virtual interface, to allow remote connections to CLI using remote shell services
* SVI config is the same as default gateway on a multilayer switch
  * `interface (vlan#)` enter vlan interface config mode
  * `ip address (ip) (subnet mask)` configure ip address for SVI 
  * `no shutdown` enable interface
  * `exit` exit interface cfg mode
  * `default-gateway (default gateway for network)` configure default gateway of the switch so that devices in other vlans can access

### Telnet
* ssh precursor
* teletype network
* proto-remote-bash
* obsolete and security risk
  * PLAINTEXT!!!
* TCP port 23

### Telnet configuration
* `enable secret (password)` wihtout enable secret no remote access
* `username (username) secret (password)` enable user access if you want
* also a good idea to configure an ACL to restrict who can remote bash into your devices
* `line vty (lower vty line limit) (upper vty line limit)` telnet and ssh line needs vty lines. Limit of 16 vty lines, 0-15. 16 users can remote access these devices


## FTP/TFTP 
* FTP, file transfer protocol, tftp, trivial file transfer protocol, are industry standard file transfer systems on the server model
* clients can use can use these to copy files to and from the server
* good for upgrading the software on network devices
* download newer version of cisco IOS from a server and reboot those devices to a new IOS

### updated with FTP
* load file onto the server in LAN
* use ftp to copy the file to memory of the desired device

### TFTP
* Simpler than FTP
* Lightweight basic version of FTP. Only copy file to and from a server
* no authentication. Servers respond to all FTP requests as long as the FTP port is open
* no encryption either
* TFTP is best used in controlled environment to transfer small, unimportant files quickly
* UDP port 69
* TFTP has its own means of ensuring reliability

### TFTP reliability
* all TFTP messages are acknowledged
* this means that if the client receives no ack, it knows it has to send the message again
* if the server is sending to the client, the client returns ack
* timers are used. If the timer exceeds a threshold, retransmission

1. Read request from client
2. data response from server
3. failed ACK from client to server, client receives no more data because ack didnt go through
4. ack retransmission by client
5. server sends more data
6. ack sent by client
7. repeat until the whole file is received

* in this process, the device acting as the client is the only one that does retransmission

### TFTP connections
* 3 phase connection from client to server
    1. Connection: Client sends request to server, server responds back initializing connection
    2. Data transfer: the client and server exchange TFTP messages. One send data, the other acks
    3. Termination: after the last datagram is received, final acknowledgeemnt is sent and the connection ends.

### TFTP TID
* when first message received by server, destination is UDP69. SOurce is a random ephemeral
* random port is called a transfer identifier, TID
* The server also selects a random tID to be used as the source port for replying to the client, not UDP 69
* The next client message will be directed at this TID port, not UDP 69
* UDP 69 is only used in the first connection message from client to server

### FTP
* TCP port 20 and 21
* listens on 21, since connection is initiated using control connection
* usernames and passwords supported, but no encryption
* FTPS (ftp over ssl and tls) is used to upgrade to security
* SFTP SSH file transfer protocol can be used for greater security
* FTP can be used for directory navigation as well as copying
* client sends FTP commands, rather than requests and acknowledgements

### Control COnnections
* FTP uses 2 connection types
  * control connection on TCP 21 for sending commands and replies
  * data connection file transfers work on TCP 20
1. the same process for establishing the connection, using requests and acks occurs 
2. ftp client sends commands, and the server replies on tcp 21

### Modes for FTP
* ftp can work in two modes
* active and passive mode only apply to data connection 
* acive mode
  * default connection is active mode in which the server initiates the tcp connection
  * the control connection is maintained throughout the process
* passive mode
  * the client intiates the connection
  * important when there is a firewall in front of the client
  * a firewall might accept FTP replies, but wont accept incoming connection as a security measure

### Comparison
* FTP
  * TCP
  * commands and file transfer
  * supports auth
  * no encryption
* TFTP
  * UDP
  * only file copying
  * no auth
  * no encryption

### IOS File Systems
* you can view the file systems of a cisco IOS device with `show file systems`
* different file systems
  * disk: flash memory
    * on startup, the OS is loaded from flash to ram
  * opaque: internal function
  * nvram: non volatile ram, startup config file stored here
  * network: external file systems accessed via ftp and tftp
* `show version` command shows IOS information
* `show flash` reveals the contents of flash, the operating system
* you can use ftp to load a new version of cisco IOS onto a network device
* to do this with tftp:
  * `copy (ftp/tftp) (destination system, like flash)`
  * it will then ask for hostname, enter the device lan IP
  * then it asks for source filename and destination filename
  * you must know the local and remote filepath of the file you are transferring, tftp cant handle that by itself
  * how can we make the device use the new file as the os?
    * `boot system (filepath)`
    * otherwise, the device will use the first IOS file it finds
    * then to save the changes, run `write memory` and `reload`
    * to delete the old os file, run `delete` filepath
* to do this with ftp
  * before running ftp operations, configure the username and password
    * for username `ip ftp username (username)`
    * likewise, `ip ftp password (password)`

## NAT
### Network Address Translation
### Private IPV4
* IPV4 doesnt provide enough addresses for all devices to be globally unique
* solutions:
  * CIDR, subnetting
  * private IPV4 addresses
    * private on ranges
      * 10.0.0.0/8, 10.0.0.0-10.255.255.255
      * 172.16.0.0/12
      * 192.168.0.0/16
      * one range from class a b and c
      * private IP addresses usually exist only within lans
      * private IPs cant access the internet. This is where NAT comes in
      * RFC 1918
### NAT
* suppose there are two routers connecting over the internet, each having one client connected to their respective lans with the same private IP addresses. How does the client in one lan communicate with the client in another?
  * duplicate addresses
  * private addresses cant be used over internet
* NAT solves both
  * alhtough private IP addresses are not unique, the public IP address of router is
  * NAT allows the lan client to borrow the public IP address to access the internet
  * any number of devices can borrow the router's public IP to access the internet

### In depth
* modify source and destination IPs of packets
  * allow hosts with private IPs to communicate with other hosts with private IPs
  * thus multiple hosts can share a single public IP

#### Source Nat
* PC1 has the IP of 192.168.0.167 
  * destination is the 8.8.8.8 server (google)
  * steps for source NAT:
    1. pc1 sends packet to router
    2. router replaces the original source IP of pc1 to be the ip of the router external interface
    3. sends to 8.8.8.8
    4. server at 8.8.8.8 sends the packet back
    5. router receives on public interface and reverses the translation, setting destination IP to that of pc1, forwarding it to pc1

##### Static Nat
* This means manually configuring a one to one mapping of private IPs to public IPs (or any ip to any other ip)
* an **inside local** address is mapped to an **inside global** address
* inside addresses:
  * inside means in lan, for instance, on the router private interface
  * inside local address:
    * the ip address of the host as other devices inside the lan see it. If one device wants to send a packet to another device in the lan, this is the address they use
    * what is pc1's address?
  * inside global address:
    * the ip address of the inside host from the perspective of the outside hosts
    * the ip address of the host, like pc1 AFTER nat translation, eg when the router translates pc1's packet after it is sent out
    * this is the unique IP public ip address for the private IP
* since static nat is under the umbrella of source nat, the source nat is changed when nat happens. However, this source nat is whatever the admin configures
* but this kind of defeats the purpose of private IPs, since it means every device that wants to communicate with the internet must have a globally unique IP address

##### Static Nat Configuration
1. define the inside interface with `int (interface number)`, then `ip nat inside`
2. then define the outside interface with `int (interface number)` then `ip nat outside`
   1. both cases just require you do the main command inside interface config mode
3. once this is set up, you can configure the ip address mappings using `ip nat inside source static (inside IP address) (outside ip address)`
4. to see entries to nat tables, do `show ip nat translations`
5. each time a static nat entry is used, a dynamic nat entry is added
6. to clear these dynamic nat translations, use `clear ip nat translation *`
7. to see information about nat operations, do `show ip nat statistics`
  * shows peak translations, maximum number of translations using the table
  * total active translations
  * outside and inside interfaces

##### outside local and outside global
* outside local
  * IP address of the outside host from the perspective of the local network. what does pc1 think the address is?
* outside global
  * what is the ip address of the outside host from the perspective of the outside network, wan
* unless destination NAT is used, these two will always be the same
* inside/outside indicate location of host, inside or outside the local network?
* local/global indicate perspective from which that host is being viewed. Local network, or global network?

### Dynamic Nat
* in a dynamic nat, the router automatically maps inside local and global addresses to one another
* ACLs are used to identify what should be translated and what should be blocked
  * if the source IP is permitted, it will be translated
  * if the ip is denied, it will not be translated, but will not drop the traffic
* a nat pool sepcifies the range of addresses available to translate to
* although the mappings are dynamic, they are still globally unique. 
* what if all addresses in the nat pool are in use already? this is pool exhaustion
  * in this case, any host that tries to use dynamic nat will have its packets dropped due to saturation of addresses
  * the host cannot access outside networks until the pool exhaustion is over
    * pool exhaustion is averted by automatic nat timeouts, or manual cancellations
    * this is the key advantage of dynamic NAT, so addresses are only used when needed
* dynamic nat still doesnt allow for 2 hosts to use the same outside global IP!!! for this we need PAT

#### Dynamic Nat Configuration
1. enter inside interface config mode `int (interface)`
2. `ip nat inside`
3. enter outside interface config mode `int (interface)`
4. `ip nat outside`
5. permit traffic from desired host on the ACL
6. define the nat pool with `ip nat pool (pool name) (lower address limit) (upper address limit) netmask (subnet mask)`
7. finally, configure dynamic nat by mapping ACL to pool with:
   1. `ip nat inside source list (ACL #) pool (pool name)`

* remember in the NAT table, a new entry is created whenever NAt is used for a connection or request. These clear after a minute
* the default dynamic mappings last 24 hours
### Port Address Translation
*  aka nat overload
*  translates the port number and address
   *  by using a unique port number for every local host, many such hosts can use a single inside global address
   *  the router then keeps track of the port number and address mappings
   *  in short, two hosts can use the same inside global IP, as long as they use different ports for communication
* so then how does something like ssh work over the internet if it needs port 22?
  * only the source port is changed, the destination port attached to the destination address is still 22.
  * Once the destination server receives and responds, it sends a packet back to the origin ip and port
  * the origin router translates the packet source ip:port back to the inside local address, and the host receives the response
  * additionally, since the translation only happens inside the router, hosts can use the same ports for specific services at the same time. 
  * this is why when capturing packets with wireshark, an ssh message from host to router will have source and destination port of 22 still!!
* this basically eliminates the issue of public ip exhaustion. PAT is the most widely used form of NAT
* one IP address can represent many thousands of hosts

### PAT configuration
* PAT config is the same as dynamic nat, except you add one keyword to the last command:
* `ip nat inside source list (ACL #) pool (pool name) overload`

* you could also configure the router to use its own public facing interface address as the inside global address, using the command:
* `ip nat inside source list (ACL #) interface (interface number) overload` 

## QOS
* quality of service
* used to prioritize certain types of network traffic to make some services smoother

### IP phones
* traditional phones operate over public switched telephone network, PSTN
* IP phones use VoIP, sending voice data using IP over a network
* connected to a switch
* IP phones generally have  a3 port internal switch
  * uplink, to the external switch
  * downlink, to the PC
  * internal, to the phone itself
  * thus, network traffic goes through the IP phone to the PC, and back.
  * this is better because it needs less confiugration in big enterprise networks. Both the PC and phone have the same switch ports
  * we get half the ports for the same number of devices, better
  * best to also place phones and pcs in separate VLANs, voice vlans. 
  * how can we configure a voice vlan on a switchport?
    * when in interface config mode, do:
      * `switchport voice vlan (vlan number)`
    * pc1 will send traffic untagged as normal, and switch 1 will use cdp to tell the phone to tag its own traffic in vlan11
    * even if there is a voice vlan and a regular vlan on the same switchport, it does not require trunking!
  * thus, we have data vlan and voice vlan

### Power Over Ethernet
* how do the IP phones get power? its inconvenient to have another power cable for all phones
* PoE allows powered devices to draw electricity from a power supplying device, like a switch, over an ethernet cable
* PoE has a method to determine how much power a device needs, so its not overloaded
* when a device is connected to a PoE enabled port, the PSE switch sends low power signals, monitors response, and determines how much power the device needs
* the PSE continues to monitor the device and supplies the rrequired power
* configure power policing to prevent too high power draw
  * `power inline police` configures power policing with the default settings, to disable port and send syslog message if too much power is drawn
  * you could also do `power inline police action err-disable/log`
    * when set to 'err-disable' the interface goes to 'error disabled' and must be restarted with `shutdown` then `no shutdown`
    * if its set to log, the PSE just logs the issue and the device keeps going
* originally, cisco invented cisco ILP. 
  * later these were standardized. Power supply capability continuously went up every iteration of the standard
  * ILP -> PoE type 1 -> PoE+ type 2 -> UPoE type 3 -> UPoE+ type 4

### Quality of Service
* why QoS?
* Voice traffic and data traffic used entirely different networks.
* Since this required two separate networks, it was cost inefficient
* however, when these were integrated, data and phone traffic started competing.
* Since voice requires very high quality connection, it is given network priority
* some types of packets get high priority treatment, others get low priority

#### Characteristics
1. Bandwidth, overall capacity of the link. QoS tools allow to reserve a certain amount of link bandwidth for specific kinds of traffic
2. delay: amount of time it takes for traffic to go source to destination = 1 way delay. TIme to go there and back, to way delay
3. Jitter: variation in one way delay for individual packets. Bad audio quality. IP phones have jitter buffer to prevent jitter buffer. However too high of jitter overrides this
4. loss: % of packets that dont reach their destination. Due to faulty cables, or congested queues dropping packets

* recommended characteriustics of interactive audio
  * one way delay: 150 ms or less
  * jitter: 30 ms or less
  * loss: 1% or less
* these provide decent experience

### Queueing
* if a device receives packets faster than it can send them out of another, it puts the incoming packets into a queue. Packets forwarded in first in first out, in general
* if the queue is full, all packets incoming will be dropped
  * this is tail drop
* tail drop is bad beecause it can lead to TCP global sync
  * global means within the network
  * why is that bad? 
  * TCP use sliding window to increase/decrease rate at which they send traffic
  * when a packet is dropped its retransmitted, and transmission rate is reduced
  * transmission rate slowly increases after
  * when multiple tcp clients have the same behavior, they will all increase transmission rate at the same time, and lead to more congestion. 
  * it is a terrible cycle!!
  * waves of underutilization and overuitilization
  * solution:
    * random early detection, RED
    * when traffic in queue reaches a threshold before being completely full, the device receiving packets will drop random packets being received. 
    * This way, packets can still enter the queue since it isnt full, and other devices will experience slower network connection, avoiding the global sync problems
* Weighted random early detection, WRED allows to control priorities. High priority packets wont be dropped
  * possible to exploit this for targetted DDoS??

### Classification
* purpose of QoS is to give certain network traffic priority
* classification organized traffic into classes
* traffic identifiers allow for organization 
* classification methods:
  * ACL
    * permitted traffic is high priority
    * denied traffic is low priority
  * NBAR
    * deep packet inspection, looking to layer 7 to identify the specific sort of traffic being sent
  * layer 2 and 3 headers
    * PCP (priority code point) in ethernet header identifies prioritty, high or low (layer 2)
      * within the .1Q tag, for VLANs. 
      * also referred to as COS, class of service
      * IEEE 802.1p
      * 3 bits
        * 0, best effort
          * no guarentee that the data gets to the destination, just regular traffic
        * 3, critical
        * 4, video
        * 5, voice
          * it is important to note that the call signal for VoIP phones is classified as 3, but the actual call is 5
      * unfortunately this means the PCP can only be used over trunking links, or on the native vlan
      * the exception is access links with voice VLAN
    * DSCP field of IP header also used in the same way (layer 3)
      * ToS byte, type of service
      * IPv4 header
      * 2 parts: DSCP, ECN
        * Differentiated Services Code point
        * Explicit Congestion Notification
      * 6 bits for DSCP, 2 for ECN
      * preceeded by IPP
        * IP precedence
        * 3 bits
      * DSCP: 
        * RFC 2474
        * new more generalized markings, industry standard
          * Defualt forwarding: best effort traffic
            * 000000 in the header
            * marking 0
          * expedited forwarding: low loss latency, voice
            * 101110 in header
            * marking 46
          * assured forwarding, AF, set of 12 standard values
            * four traffic classes. All packets in one class have same priority. Higher class number have higher priority
            * within a class there are 3 drop precedences
              * higher DP means more likely to drop packets in congestion, lower QoS
              * anatomy:
              * first 3 bits represent class, 4th and 5th bit represent drop precedence, the final bit is always 0
            * when writing an AF marking, we do AFXY
              * what is XY?
              * X is the decimal number of the class, Y is the decimal number of the drop precedence
              * the normal DSCP value is just the value of the entire AF header
              * AF 43 is the highest it goes
              * to go from AF to DSCP, do 8x + 2y
          * Class Selector: set of 8 standard values provides backward compatability with IPP
            * 8 DSCP values for backward compatability with IPP
            * the 3 bits added to support DSCP are all set to 0. The original 3 IPP comprise 8 values
            * CS values always denotes as CS 0-7
              * to get the DSCP value of the CS tag, multiply the number by 8
* when configuring QoS class maps identify what traffic to match. `class map (class name)` to create
* `match dscp (dscp identifier, af, cs, df, ef)`

#### How is all this used?
* RFC 4954 aims to standardize how these are used
  * voice traffic: EF
  * interactive video: AF4x (anything with the class number to 4, and drop precedence to anything)
  * Streaming video: AF3x
  * high priority dataL AF2x
  * Best effort: DF

### Trust Boundaries
* The boundaries where they do and dont trust QoS markings
  * if markings are trusted, messages forwarded unchanged
  * otherwise, the device changes markings according to their own QoS policy
* say a trust boundary exists at switch 1, and phone 1 is sending a packet with EF, CoS/PCP 5
  * the switch doesnt trust the QoS marking since it is at the boundary, and switches the packet to DF, CoS 0
  * usually the trust boundary should be on the phones internal switch, so it can prioritize its own traffic
  * that way users can artificially increase their speed

### Queuing and Congestion Management (again)
* remember, when network receive data faster than it can send it, the queue becomes full
* when this happens, packets drop, either tail drop ( drop anything coming in once full) or using RED/WRED to avoid global TCP synchronization
* QoS essentially relies on multiple Queues
* this is where classification comes in. Device matches traffic based on DSCP markings and such, and then put it in the proper queue
* although the device can only forward one frame at once, it uses a scheduler to asynchronously forward traffic
* prioritization provides the scheduler with a sense of what order, and how quickly to empty certain queues

#### Queueing scheduling management
* weighted round robin
  * common scheduling strategy
  * packets are taken from each queue in order, cyclically
  * more data is taken from hig priority queues
* CBWFQ (class based weighted fair queueing)
  * uses weighted round robin, while guarenteeing each queue a certain percentage of avaialble bandwidth during congestion
* round robin isnt good for voice video traffic though, it adds delay and jitter. They have to wait their turn in the scheduler!
* LLQ (low latency queuing)
  * designates one or more queues as strict priority queues
  * if there is any traffic in the LLQ, the scheduler always takes the enxt packet from the queue until it is empty
  * very good for reducing the delay and jitter of voice
  * however, it can potentially starve other queues, preventing the other queues from doing anyting

#### Shaping & Policing (continued)
* boht used to control traffic rates
* what if interfaces are not operating at or above full capacity but we still want to limit traffic?
* shaping
  * buffers traffic to a queue if the rate goes over configured rate
* policing
  * drops traffic if traffic rate goes over the configured rate
  * burst traffic is allowed for a short period, so applications that send large data over a short period can operate
* classification can be used for different classifications
* but why?
  * what if a customer only bought a 300 mbps connection on a 1 gbit port? They can only transmit data at 300 mbps, way under the specs of the hardware

## Security Concepts
### Why security?
* confidentiality
  * only authorized users can access data
* Integrity
  * data should not be tampered with by unauthorized users
* Availability
  * the network should be operational for authorized users
* CIA Triad
* attackers can threaten all of these

### Keywords
* vulnerability, any potential weakness which can comrpomise the CIA of a system
* an exploit uses the vulnerability to gain access to a system
* a threat is the potential of a vulnerability to be exploited
* mitigation technique protects against threats
* no system is ever perfectly secure

### Common Attacks
* DoS
  * threaten availability
  * TCP SYN Flood
    * exploits the 3 way TCP handshake
    * in TCP syn flood, the attacker sends many SYNs at once to a target
    * the target responds, but the attacker never acknowledges
    * the target waits for the final ack of each connection, and fills up the connection table, so no other clients can connect
  * much more powerful, DDoS, does the same thing
    * uses multiple devices in a botnet to execute such DoS attacks all at once
* Spoofing
  * use a fake source address, IP or MAC
  * numerous attacks involve spoofing
  * DHCP Exhaustion
    * DHCP exhaustion attack is an example
    * an attacker uses spoofed mac addresses to flood DHCP discover messages
    * the DHCP pool becomes full, resulting in a denial of service to other devices, since the mac address changes every time
  * DHCP Decline attack
    * spoof a target IP and mac, then send a release message to the router to tell the router you no longer need the IP address
  * VLAN hopping
    * DTP exploit that allows the attacker to gain access to other VLANs
* reflection/amplification
  * reflection  
    * The attacker sends traffic to a reflector like a DNS server, and spoofs its owns ource address to be that of a target
    * the reflector, like a DNS server sends the reply to the target IP address 
    * if the amount of traffic grows enough, there is a denial of service
  * amplification
    * same as reflection, but the amount of traffic sent by the reflector grows exponentially compared to the data the attacker sends
    * DNS and NTP have this vulnerability
* man in the middle
  * an attacker sits between a connection of 2 clients, intercepting and reading packets received from one, and then forwarding them to the next, so it looks as if nothing is happening
  * ARP spoofing/poisoning
    * attacker sends an ARP request, telling the target to map the other target IP to their mac address
    * all messages will then go to the attacker in the lan
    * attacker could also modify messages before forwarding them
  * DHCP Poisoning
    * A 'spurrious' DHCP server, an attacker pretending to be a DHCP server responds to DHCP discover messages from clients before a legitimate DHCP server can
    * the fake DHCP attacker assigns an IP to the client, then tells the client that the attacker IP is the default gateway
    * the attacker forwards packets to and from the client and server, but intercepts all
* reconnaissance
  * collect publically available information, OSINT
    * nslookup to find IP of website
    * lookup.icann.org to find website information
* Malware
  * evil programs
  * viruses
    * infects other programs to spread, requires a host to move around. 
  * Worms
    * same as viruses, but can move around on their own without user interaction
  * Trojan
    * harmful software disguised as good software
  * Rootkit
    * malware embedding in the kernel of the computer
* Social Engineering
  * trick people into giving up secrets
  * phishing
    * legit looking email containing link to fraud website which logs data, credentials, and such
    * spearphishing
      * targetted phishing attack to certain people
    * whaling
      * taargeted at high profile members of an organization
    * vishing
      * voice phishing, scam calls
  * watering hole
    * compromise a website users like to visit, then steal information from there
* password related attacks
  * most systems have passwords
  * username is usually easy to guess, like an email address
  * password strenght is relied on for security
  * ways to get passed passwords:
    * guessing (I guess)
    * dictionary attack with common/previously leaked passwords
    * brute force: test all char permutations, requires very powerful computer
  * long passwords are the best way to avoid brute forcing
  * passwords should also be changed regularly

### Multi Factor Authentication
* what if the password is leaked?
* usually relies on OAuth industry standard processes

### Digital Certificates
* prove the identity of the cert holder
* used for websites to verify legitimacy of the website
* organizations that want a cert ask for a certificate from a CA, certificate authority

### AAA
* authentication, authorization, accounting
* monitoring and control framework
* authentication:
  * verify user identity
  * passwords, usernames
* authorization:
  * process of granting permissions
  * what services can the user access? what cant they access?
* accounting:
  * record user's activities on the system, surveillance of user activity
* most companies use AAA servers which administer these services, running on:
  * RADIUS protocol: industry standard UDP 1812 1813
  * TACACS+: Cisco proprietary protocol TCP 49

### Security program elements
* user awareness programs: make employees aware of threats
* user training: train users in cybersecurity basics and policies
* physical access control: lock the stupid doors for the sensitive equipment!!! 

## Port Security
* port sescurity is a feature of cisco switches
* allows control over what mac addresses are allowed to enter the switchport
* if unauthorized source mac address enters the port, the switch does something
  * by default, the interface enters an err-disabled state 
* when configuring port security on an interface with the default settings, one mac address is allowed
  * allowed mac addresses can be configured manually
  * alternatively, the switch will allow the first mac address that enters the interface
* you can also increases the maximum number of mac addresses on the port, such as with a pc connected in series with a voip phone to a switch
* if more than one mac address is allowed, they all dont have to be automatic or manually configured, you can have a combination

### Why?
* net admins can control what devices have access toa network
* however, mac spoofing isnt so hard
* port security's ability to limit the number of mac addresses allowed on an interface is good.
  * the DHCP starvation attack for instance relied on spoofing thousands of separate mac addresses and sending DHCP requests to the DHCP server. That is impossible with port security
  * switch mac address tables can only hold so many mac addresses. When they overflow, it cant learn new macs and support new connections

### Basic configuration
* enter interface config mode `interface (interface)`
* by default switches are in dynamic auto mode, which deosnt support port security
  * port security only works on access and trunk, both manually configured static
* to start security, do `switchport port-security`
  * default violation mode is shutdown. Unauthorized connections trigger shutdown of interface
    * to re-enable a port, first disconnect the unauthorized device
    * then shutdown, and no shutdown the interface
  * also displays mac address limits

### Err Disable State
* security isnt the only reason devices enter this state
* you have hte option to set up automatic re-enabling of interfaces when they go down for select reasons
* when configured, the port will go back up after 5 minutes
* to enable the auto recovery, do `errdisable recovery cause (cause)`
* to change time interval for recovery, do `errdisable recovery interval (time in seconds)`
* too see cuases, do `show errdisable recovery`
* this is useless if you dont also disconnect the device that caused the errdisable. Otherwise it just loops

### violation modes
* determines what to do if unauthorized access is detected on an interface
* shutdown
  * shuts down port
  * generate syslog and SNMP message
  * violation counter set to 1 as long as interface is disabled
* restrict
  * the switch discards traffic from unauthorized mac addresses, but the switch is not disabled
  * generates syslog and SNMP each time detected
  * violation counter increase by 1 every unauth frame
* protect
  * discard traffic
  * no messages
  * silent discard of unauthorized traffic

### More configuration
* to enable security authorizing a specific address, do 
  * `switchport port-security mac-address (mac address)`
* to enable a violation mode, do:
  * `switchport port-security violation (violation mode)`
* secure mac addresses, mac addresses managed by the port-security, can be configured to age out.
  * by default the mac addresses stay alive for 0 mins, forever
  * the default aging type is 'absolute'
    * absolute: after mac address is learned, the aging timer starts and the mac is removed upon expiration, even if the switch is still receiving frames
    * inactivity: same as absolute, but the timer is reset every time a frame is received
    * static: enables aging for all mac addresses, including those manually configured
* to configure mac address aging, do
  * `switchport port-security aging (aging type)`

### Sticky Secure Mac Addresses
* sticky secure mac address learning enabled by 
  * `switchport port-security mac-address sticky`
* when enabled, all dynamically  learned mac addresses will be added to the running config, as if you ran the command
  * `switchprt port-security mac-address sticky (mac)`
* these macs never age out. To write them to NVRAM, however, you must do `write memory`

### MAC address table
* all of these will be added to the mac address table.
  * if the mac address is sticky, it is assigned the type static.
  * otherwise, it gets the type dynamic

## DHCP Snooping
* security service of CISCO devices which helps guard against attacks utilizing DHCP

### What is it?
* Filter DHCP messages received on untrusted ports
* only filters DHCP
* all ports are untrusted by default
  * usually uplink ports are trusted, and downlink ports remain untrusted
    * downlink ports are those closest to the end hosts, pointing toward the end hosts
    * trusted ports, likewise, point away from the end hosts to the network infrastructure
  * messages received by trusted ports arent inspected
  * if the message is received on an untrusted port, DHCP snooping inspects the message. The message is dropped if it is determined to be harmful

### DHCP messages
* when DHCP snooping checks messages, it treats server and client messages differently
* clients are inspected
  * discover
  * request
  * release: no longer need IP
  * decline: decline the IP address offer
* servers are trusted
  * offer
  * ack
  * nak (decline DHCP client request)

### How does it work?
* if the DHCP message is received on a trusted port, forward it as normal
* if received on an untrusted port, inspect and act
  * if it is a DHCP server message, drop it. DHCP servers shoudlnt be on untrusted ports, good sign its someone running a DHCP poisoning attack
  * if a DHCP client message:
    * discover/request: if the source mac and DHCP CHADDR fields match. If they match, forward, else, discard
      * guards against spoofing, sort of, but not really
    * release/decline: check if the packet source IP address and receiving interface match the DHCP snooping binding table. If match, forward, else drop

### DHCP snooping binding table
* when a client leases an IP from server, server makes new entry in DHCP snooping binding table

### DHCP snooping config
* to enable DHCP snooping on switch, `ip dhcp snooping`
* in addition to globally enabling snooping, also must be enabled on each vlan
  * `ip dhcp snooping vlan (vlan number)`
* then usually its good to run `no ip dhcp snooping information option`
  * what is information option? option 82
  * one of many DHCP options (check this out)
  * provides additional info about which DHCP relay agent received client message
  * DHCP relay agents add option 82 to messages forwarded to remote DHCP server
  * with DHCP snooping enabled, cisco will automatically add option 82 even if the swithc isnt a relay agent!
  * untrusted ports also automatically drop option 82 messages, resulting in inconsistent relay information error
  * this command disables the option 82 adding behavior
* then from interface config mode, specify your trusted ports with `ip dhcp snooping trust`
* remember, the interfaces facing the clients should be untrusted!
* to see the binding table, do `show ip dhcp snooping binding`
  * displays lots of information about connected clients

### Rate Limiting
* snooping also can limit the quantity of DHCP messages entering an interface
* if the threshold is exceeded, the port goes into err-disabled mode
* to configure, enter interface config mode
  * `ip dhcp snooping limit rate (number)`
  * the interface will only allow (number) DHCP requests per second
* to re-enable the switchport, we can enable errdisable recovery
  * `errdisable recovery cause dhcp-rate-limit`
* good for protecting against DHCP exhaustion attacks

## Dynamic ARP Inspection, DAI
* security feature of switches which inspects ARP messages
* like dhcp snooping, but for ARP

### Gratuitous ARP
* ARP reply sent without receiving an ARP request
* sent to broadcast mac address
* allows other devices to learn the mac address of the sending device without making an ARP request
* some devices automatically send GARP messages when an interface is enabled, IP/mac address is changed

### DAI
* used to filter ARP messages on untrusted ports
* like with DHCP snooping, downlinks (closest to end host) should be untrusted. Uplinks (closest to network infrastructure) should be trusted
* like DHCP, if the DAI determines that the ARP packet is not allowed, it drops it 

### How it works
* inspects the sender mac and IP fields of all received ARP messages on untrusted ports, then checks there is a matching DHCP snooping binding table entry, and or ARP ACLs
* ARP ACLs can be manually configured to map IP addresses, MAC addresses for DAI to check. Good for non-dhcp devices
* also supports ARP rate limiting
  * remember, DHCP snooping and DAI still use device CPU, so even if messages are dropped, if the switch is overwhelmed with either such message, ti will break the CPU

### Config
* to enable DAI on a vlan, do `ip arp inspection vlan (vlan number)`
* confiugre the ports you want to be trusted with. All are untrusted by default
  * `ip arp inspection trust`
* DAI rate limiting is enabled by default on untrusted ports, at 15 packets per interval
* you can also specify burst interval, this specifies the interval over which packet quantities are measured. This is 1 second by default

### DAI Optional checks
* check destination mac address, ip address, and source mac
  * destination mac: checks mac address against the target mac address in the arp message. INconsistency=drop. dst-mac
  * ip validation: unexpected or inconsistent IP check, dropped if there is invalid IP address, like broadcast address. ip
  * source mac validation: check if source mac of ethernet header is the same as sender mac value of the arp packet. src-mac
  * to configure these optional checks: `ip arp inspection validate (validation types you want, all in one command)`
    * if you run the command multiple times, the checker does not append to the list of checkers. Instead, it overwrites
* to see the DAI logs, do `show ip arp inspection`

## LAN Architectures
* there are standard best practices for network design, but no universal answer usually

### Common Terminology
* Star topology
  * several devices all connect to one central device, making a star shape
* full mesh
  * each device is connected to each other device
* parital mesh
  * some devices are connected, but not all

### Two Tier Campus LAN design
* a lan or multiple lans in a building or close area
* two hierarchical layers
  * access layer
    * end hosts connect here. 
    * QoS marked traffic
    * security services
    * PoE switchports enabled for phones and such
  * distribution layer (aggregation layer)
    * network equipment aggregating connections from access layer switches
    * conects to internet and WAN
* also called 'collapsed core', because
*  it is a simplified version of 3 tier
*  when your network grows however, tier 2 becomes inefficient
   *  since at tier 2, distribution layer switches are in partial or full mesh, the connection # increase for each additional D-Layer switch increases rapidly
   *  to scale large lan networks, add a core layer
   *  if there are more than 3 distribution layers, you should have a core layer

### Three tier lan design
* adds a core layer to the architecture
  * connects distribution layers in large LANs
  * the focus is speed, fast transport
  * no security on this layer to avoid excess CPU use
  * All layer 3 connections, NO STP!!!
  * should maintain connectivity even if devices fail

### Spine leaf architecture
* application centric architecture, ACI
* common datacenter architecture
* datacenters are dedicated area for running large computer systems like servers and network devices
* previously, datacenters used 3 tier architecture when data was north south, client to network
* datacenters need east west communication however, host to host
* virtual servers, cloud, and HPC require greater inter-host communication when large datacenters operate like clusters
* also called Clos architecture

* there are 2 layers, leaf and spine
  * every leaf switch is connected to every spine switch
  * every spine switch is connected to eveery leaf switch
  * spine switches dont connect to other spine switches
  * end hosts only connect to leaf switches
* the path traffic takes is random for load balancing
* each server is separated by the same number of hops, so there is consistent delay between servers
* very extensible 

### SOHO networks
* small office/home office
* no complex needs, all networking functions provided by the home router, or wireless router

* the router is usually:
  * a router
  * switch
  * firewall
  * wireless access point
  * modem

## WAN Architectures
* Wide Area Network
* network that extends over a large geographic area
* connect geographically separate LANs
* while the network nfractructure for LANs focuses on switches, WANS focus on routers and routing

### Leased Lines
* A dedicated physical connection between two sites.
* private connection
* usually managed by an ISP, who provides the actual cable lines from location to location
* there are either serial cables (with PPP or HDLC encapsulation) 
* optic fiber cables are becoming more common for WAN leased lines as well
  * these are becoming more popular, as they are faster and longer range

### MPLS
* multi protocol label switching
* similar to internet, MPLS is shared customer infrastructure that allow enterprise WAN
* label switching allows vpns to be created over the MPLS infrastructure by use of labels
  * this allows different data to be identified to different customers, so it doesnt get mixed up and goes to the right place

#### MPLS Infrastructure
* CE router: customer edge router
  * customer infrastructure connected to ISP
* PE router: provider edge router
  * ISP infrastructure directly connected to customer
* P router: provider core router
  * internal infrastructure of ISP network infrastructure
* when the PE router receive frames from CE routers, they add a label to the frame, identifying where it came from
* these labels replace the IP for determining the destination of the frames
* CEs do not use the MPLS, only PE/P routers do

##### Layer 3 MPLS VPN
* when using a layer 3 MPLS VPN, the CE and PE routers connect using a routing protocol like OSPF to share route information
* MPLS uses labels for forwarding instead of IPs

##### Layer 2 MPLS VPN
* At layer 2, CE routers directly connect without connecting to PE and P routers. all CE routers in the same WAN are directly connected
  * the wan interfaces are also in the same subnet
* if routing protocol used, routers peer with each other directly
* basically, the ISP operates like a big switch

### MPLS hardware
* many technologies are used for these mpls connect9on
  * wireless 4g 5g 
  * ethernet
  * cable tv
  * serial
* whichever they use, all can communicate if part of the same MPLS VPN

### WAN over internet
* sending important data over the internet unprotected is a bad idea
* to establish secure connection, the company uses VPN tunnels from site to site. This encrypts data being transmitted
* this allows secure communications over the internet

### Connecting to the internet
* private leased lines
* mpls vpns
* although these are private, they can access the public network
* CATV and DSL, used by homes, can also be used in enterprise situations
* fiberoptics are taking over also

### DSL
* digital subscriber line
* internet connectivity via phone lines, sharing phone lines already in homes
* DSL modem is required to convert data to phone line compatible data
  * this might be a separate device, or part of the home router

### Cable
* Similar to DSL in operation
* uses cable television lines for internet access
* requries modem for data format conversion

### Redundant Internet Connections
* for big enterprises having backups is a good idea
* one connection to one ISP is single homes
  * no redundancy
* two connections to 1 isp is dual homes
  * better
* one connection to 2 isps multihomes
  * good if one ISP goes down
* two connections to 2 ISPs dual multihomed
  * best redundancy

### Topologies
* one common topology is hub and spoke. Same thing as star in LANS. 
  * allows a central source to govern traffic flow
  * all traffic must go through the hub

### Internet VPNs
* when using the internet for WAN, no built in security
* VPN provide good security over shared internet connection

#### Site 2 Site VPN
* used IPsec
* VPN between two devices for connecting devices over internet
* in site to site vpn, tunnel created by encapsulating original IP packet with VPN header and new IP header
* this original packet is encrypted before being encapsulated (when using ipsec)

1. unencrypted data is encrypted alongside a session key at source router
2. new VPN and IP headers added.
3. send the data over internet
4. destination router decrypts data

##### Limitations
* no broadcast or multicast traffic, since IPSec (site 2 site vpns) support only unicast
  * OSPF and such cant be used
  * solved by GRE over IPsec
* also, configuring a mesh of tunnels is hard
  * solved by DMVPN

#### GRE over IPsec
* generic routing encapsulation creates tunnels, with no encryption
* can encapsulate many layer 3 protocols along with broadcast and multicast
* flexibility + security = GRE over IPsec
  * GRE packet created much like IPsec, with GRE header and IP header
  * then the data is encrypted, and it receives another header, IPsec and another ip header

#### DMVPN
* removes need for full mesh IPsec tunnels
* allows routers to denyamically route tunnels
1. configure IPsec tunnels to a hub site
2. hub router gives each router information on how to forma n IPsec tunnel with the other routers
* config simplicity of spoke to spoke architecture with the interconnectivity of full mesh

### Remote Access VPNs
* while site to site VPNs are used to make point to point connection between two sites, remote VPNs allow any end device to access internal resources security
* relies on TLS, transport alyer security
* provides the security for HTTPS
* formerly SSL
* VPN client software is installed on end devices for employees working from home
* such ned devices for tunnels to company routers and firewalls, accessing resources

### Comparison
* site to site use IPsec while remote VPNs use TLS
* site to site provide service to many devices between connected networks. Remote access VPNs provide service to one end device
* site to site VPNs are for more permanent connections. Remote access VPNs are usually for on demand access  
* 

## Virtualization and Cloud
### Server Hardware
* Dell, EMC, HP, IBM
* how do servers work?
  * before virtualization, each server had one OS running
  * on top of the OS is the app layer, which runs jobs

### Virtualization
* with virtualization, multiple OS' can run on a single hardware unit
* thus multiple services, which would otherwise be delegated to separate hardware can operate separately in VMs
* these are all managed by the hypervisor, or VMM (virtual machine monitor)
* 2 types of hypervisor
  * type 1 hypervisor: runs directly on top of the hardware, bare metal, native hypervisors
    * efficient, since it runs on hardware and doesnt take as many resources
  * type 2 hypervisor: runs on top of a host OS
    * vmware on a laptop
    * the hypervisor has to communicate with the hardware through the host OS
    * the hypervisor acts as an app, running guest OS'
    * hosted hypervisor
    * not used in datacenters

### Why virtualization?
* partitioning: multiple OSs on one physical machine, dividing physical resources
  * no hardware underuse
* isolation: there is separation of concerns, so problems on one service dont bring all services down
* encapsulation: save the state of VM to files, copy and paste VM images
* hardware independent: no matter what vm you have, as long as the hypervisor works on your hardware, the VM will work
* much easier to set up a new vm than buy a new physical server and set it up

### VM networking
* VMs are connected to one another via a virtual switch
* this is usually provided by the hypervisor
* just like  aregular switch, vSwitch interfaces can operate in access or trunk port mode, and use vlans to spearate the VMs
* interfaces on the virtual switch connect to physical network interface cards, NICs to connect with the outside network
* to facilitate this, a local NAT is also set up

### Cloud Services
* traditionally all network infrastructure was stored on premises
* alternatively, datacenters could rent out physical space and infrastructure to companies. Companies must still do all the switches, but servers and such are held by the datacenter
* cloud provides an alternative to both

### Cloud Computing
* SP 800-145 by NIST says it is:
  * convenient on demand access to shared pool of configurable computing resources which can be quickly released with low effort.
  * depends on 5 essential characteristcs, 3 service models, 4 deployment models

#### 5 essential characteristics of cloud computing
* on demand self service
  * a consumer can provision computing capabilities as needed automatically without human interaction will all service providers.
  * the user can interact with the cloud resources using a web portal, through which payment and config is handled
* broad network access
  * capabilities are available over standard network connections and can be interfaced with any device that connects with such networks
* resource pooling
  * resources are pooled to serve multiple consumers, a pool from which resources are dynamically assigned to customers as needed
  * location independence, no user control over location of actual resouorces. 
  * resources: storage, processing, memory, network bandwidth
* rapid elasticity:
  * customers can quickly expand or scale back from the resource pool with little difficulty or limit
* measured service
  * cloud systems optimize resoure use by measuring resource use.
  * the provider and customer have access to usage analytics. Both user and provider know how much is being used and how much it costs

#### 3 service models
* all is provided on a service model
* SaaS: software a as a service
  * use provider's applications running on cloud infrastructure
  * microsoft office 365
  * provider is in control of everything. They are only providing you an application that runs on the cloud
* PaaS: platform as a service
  * the user can deploy their own applications onto a cloud hosted platform
  * AWS lambda, google app engine
* IaaS: Infrastructure as a service
  * the provider only provides the hardware
  * the user can deploy and run software, like OSs and applications
  * storage is also user controlled
  * Amazon EC2, google compute engine
  * most customer control

#### 4 deployment modes of cloud
* private cloud
  * infrastructure provisioned for exclusive use by single organization
  * large enterprises
  * cloud private, still maybe owned by third party
  * AWS provides infrastructure for DoD
  * on or off premises
* community cloud
  * cloud infrastructure is provisioned for a sepcific community made up of groups with similar goals or missions
  * least common deployment
  * infrastructure reserved for use by only specific organizations 
* public cloud
  * provisioned for use by the general public
  * may be owned managed and operated by central organization
  * Azure, AWS, etc
* hybrid cloud
  * composite of different cloud infrastructures, community + public
  * any combination of the 3 other types
  * private cloud that can make use of public cloud resources when necessary

### Benefits of cloud
* cost: Much lower capital expenses than buying hardware
  * replaced by operating expenses
* scalability: very easy to scale globally, and spread service globally
* agility: easy to modify resource consumption
* productivity: no need to setup or install physical systems
* reliability: backups in the cloud are very easy to perform. Data can be mirrored at multiple sites

Most companies use a combination of on premises equipment and cloud systems

### How does enterprise connect to the cloud?
* private WAN 
* internet (cheapest, least secure)
* IPsec VPN tunnel

## Containers
* similar to VMs

### What is a container?
* application containing all of the dependencies and binaries for the app to run
* multiple apps can run on one container, but usually one container per app
* containers are light weight, good for single application virtualization
  * VMs run an os in each VM, containers dont
* containers run on the container engine
  * container engine is run on a host os, usually linux
* we also have container orchestators, software for automating container management and deployment
  * for microservice apps that might have thousands of containers working together

### VM vs containers
* containers boot up fast, and recover fast from problems
* vms take a lot of space, containers dont
* vms use more cpu and ram than containers
* containers are even more portable, smaller, faster.
* VMs are isolated. Issue on one OS wont affect other VM
  * all containers run on one OS
  * this provides security benefits for VMs

## VRF
* virtual routing and forwarding
* allows division of one physical router to multiple virtual routers
* like VLANs, for routers

### What is it?
* divide a single router to multiple virtual routers
* separation of concerns between mutliple groups of clients, using one hardware unit
* traffic cant be forwarded between VRFs
  * with exception of VRF leaking which allows some traffic to be forwarded out of mismatched ports
* this is because each virtual router has its own routing table

### Why?
* used to facilitate MPLS, remember how service providers allow many customers to share infrastructure? 
* we are using VRF lite though, no mpls
  * each customer connects to their own virtual router
  * VRF is a major cost saver
* without VRF, two interfaces on the same router cannot be in the same subnet
  * VRF effectively allows for local IP reuse

### Configuration
1. `ip vrf (vrf name)` to create vrf
2. `show ip vrf` lists vrfs
3. next, assign interfaces
   1. enter interface config mode
   2. `ip vrf forwarding (vrf name)`
4. configure subnets on the interfaces
5. to see a vrf routing table, `show ip route vrf (vrf name)`

* each vrf has interfaces. Interfaces in the same VRF can forward data out of one another
* additionally, not all interfaces have to be in a vrf

## Wireless Fundamentals 
### Radio Frequency
* assigned frequency ranges
* for wireless networks, the frequency range is called wifi
  * "wireless lan"

### Wireless Networks
* Focus is on WiFi in the CCNA
* the standards defined in IEEE 802.11
* Wi-Fi is a trademark of the WiFi alliance
  * tests equipment to 802.11 standards compliance to certify they are interoperable with other wifi devices

#### Issues
* wireless networks have some issues
* all devices within range receive all frames. There is no such thing as a directed wireless signal, wireless lan antennas are omnidirectional
* this is the same problem as ethernet hubs
  * collisions of data
* privacy of data is alsoa  greater concern since all networks are broadcast
* encryption on a wireless network is essential since anyone sitting near the network can pick up its signals
* as for data collision, CSMA/CA (carrier sense multiple access with collision avoidance) allows half duplex communication.
  * avoid collisions before they occur
  * wait for other devices to stop transmitting before it transmits data itself

* wireless communication are regulated by international and national bodies
  * different countries demarcate different frequencies differently

* with wireless connections, not only wire lenght matters
  * signal range and integrity
  * absorption, reflection, refraction, diffraction, and scattering (electromagnetism, if you know you know) interfere with wireless signals
  * multiple devices using the same channels cause interference

### Radio Frequency
* to send wireless signals, sender applies alternating current to an antenna
  * this creates electromagnetic field which propogates as a wave
* wireless is limited to a few small frequency bands
  * UHF and SHF bands
  * 2.4gHz band
    * 2.4-2.4835 ghz
  * 5gHz band
    * 5.150 to 5.825 ghz
  * in future, wifi 6 will have a range in the 6ghz range
* each band is divided up into several channels
  * devices are configured to transmit and receive traffic on one or more of these channels

### Channels
* the 2.4 ghz band is divided into many channels, each with a 22MHz range
* some channels overlap, so we must choose what channels to use for different access points
* for SOHO wireless networks this isnt a problem, there is only one AP (access point)
* in larger WLANs (wireless lans), adjacent APs using the same channel will interfere
  * this reduces performance
* in the 2.4 ghz band its recommended to use the 1,6, and 11 channels. These dont overlap at all. Remember this
* as for the 5GHz band, channels do not overlap at all!!
* in addition, you must take into account the placement of your APs. See the image for wireless arrangements

### Standards
* much like wired connections, different versions of the wireless standards have different data throughput

1. 802.11: 2.4 ghz, 2mbps
2. 802.11b: 2.4 ghz, 11mbps
3. 802.11a: 5 ghz, 54 mbps
4. 802.11g: 2.4 ghz, 54 mbps
5. 802.11n: 2.4/5 ghz, 600 mbps 'Wifi 4'
6. 802.11ac: 5 ghz, 6.93 gbps, 'WiFi 5'
7. 802.11ax: 2.4/5/6 ghz, 25 gbps, 'wifi 6

* note that the data rates are theoretical, not absolute
* some devides support one, some or all of these standards

### Service Sets
* 802.11 enumerates different service sets, groups of wireless network devices
  * independent
  * infrastructure
  * or mesh
* all in the same service set share the same SSID, service set identifier
  * a name which identifies the service set
  * not necessarily unique, but better to be unique
  * this is the name of a wireless network

#### IBSS
* independent basic service set: wireless network in which two or more wireless devices connect without using an access pont
* 'ad hoc' network
* airdrop
* not scalable, suitable only for quick file transfers

#### BSS
* basic service set
* infrastructure in which clients connect via an AP, not directly to one another
* the AP serves as a wireless switch
* the BSSID, basic service set id identifies the AP. The mac address of the AP radio
* other APs can use the same SSID but not the same BSSID
* wireless devices request to 'associate' with the BSS
  * the wireless devices associated with the BSS are stations/clients
  * BSA (basic service area) is the area in which the signal is usable
* traffic MUST flow through the AP, not go direct

### ESS
* extended service set
* when one BSS isnt enough, and there must be wireless signal over a large physical area
* in this architecture, several BSSs operate in a network, all connected by wire to a switch
  * Each BSS uses the same SSID
  * each BSS has a unique BSSID
  * each BSS used a different channel
* the goal of the BSS is to use several APs to extend range, while making it seem like you are on the same network all the time
* this is how on large campuses you can go anywhere, and still connect to the same wifi
* roaming is when the client/station can move between these APs seemlessly
  * to support seemless transition, BSAs should overlap by 10-15%

### MBSS
* mesh basic service set
* difficult to run an ethernet connection using every AP
* each AP uses two radios, one which connects to stations/clients, and one to form the mesh connection to other APs wirelessly
* at least one switch is connected by wire to a router, the RAP, route access point
* other routers connected in the mesh are MAPs, mesh access points

### Distribution system
* ost wireless services arent standalone network, but are a way for clients to connect to the wired infrastructure without actually using a cable
* this wired network is the DS, distribition system
* each BSS or ESS is mapped to a VLAN in the wired network
* a single AP can also provide multiple unique SSID WLANs. Think an employee wifi and a guest wifi on the same AP.
  * basically, WVLANs
  * each WLAN mapped to a VLAN, connected to wired network by trunk
* each WVLAN also uses a unique BSSID, incrementing the last digit of the physical BSSID by one

### AP Operational modes
* APs operate in modes
* an AP repeater will extendthe range of another AP
  * in the case of a single radio AP, both the repeater connection and the repeater's BSS operate on the same channel, reducing data througput
    * every additional level of repetitiion, throughput reduces by 50%
  * all this is avoided with 2 radio APs though
* workgroup bridge
  * allows a connection for wire only devices to the wireless network
  * a device with a wired connection to a WGB can connect to the wireless AP, even if it has no wireless NIC
  * uWGB
    * universal WGB, allows one device to connect to wireless network
  * WGB
    * cisco proprietary version allowing multiple wired clients to bridge to wireless AP using one bridge
* Outdoor Bridge
  * long range wifi connections using directed antenna dishes, focusing signal strength
  * allows long distance connection in one direction

## Wireless Architectures
### 802.11 Messages
* WLANs communication differs from standard ethernet 
* 802.11 frames are significantly more complex than ethernet and IP headers
  * many more fields

#### Frame fields
* FC frame control: information such as message type and subtype
* duration/id: identifier showing
  * time (microseconds) the channel will dedicate to sending the frame
  * ID for association (connection)
* addresses
  * up to 4 in one frame
  * which ones are present depends on the frame type
  * DA: destionation address
  * SA: source address, original sender
  * RA: immediate recipient of the frame (the AP probably)
  * TA: immediate sender of the frame (again, AP probably)
* sequence control
  * re-assemble fragments and eliminate duplicate frames
* QoS control: prioritize some traffic
* HT: High throughput operations
  * last field of the header
* after this is the frame body
* finally, the trailer is the FCS, frame check sequence, find errors in the frame
  
### Association process
* access point bridge traffic between wireless stations and other devices
* for station to send traffic through AP, it must associate with that AP
* 3 AP connection states
  * not authenticated & associated
  * authenticated, not associated
  * authenticated and associated
* station must be auth and ass. to the AP to send traffic through it

the process:
1. station/client sends the probe request to find out what APs are available
   1. active scan: send request and wait for response
   2. passive scan: listen to AP beacon messages
2. AP sends probe response to say its available
3. station sends password to the AP
4. AP authenticates it if the password is correct
5. station sends association request
6. AP sends association response

now the station can send traffic through the AP

### Message types 802.11
* management: manage the BSS
  * beacons
  * probes
  * authentication
  * association
* control: control acccess to radio. assist with deliviery of management and data
  * RTS (request to send)
  * CTS (clear to send)
  * ACK
* data: actual data packets

### AP deployments
#### Autonomous APs
* self contained, not relying on WLC (wireless lan controller)
* configured individually by cable, cli, http, or gui
* this is fine for small networks, but not efficient in large networks
* for this kind of config, you must confiugre an IP to connect to for management
* the RF parameters are also to be configured. Power, channel
* security policies are per AP
* QoS are per AP
* no central monitoring or management
* config:
  * each AP should have a trunk port connection
  * data traffic has a direct path to wired networks or to other wireless clients
* why else is this bad?
  * large broadcast domains, since each AP has its own VLAN and these extend across the entire network
  * spanning tree will disable links (avoid STP as much as possible)
  * managing vlans is hard

#### Lightweight APs
* function of AP can be somewhat delegated to the WLC, wireless lan controller
* Lightweight APs handle real time operations, transmission, cryptography, and beacons/probes
* other functions carried by WLC
  * RF management
  * security/QoS management
  * client auth
  * client association management
* split MAC architecture, functions split between AP and WLC
* WLC is used for central configuration, so all AP can be configured at once. Very nice!!!
* can be located in the same VLAN and subnet or a different one
* WLC and APs authenticate to one another using digital certs, so an attacker cant maliciously attach their own AP in the network to mess with traffic
* this relationship relies on the CAPWAP protocol
  * Control and Provisioning of Wirelesss Access Points
  * based on LWAPP, lightweight access poiint protocol
* for communications, two tunnels are formed between the AP and WLC
  * Control tunnel: UDP 5246. Config the APs, control ops, all traffic encrypted
  * Data Tunnel: UDP 5247. All traffic from wireless clients is sent through this tunnel to the WLC by wire. 
    * Until it goes through the WLC by the tunnel, it cannot go to the wired network!
    * encapsiulated with new headers, like vpn tunnelling
    * this traffic isnt encrypted by default, but can be configured to be with DTLS, datagram transport layer security
* since all traffic is tunneled directly to the WLC with CAPWAP, the switchports are in access mode, not trunk mode
  * this is because instead of each SSID on the AP being mapped to a VLAN, the vlan mapping happens on the wlc instead
* the wlc on the other hand must be connected to the wire network by a trunk link
* lightweight APs have different modes
  * local: the AP offers a BSS for clients to associate with (default)
  * flexconnect: AP also offers BSS. Allows the AP switch wireless and wired traffic on the network if the connectivity to the WLC is lost. Good redundancy
  * sniffer: the ap doesnt offer a BSS. Dedicated to capturing 802.11 to send to another device for analysis
  * monitor: the AP doesnt do BSS. Dedicated to receiving frames to detect rogue devices. If rogue is found, the monitor tells the AP to send de-auth messages to get rid of the rogue
  * rogue detector: AP doesnt use radio, listens to traffic on the wired network and gets a list of potentially rogue clients and AP mac addresses. By listening to ARP onthe network it can detect rogues
  * SE connect: AP dedicated to analyzing RF spectrum. HElps find sources of interference
  * bridge/mesh: like outdoor bridge mode, configures lightweight AP as a bdirge between sites over long distance. Mesh can be made between access points
  * flex plus bridge: adds flex connect functions to bridge connect
    * allow forwarding of traffic in a bridge mesh architecture even if the WLC dies

#### Cloud Based
* middle ground between autonomous and split mac/lightweight
* centrally managed in the cloud
* cisco meraki is popular cloud b ased wifi solution
* meraki dashboard can be used to configure APs, montior network, generate reports
* regular data isnt sent to the cloud. Sent directly to the network like with atuonomous APs
* only management information is operated in the cloud

### WLC deployment models
* four main deployment methods
  * unified: WLC is a hardware device at a central network location
    * supports 6000 APs
    * good for large enterprise, or large campus
    * if you need more APS, just double the WLCs
  * cloud based: wlc is a VM running on server on a private cloud in a data center
    * not the same as the cloud based AP architecture
    * the WLC is on the cloud
    * supports about 3000 aps
  * embedded: WLC is integrated within a switch
    * good for about 200 APs. 
    * smaller networks
  * mobility express: WLC is integrated within an AP
    * about 100 APs
    * suitable for small branch office, or something

## Wireless Security
802.11x
* security is important everywhere
* most essential in wireeless networks though. Any device in range of the signal can receive the signal
* in wired networks, traffic is usually only encrypted when sent over untrusted netwokrs like the internet
* in wireless, very important to encryp ttraffic sent between wirless clients and the AP
* Authentication
  * all clients must be authenticated to associate with AP 
    * verify identity of user and device
    * only trusted users and devices on the network!
    * separate ssid for guests can be provided
  * clients should also authenticate the AP to avoid associating with maliciious APs
  * passwords, usernames, certificates
* encryption
  * traffic sent between clients and APs should be encrypted so it can only be read by client and AP
  * clients must use same encryption protocol on network, so they can communicate
  * each device has its own key
    * also group key used so AP can send traffic to all clients
    * all clients keep this key
* integrity
  * message must not be modified by third party in transit!
  * message integrity check, MIC is added to messages to help protect integrity
  * how?
    1. sender calculates a mic for the receiver, and attaches this to the message
    2. receiver receives and calculates a new MIC using the same protocol. If the MICs dont match, the receiver drops the message
  * the mic identifies tampering, its like a checksum to software!

### Authentication methods
all these are 802.11x auth methods
* Open Authentication
  * client sends auth request and AP accepts it. No credentials
  * not secure, because no security exists
  * after authentication and association, the user might have to authenticate via other methods to access the network
  * this is guest wifi usually
* WEP: Wired equivalent privacy
  * wired equivalent privacy provide aut and encryption of wireless traffic
  * uses RC4 encryption
  * requires shared key between clients
  * WEP kes can be 40 or 104 bits in length
  * keys combined with 24 bit IV (initialization vector) to bring total length to 64 or 128 bits
  * longer key is usually more secure
  * WEP is not secure, not modern!!
  * authentication side:
    * AP sends a challenge phrase, series of bits
    * client encrypts the challenge phrase and sends it back
    * AP compares client encrypted challenge with AP encrypted challenge
    * this isjust testing that the client knows the AP key
* EAP: extensible authentication protocol
  * framework on which other auth is based
  * defines auth functions used by the below
  * uses 802.11x, port based access control
    * limit network access for clients until authenticate
    * 3 entities
      * supplicant: device requesting connection
      * authenticator: device providing access to network
      * AS (auth server) receives client credentials and permits/denies them (radius server of sorts)
      * steps:
        1. open auth to associate with authenticator. NO access to network except to interface with the authentication server
        2. authentication server decides if the supplicant can access network
        3. the authenticator is a middleman, this is the AP usually
* LEAP: lightweight EAP
  * clients must provide username and password for auth
  * challenge phrase sent by both the client and authentication server
    * basically bidirectional version of WEP with username and password auth
  * dynamic wep keys: wep keys change frequently and automatically
  * this is also vulnerable nowadays though
* EAP-FAST: EAP flexible authentication via secure tunneling
  * 3 phases
    1.  PAC (protected access credential) created and sent from server to client
        1.  shared key
    2. establish secure TLS tunnel between client and authentication server
    3. client is authed in the TLS tunnel
* PEAP: protected EAP
  * tls tunnel like EAP fast
  * instead of PAC, the server has a digital cert
  * cert also used to establish the tunnel
  * client must still authenticate after tunnel formation
    * MS-CHAP, microsoft challeng handshake auth protocol
* EAP-TLS: EAP TLS
  * requires a certificate from the server and client
  * most secure auth method
  * hardest to implement since all clients need a cert
  * TLS is still used to exchange encryption information, but it is not for authentication

### Encryption
* TKIP
  * temporal key integrity protocol
  * solve wep vulnerabilities using hardware designed specifically for wep
  * temporary solution
  * adds security features
    * MIC added 
    * key mixing for unique wep key every frame
    * initialization vector doubled in size to make bruting difficult
    * MIC includes source mac
    * timestamp added to MIC to prevent replay attacks <- research this
    * TKIP sequence number to track sent frames, protect against replay
  * used in WPA1
* CCMP
  * counter CBC mac protocol
  * MAC is message authentication code
  * more secure
  * used with WPA2
  * must be supported by hardware
  * encryption:
    * AES counter mode
      * most secure symmetric encryption method
    * CBC-MAC cipher block chaining message authentication code
      * advanced sorta MIC
* GCMP
  * Galois counter mode protocol
  * more secure and efficient
  * higher data throughput than previous
  * used in wpa3
  * AES counter mode
  * GMAC:
    * superior MIC to CBC-MAC

### WPA
* wifi alliance developed WPA, wifi protected access to standardize all these confusing security measures
* for certification under WPA, it must be tested in wifi alliance testing labs
* support 2 auth modes
  * personal mode
    * PSK: pre shared keys
      * when connected to home wifi, if you enter the password you are authenticated
      * the PSk isnt sent over network, but instead used in a 4 way handshake workflow for encryption key generation
    * Enterprise mode: 802.1X with auth server (radius server, remote authentication dial in user service) 
      * all EAP methods supported
* after wep proven vulnerable
  * WPA:
    * TKIP
    * 802.11x auth
  * WPA2
    * CCMP
    * 802.1x or PSK
  * WPA3
    * GCMP
    * 802.1X auth or PSK
    * other security features
      * PMF: protected management frames
        * no management forging for WLC management
      * SAE: simultaneous authentication of equals
        * protects four way handshake
      * forward secrecy: prevents data being decrypted after transmitted over the air
* basically WPA standards package security methods into simpler sets

## Wireless Config
* oh boy, this will be a long one...
* we will use GUI for wireless config!

### Network topology
* WLC connects to a switch using static etherchannel, referred to as LAG

### Configuration
#### Switch
* create VLANs
* configure the ports connecting to APs as access ports

#### router
* DHCP
* subnets
* configure as NTP server

#### WLC
* first must connect to console port to configure GUI
* just let the wizard run the course
* virtual gateway IP: IP used when communicating with wireless clients
* multicast IP address for forwadding traffic through APs
* mobility/group name is for identifying WLC groups, so they work together
* nnote: when entering a country code, you must select a coutnry code under the jurisdiction of the regulatory domain of the AP
* make sure the management VLAN for the wlc is configured on the entwork to connect to and configure it with the GUI

##### WLC GUI Config
* when connected to the management vlan on the network, go to the IP address of the WLC in the browser
* login with configured password
* controller tab
  * interfaces
    * see the logical WLC interfaces, connecting to the APs
    * wlc ports are physical ports
      * service port: out of band management, to keep management traffic out of the data traffic
        * must connect to switch access port
        * recovery, management, etc
      * distriution system port
        * standard network port that connects to the DS, wired network
        * switch trunk port
      * Console port
      * redundancy port
        * connect for HA, high availability pair
    * wlc interfaces are logical ports
      * management interface: for maangement traffic. Telnet, ssh, http/s, radius, etc etc. These have CAPWAP tunnels
      * redundancy managmeent interface: with an HA connection between two WLC, one WLC is on standby, the other is active. This interface allows for management of the standby wlc
      * virtual interface: used for relaying DHCP requests, web auth to clients
      * service port interface: out of band management bound to service port
      * dynamic interface: map WLAN to VLAN.
        * traffic to internal WLAN sent to wired network from WLC internal dynamic interface 
* to add dynamic interfaces:
* controller tab
  * click 'new'
    * internal WLAN, map to vlan number. Enter name also.
      * enter all the network information, DHCP address, subnet, etc
      * apply

* configure WLANs
* wlan tab
  * for SOHO, use PSK security (layer 2 sec tab)
    * must enter the PSK key manually
  * in layer 3 security, you can configure:
    * web authentication: for open authentication
    * passthrough: no authentication except accepting ToS
  * map wlans to internal dynamic interface
  * also AAA servers, for RADIUS setup
  * QoS
    * control what quality is delegated to the wireless traffic
    * QoS setting: best effort by default
    * platinum: voice
    * gold: video
    * bronze: background

* wireless tab has configuration management for the APs
* management: summary of management settings

## intro to network automation
### network automation
* the traditional model of network management is diluted by automation
* traditionally, individual devices managed one by one
  * typos and mistakes are a problem in big networks if you have to configure a bunch of devices manually
  * time consuming, inefficient
* automation facilitates scalability, easy network wide changes, troubleshooting
* network wide policy compliance, software updates
* fewer man hours per task
* automation methods:
  * python scripts
  * SDN (software defined networking)
  * puppet
  * ansible

### The 3 planes of the newtork
* traditionally every device has its own plane. In SDN, planes are centralized
* data/forwarding
  * all user data transmitted from one client to another is in the data plane
  * routing, packet examination, forwarding, ACLs, and NAT all exist in this plane
  * relies on ASIC instead of CPU for higher speed for forwarding
  * Also uses stuff like TCAM (ternary content addressable memory) for high speed memory
  * data plane work on the devices is much closer to the hardware!
* control
  * how does the router know where to send things?
  * arp table, mac table, STP, routing table
  * operations to build these tables
  * controls what data plane does
  * Overhead operations
    * OSPF doesnt send and receive packets, but informs the data plane where routing options are available
* management
  * overhead work
  * doesnt directly affect normal traffic
  * manage devices
  * SSH, telnet, syslog, SNMP, NTP

### SDN
* software defined networking
* centralizes the networking control plane to a single application, the controller
* SDA (software defined architecture) controller based networking
* traditional planes are distributed
  * each router runs OSPF, finds the best routes, shares information
  * SDN centralizes these things, like route calculations
* controller can interface with network devices using APIs

* in an SDN architecture, the controller runs OSPF, and relates data to the routers
* much more efficient than idividual communication
* this coordination is done with the `southbound` interface, a software interface

* some architectures centralize only some of the control plane

#### Southbound interface
* sbi used for communications between network devices and the controller
* usually an API
* examples:
  * openflow
  * cisco opflex
  * cisco onepk
  * netconf 

#### Northbound Interface
* using SBI, controller communicates with devices
  * learns about them, and about the network as a whole
* northbound interface allows the devices to interact with the controller and use its resources
* the nortbound interface is usually controlled by an app, and REST api
  * Representation State Transfer
  * communicates via json and xml

### Traditional vs SDN
* in traditional net architecture:
  * python scripts still can be used to run commands on many devices
  * parse through show commands to make things easier to read
* SDN:
  * central control
  * central analytics
  * easier to use
  * 3rd party applications using APIs

## data serialization
* data serialization allows a standard data format
* allows data at the application layer to be put in a format it can be packaged in byte form to be sent over a network

### what is serialization?
* standard format for data to be stored or sent
* data communicated between applications both can understand
  * java and python applications can communicate
* json is basically python lists and dicts
* REST APIs are basically entirely based on json messages

### JSON
* javascript object notation
  * file format/data interchange format
  * can be used to store data AND send data
* rfc8259
* originally for javascript, but now language agnostic
* whitespace insignificant
* 4 primitive datatypes
  * string 
    * text surrounded by double quotes
  * number 
    * an integer, or float
  * boolean
    * true or false
  * null
    * null value, nothing
* 2 structured datatypes
  * object
    * basically a dict
    * surrounded by curly brackets
    * key must be string
  * array
    * just a list of values, no keys

### XML
* extensible markup language
* markup language?
  * format text for HTML
* repurposed for serialization
* less human readable
* whitespace insignificant
* often used in REST
* `<key>value</key>`
* list headers are:
  * `<entry>`
  * `</entry>`

### YAML
* yet another markup language
* yaml aint markup language
* used by ansible
* most human readable
* whitespace significant
* yaml files start with ---
* `-` indicates a list
* keys and values represented as key:value

## REST APIs
* application layer communication
* northbound interface

### CRUD
* create read update and delete
* key API operations and HTTP verbs
* creative operations:
  * create variables and set values
* read
  * get the value of variables
* update
  * change variable values after creation
* delete
  * delete variables

### HTTP
* HTTP methods are classified into these crud operations
* the HTTP verb determines what the receiver will do with your message
* applications usually use HTTP, for its simplicity and wide usage
* create:
  * POST
* read:
  * GET
* update:
  * PUT, PATCH
* delete:
  * DELETE

### HTTP request
* when a client sends a request to server, it includes:
  * http verb
  * URI
      * what resource is the client trying to access?
* additional headers
  * research yourself
* http request
  1. IP header
  2. TCP header
  3. verb
  4. URI
  5. additional headers
  6. data
* REST APIs use HTTP (mostly)

### HTTP Response
* after server receives client message, server returns response
* status code indicating success or failure of request
* 3 digits
  1. class of the response
     1. 1xx informational, continuing to process
        1. 102, received response and processing
     2. 2xx successful, successfully accepted
        1. 200 okay, successful request
        2. 201 created, success, new resource created
     3. 3xx redirection, further action must be taken to complete request
        1. 301 moved permanently (server changed)
     4. 4xx client error, cannot fulfill request
        1. 403 unauthorized
        2. 404 not found
     5. 5xx valid client request, server cannot fulfill though
        1. 500 internal server error
  
### REST APIs
* representational state transfer
* set of rules on how API must operate
* constraints:
  1. uniform interface
  2. client server
     1. client uses API calls to access server resources
     2. separation means both client and server can evolve independently
     3. when client app changes or server app changes, interface will not break
  3. stateless
     1. exchanges are stateless
        1. tcp is stateful, long lives connection
        2. udp is stateless, no connection
        3. rest APIs use TCP, stateful, HTTP isnt stateful
     2. each API exchange is a separate event
     3. independent of all previous requests
     4. servers dont store previous requests
     5. every individual must request must have authentication 
  4. cacheable or non cacheable
     1. must support data caching
     2. store data for future use
     3. quicker response times, reduces server load
     4. all resources neednt be cacheable, but those that are must be identified as such
  5. layered
  6. code on demand (optional)

### Cisco DEVNET
* developer program for IT people write applications for cisco APIs
* teaching resource for development
* there is devnet cert as well
* devnet provides the DNA center, an always allive server, to test API requests
* we can send HTTP requests via postman
* to use:
  1. generate token with post request
     1. specify username and password
     2. if successful, response 200
     3. copy the token
  2. retrieve device inventory with get request
     1. add the token to http header
     2. see all available devices

* scheme of the URI identifies the protocol used

## Software defined networking
* more specifically, SD (software defined) access
* centralize control plane into the controller application
* network devices share information with controller which calculates routes. Routers dont use OSPF anymore to talk to each other!
* controller interacts programmatically using APIs with the rest of the network

### SDN architecture
1. Application layer
   1. apps tell SDN controller what to do
2. control layer
   1. receives and processes instructions
3. infrastructure layer
   1. actual devices in the network

### sd-access
* cisco solution for automating large area LANs
  * ACI (application centric infrastructure) solution for automating data centers (spine leaf)
  * SDWAN is sdn for wan
* cisco DNA
  * controller at the center of SD access
  * intermediary between the applications, and the network
* underlay: underlying network devices providing IP connectivity with IS-IS
  * the switches
* overlay: virtual network on top of physical underlay
  * sdaccess uses VXLan to build tunnels (virtual extensible lan)
  * all data in virtual network is sent using these tunnels
* the fabric is combination of overlay/underlay, all the network as a whole

### underlay
* the underlay provides the infrastructure for VXLAN tunnels
* different roles for switches in sdaccess
  * edge nodes: connect to hosts
  * border nodes: connect to exterior devices
  * control nodes: uses LISP (locator id separation protocol) to perform control functions
* you can add sdaccess to existing network if supported by hardware.
* this is a brownfield deployment
* ideally youll do a greenfield (new) deployment
  * all switches should be layer 3
  * routed using ISIS protocol
    * STP and FHRP no longer needed
    * routers are the default gateways
    * every device is routed to one another
  * all links are routed, no STP

### overlay
* LISP provides control plane
  * mappings of endpoint ids (EIDs) to RLOCs (routing locators)
  * EIDs identify the hosts connected to end switches
  * RLOCs identify edge switch to reach the end host with
  * DNS like mapping
* trustsec (CTS) policy control, QoS, security
* VXLAN 
  * tunnel access for SDACCESS
  * data plane of SD-Access
  * basically, a pc can ask a switch how to reach another device
  * then a vxlan tunnel is created between the two devices

### CISCO DNA
* 2 roles
  * SDN controller
  * network manager (when not using SDACCESS)
* DNA center is installed on UCS server
* rest API
* SBI supports netconf, restconf, telnet, ssh, snmp
* dna center enables IBN, intent based networking
  * allow engineers to communicate network intent for behavior, then DNA center will handle the heavy monotonous lifting behind the scenes
  * ACLs can have thousands of entries
    * easy to forget what entries do
    * DNA center allows user to specify policy intent. X cant interact with Y, then the DNA configures it for you
    * the engineer can write comments for policies
* manage network operations, DHCP, DNS, etc
* show inventory of network devices
  * by default, messages are managed
  * you can also see compliancy with network policies
    * if a device isnt updated with new software, it will be listed as non-compliant

### DNA center vs traditional network
* Devices centrally managed and monotored by DNA center
* administrator communicates intended network behavior
* configs are centrally managed along with polkicies
* software versions centrally manages
* network deployments much easier
* lower human error

## Ansible, puppet, chef
* can be useful in any network, but they are just tools
* use the right tool for the job!!

### configuration management, why?
* configuration drift:
  * individual changes over time cause device config to deviate from policies
  * standard configuration allows more seemless operations between devices
  * records often arent kept of individual changes
  * configuration management tools help avoid this
  * with no management tool, configuration files should be stored in a filesystem and compared against a standard set of templates
    * this doesnt guarentee safety though

### config provisioning
* help apply config changes to all devices in the network
* no more individual configuration!
* we might create a json file storing a configuration for a device
* then send this file to all devices we want

### managers
* ansible puppet and chef (that order of popularitgy) were originally developed for large scale VM management
* they now work for distributing configuraitons for networks as well
* check device configurations for compliance with policies
* also supports network automation using scripts

### Ansible
* config management tool owned by redhat
* written in python
* agentless
  * doesnt require special software to host it
* uses SSH to connect to devices and run its course
  * this means its very versatile. Most popular as a result
* push model: the ansible server connects to the devices and push configurations to devices
* Components
  * playbooks: ansible uses playbooks, yaml files for automating tasks. Overview logic and actions
    * YAML
  * inventory: list devices managed by ansible and characteristics of each device
  * templates: device config files
    * jinja2 format YAML
  * variables
    * list variables and values, substituted to templates to complete configs. YAML

* in short, the playbook draws from inventory, templates, and variables to run scripts to interface with network devices

### Puppet
* configuration tool written in ruby
* agent based
  * specific software must be installed to work
  * not all cisco devices support puppet agent
* TCP 8140
* can be run agentless. Proxy agent runs on external hosts, and proxy uses agent to SSH to drvices
* puppet server = puppet master
* pull model: clients connect to server and pull configurations from it
* instead of yaml, uses proprietary language
* text files required:
  * manifest: defines configurations for devices
  * templates: generate manifests

### Chef
* agent based
* ruby
* not all cisco devices support chef agent
* pull model
* TCP 10002 to send configs
* files use DSL domain specific language based on ruby
* files:
  * resources: ingredients in a recipe, configs managed by chef
  * recipes: outline logic and actions of tasks performed
  * cookbooks: sets of related recipes
  * runlist: ordered list of recipes run to bring devices to standard with the policy