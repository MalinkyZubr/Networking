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

note: when people say "layer 2 problem," for instance, they mean with respect to the OSI model


## intro to the CLI
How do you connect to a cisco device to manage it with the CLI? 

1. Connecting to console port, either via rj45 or usb mini-b. Requires a Rollover cable to interface.
   * then you need to open a putty session, which is a terminal emulator. From there you can go to serial to modify settings for the serial connection. By default they are the same as cisco devices
   * Baud rate should be 9600 bits/second. 8 data bits. 1 stop bit. Every 8 bits of data, 1 stop bit is sent to signify the stop of the bits. Parity set to none. Parity is for detecting errors. Flow control controls flow throuhg the device, set to none.
   * When entering the router you are by default in exec mode, singified by {hostname}>. all devices have hostnames. Exec mode is useless basically. Cant make any changes to the device
   * If you enter the 'enable 'command, you go into priveleged exec mode. {hostname}# is priveleged exec mode. Provides complete access to view the devices configuration, restart the device, etc. However you cannot change hte config here, but can change the time and save the config file, etc. To view all commands, do ?. Ifg you want to display all commands that start with a letter, do e? for example
   * to enter global configuration mode, enter "configure terminal"
   * Protect privileged exec mode with a password. "enable password {password}"
   * to see the detailed help for a command, do "enable password ?" for instance. Must have space between command and ? 
   * To show the running configuration file, do show running-config
   * To show the startup config, do show startup-config
   * this will show nothing until we save the running configuration as a config file
   * 3 ways to do this: write, write memory, and copy running-config startup-config. However, when we look at this it displays the password
   * we nee dot do a "service password-encryption" command within configuration terminal mode. The number 7 before the encrypted password means it is using the proprietary encryption. 
   * However, there are cisco password crackers. So this is not secure. There are better passwords with tougher encryption
   * Use the "enable secret {desired password}" this will enable the secrets of cisco
   * in order to run out of level commands in the config mode, use the "do" command. "do show run" for instance
   * how do you cancel a command you executed? do: "no {previous command you want to cancel}"

Commands:
1. enable: enter priveleged exec mode
2. configure terminal: enter global configuration mode
3. enable password {password}: create a password for priveleged exec mode
4. service password-encryption: encrypts all passwords
5. enable secret {password}: makes  a more secure password. If run with password, it is disabled
6. do {priveleged exec level command}: run exec commands from global config mode
7. no {command}: remove a command previously configured
8. show running-config: displays active configuration file
9. show startup-config: displays the saved configuration file which will be loaded if the device is restarted
10. write: saves configuration
11. write memory: saves configuration
12. copy running-config startup-config: saves configuyration
13. hostname {hostname}: chgange hostname

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
* in cisco CLI, arp -a is the same as "show arp". To see the mac-address-table of a cisco device, use "show mac-address-table"
* wireshark is a good way to inspect these procedures

### mac-address-table
* includes
  * vlan
  * mac addresses
  * type (dynamic or static)
  * ports/interfaces
* accessed via "show mac-address-table"

* mac addresses age, after about 5 minutes they are automatically removed to save space
* to clear mac-address-table of dynamic addresses, use "clear mac-address-table dynamic"
* to clear specific address, do " clear mac-address-table dynamic address {mac address}"
* to remove by interface, do "clear mac-address-table dynamic interface (interface)"

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

CLASS          FIRST OCTET      NUMERIC RANGE     PREFIX LENGTH      # hosts
A              0xxxxxxx         1-126            /8                 16777214  
B              10xxxxxx         128-191           /16                65536
C              110xxxxx         192-223           /24                256
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
* "show ip interface brief" 
* displays the ip address for each interface. If unassigned, you can assign it manually
* method indicates how the host was assigned an ip address
* status is the layer 1 status of the interface. Is there a cable connected?. Administratively down means it was disabled with the shutdown command. Cisco router interfaces are admin down by default
* Cisco switches do not behave the same. 
* the protocol field shows the layer 2 status of the interface

#### Set IPV4 Address
* enter configure terminal mode
* interface (ethernet type, like gigabitethernet) (interface #, like 0/0). This enters interface config mode for a specified interface
* to change the address, enter ip address (desired ip address) (subnet mask)
* then enter "no shutdown" to activate the interface 
* when you set an ipv4 address of an interface through a router, it refers to the address of that LAN, not to the address of the router which is the first possible IP address of the network. Hosts adopt the IP address of the LAN they are connected to. You assign an IP to an interface connected to a switch so that other lans can connect and send data to that lan
* if a computer wants to interface with a router through a switch, it will do so using the interface IP

#### more show commands
* "show interfaces (interface)" shows all interface information
* "show interfaces description" shows interface descriptions which can be manually be configured. Good for organization
* to configure an interface description, enter the interface config terminal. Then run: "description ## (description) ##"

note you can manually set ip addresses for pc's in packet tracer it he config menu

## Switch Interfaces
### interfacing
1. enable priveleged exec
2. show ip interface brief
3. Switches do not have shutdown command applied by default. When you connect a device, they will be up up by default (status and protocol up)
4. Switches do not have assigned IPs because they are layer 2 devices. 
5. down down just means no connection. Routers are down by default, switches are not

### interface status
1. "show interfaces status"
2. contains port (interface)
3. name of interface (description)
4. status: shows whether interface is connected
5. vlan: Vlans are for dividing lans into smaller lans. Default is 1. Trunks are connected to other switches
6. duplex: Are the devices capable of sending and receiving data at the same time? Default is auto. Full duplex means they can
7. speed: shows speed of ethernet interface. Remember, in megabits. Auto means they negotiate speed based on fastest speed between devices for connection
8. type: shows type of interface. 10/100BaseTX for instance
   
autonegotiation usually works, but good idea to know manual configuration

### configuring speed and duplex
* enter interface configuration "interface (ethernet type) (interface number)
* speed (# speed based on network capability / auto for auto selection) to change speed
* duplex (auto/full/half) to change duplex status
* description ## (description) ##
* any value that is autonegotiated will have a-(value)
* all of these commands also work on routers

however, it is a security risk to config each individually, so you can configure all of them in groups with range interfacing

* interface range (interface speed) (interface start index) - (interface end index)
* any configuration commands made now will apply to all selected interfaces
* if you want to specify several different ranges, you just do:
* interface range (interface speed) (interface start index) - (interface end index), (interface speed) (interface start index) - (interface end index)

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
* show interfaces (speed and interface)
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
4. now the router has the packet, and it will compare the destination IP to the routing table. Each router has a routing table that stores a list of destinations and routes to those destinations. 
5. if it is already in the routing table, it will send the packet via an interface directly to the router, and via any hops in between the source and destination networks. 
6. The source router forwards the packet to the next router in the route. That router follows the same process as the first router, checks its IP table, and forwards to the next hop in the route. 

at each stage, the router compares the destination IP to its routing table, and ecides whether it needs a hop, or can directly connect to the destination IP network.

### what is the /32?
a /32 mask represents a single specific host on a network, like a PC. A pc on network 192.168.0.0/24 would have an IP of 192.168.0.54/32, but usually we just say 192.168.0.54.

To reiterate, local route is the actual IP address of the interface, and the connected route is the IP the network the interface is a member of

The ip address configured on a router interface will appear as a local route, /32. The IP address you assign the router is relative to the LAN, and thus is local. That is how clients will access the router?
### Managing routes with cisco systems
1. "show ip route" shows the ip routing table. L stands for local network, and C stands for connected network.  
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
* to configure a route, "ip route (destination-address) (mask) (next hop)". I give this packet to you, you deal with the route.
* ip route 0.0.0.0 0.0.0.0 (router interface IP address)
* the next hop will figure out how to get the packet where it needs to go
* ROUTERS WILL DROP PACKETS WITH UNKNOWN DESTINATIONS. THEY WILL NEVER FLOOD
* unless we configure our routes (or do dynamic routing, later), we cannot send packets to unknown destinations, eg dstinations not in the routing table
* How do we get around this? This command: "ip route (destination IP) (mask) (exit-interface). Instead of next hop we specify exit interface. where should we send packets as a route of last resort? to whatever is at the end of the interface. Gateway of last resort is not added however, because this is for specifric networks. But what does this mean? it is technically a direct connection to the destination IP. It is basically saying, "I will give this packet to whatever is connected on this interface, and they will route it where it needs to go". And so, when the packet gets to the router on the connected interface, its own routing will carry out the rest of the work.
* "via" usually refers to interface. Get to network IP via interface IP

there might be a problem however, one way reachability. Source can send packets, but without more static routing, the destination cannot send a reply. 

what does it mean when a router looks for most specific matching route. It looks for the destination with longest prefix length.  

in short, if a router can route to 192.168.4.254 through either 192.0.0.0/8 or 192.168.4/24, it will do soi through the latter, because it is more specific (more network octets)

THIS IS VERY IMPORTANT FOR CCNA TEST

remember, you can use scapy for manual packet crafting