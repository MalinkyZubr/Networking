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

### Chart of CIDR notation
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

### Subnetting trick:

the last octet of a /26 address can be represented as such:

NET  Host
00 | 000000
the value of the last bit in the network portion of the octet is 64. So to find the next subnet's network address, just add 64.

Thus the network addresses of the subnets on this octet are 0, 64, 128, and 192

the same process can be used for class A and B networks

### VSLM
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

what if you want to break up a broadcast domain into several smaller broadcast domains?
if we od this, we can limit access to different segments of that broadcast domain to improve security
lots of unecessary broadcast traffic also reduces network performance

this can all be done with subnets, so where do VLANs come in?

subnets each require their own router interface. Thus, for every subnet, we need an additional connection to the router.
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

process:
1. show vlan brief, shows vlans and their interfaces
2. interface range g1/0,g2/0(example) to enter configuration to configure several interfaces at once
3. then run command switchport mode access to set the interface as an access port. This means that it belongs to a single vlan, and connects to end hosts. This is as opposed to a trunk port, which carries multiple vlans. Good to explicitly specify port type
4. then run switchport access vlan (vlan number). if the select vlan doesnt exzist, it will create the vlan
5. You can also change the default name of a vlan
6. vlan (vlan number) accesses a vlan. You can then do name (name)

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
2. switchport mode trunk
3. if you get a trunk encapsulation error, you must first set encapsulation to 802.1Q to manually change encapsulation type
4. switchport trunk encapsulation dot1q, to set 802.1Q
5. switchport mode trunk (to set the mode to trunk)
6. show interfaces trunk to see trunk interfaces that are trunked
7. switchport trunk allowed vlan 10,30 (tells the switch what vlans to trunk)
8. switchport trunk allowed vlan add 20 (add a vlan to the list of allowed trunk vlans)
9. switchport trunk allowed vlan all
10. switchport trunk allowed vlan except 10 (all vlans except this one)
11. switchport trunk allowed vlan none (no vlans allowed)
12. for security purposes it is best to change the native vlan to an unused vlan. This must match between switches
13. switchport trunk native vlan 1001
14. remember, to make a vlan a trunk, you must create it first

### Router on a stick ROAS
* what is this? A new method of inter-vlan routing
* only one interface connected to the network router for all vlans
* one physical interface to function as multiple. WE are basically making sub interfaces
* first, enable interface with no shutdown
* interface g0/0.(vlan number)
* encapsulation dot1q (vlan number)
* ip address (sub-net sub-interface address) (netmask)
* remember, this needs trunk port on the connected switch, which trunks all vlans

### Using native vlan on a router
#### 2 methods
1. encapsulation dot1q (vlan-id) native, tells the router this is a native vlan, assume untagged frames belong to native vlan. Then assign ip address to the subinterface
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
* do show run to show sub interfaces, and then do show ip interface brief
* get rid of all router subinterfaces using no interface g0/0.x
* then do default interface (interface) to specify default routing interface
* then enter interface configuration mode, and set the ip for the p2p connectio between the multilayer switch and router. The subnet mask should be 255.255.255.252
#### Switch side
* enbable default interface to the router using default interface (interface connected to router)
* enable ip routing using "ip routing" which allows to build IP table. without this intervlan routing wont work
* enter selected interface
* then in the interface, run "no switchport", so that the port becomes a layer 3 routed port
* configure the ip address as you would on any router to correspond with the p2p connection
* then on the switch, set the default route, ip route 0.0.0.0 0.0.0.0 (router ip)
* thyen do show interfaces status, in order to check the interface works

### SVI config
* on the switch
* interface vlan (vlan number)
* assign ip address to the interface like normal, ip adddress x.x.x.x subnetmask
* then run no shutdown to enable the interface
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
* to enable dtp, do switchport mode dynamic auto/desireable when in interface config mode
* In dynamic desireable mode will actively try to form a trunk with other cisco switches. It will form a trunk if connected to another switchport when it is in trunk mode, or dynamic desireable/auto mode. This is DTP negotiation. It will do its best to form a trunk, unless the other switch interface is in access mode, in which case it will autonegotiate to access
* show interfaces (interface) switchport shows the settings for a selected interface switchport
* in dynamic auyto mode, it will not actively try to form a trunk with other switches. However, it will form a trunk if the connected switch port is in trunk mode, or is seeking actively to form a trunk connectiuon. If it encounters another auto mode, it will form an access connection.
* if there is a mode mismatch, the traffic will nto flow
* dtp will not trunk with a router or pc. Trunks for ROAS must be manually configured
* to disable autonegotiation, you can say switchport nonegotiate
* remember, manual configuration is always better for this!

* another feature of DTP is negotiation of encapsulation type. THis is enabled by default
* to set autonegotiation for encapsulation, run switchport trunk encapsulation negotiate
* DTP frames are sent in vlan1 when using isl, or in native vlan when using 802.1q
* if both cisco switches suppoort ISL, isl is preferred, so manual configuration is better
* do this with switchport trunk encapsulation dot1q

### VTPe
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
* to change vtp domain name, do vtp domain cisco
* if vtp switch with null domain receives advertisement, it automatically joins that domain
* if a swith receives a vtp advertisement in the same vtp domain witha higher revision number, it will update its vlan database to match
* danger of VTP: If you connect an old switch with a higher revision number to your network and the vtp domain name mathes, all switches in the domain will sync their vlan databases to that switch, and destroy everything

### VTP Transparent mode
* does not participate in the vtp domain, and does not sync to the database
* maintains its own vlan database in nvram it can add, modify, delete vlans but they wont be advertised omnother switches
* will forward VTP advertisements to other VTP switches, if its in the same domain

### VTP version configuration
* to change vtp version, use vtp version command
* vtp version (1-3)
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
* switches use the one field in the STP BPDU, bridge ID to elect a root bridge. The switch with the lowest bridge id becomes root bridge
* all ports on the root bridge are put in a forwarding state, and other switches on the topology must have a path to reach the root bridge
* traditionally, this takes 2 fields, bridge priority and source mac address
* default bridge priority is 16 bits, and set to 32768. iF all priority fields are equal, whoever has lowest mac address will become root bridge
* in modern stp however, the bridge priority field is extended to comprise of the bridge priority, and extended system id (VLAN ID) in order to support vlan operations
* why does it have a vlan ID? because cisco uses PVST, per vlan spanning tree. Each vlan has its own stp instance, so each vlan has different interfaces which can be forwarding or blocking
* the default rbidge priority is the sum of the vlan ID and the bridge priority. Thus if a switch is in vlan 1, its actual bridge value is 32769. 
* because the last 4 bits comprise the bridge priority, and the extended system id is everything up to 2048, you must increase the total bridge priority by a value of 4096 every increment if you want to change the priority without changing vlan
* valid bridge priority can be between 0 and 61440, at intervals of 4096
* the LOWEST bridge id is the root bridge

### Root switch
* the root switch with the highest bridge priority will have all ports forwarding
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
    * what if two switches have two connections between them? the interface connected to the lowest port id is the root port. TO identify this do "show spanning-tree". STP port id = port priority (def 128) + port number. the NEIGHBOR switch's port id is used to identify root port in this case
3. block ports to prevent layer 2 loops
   * every collision domain has a single STP designated port. Thus on blocked connections, we need to specify the designated port. 
   * to find the designated port:
     * the switch with lowest root cost will make its port designated
     * if the root cost is the same the switch with the lowest bridge id will make its port designated  
     * the other switch will make its port non designated, or blocking

* when you have an STP path that involves intermediate connections through other switches to get to the root bridge, you add up the sum of root connections to get total cost

### STP commands 
* show spanning-tree, show vlan information and vlans
* show spanning-tree vlan (vlan number). Root id shows data about the root, bridge id shows information about the selected bridge
* show spanning-tree detail, more details

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
  * to enable portfast, enter the interface on the switch, and do spanning-tree portfast. This will only work if the port is not in trunking mode
  * portfast can cause loops if network cabling is changed
  * risk to using portfast, but there is an additional method we can use to prevent this

* BPDU Guard
  * if an interface with guard enabled receives a bpdu from a switch, the interface will shut down to prevent a loop from forming
  * to enable, enter interface, then do, spanning-tree bpduguard enable
  * to enable bpduguard by default on portfast, from config mode, do, spanning-tree portfast bpduguard default
  * to enable a port disabled by bpduguard, just do shutdown, then no shutdown to reset the interface.
  * even if it receives a superior bpdu, the port is disabled

* loop guard
  * even if the inhterface stopes receiving bpdus, it will not start forwarding, THe interface will be disabled

### Spanning tree mode
* to change spanning tree mode, do spanning-tree mode (mst/pvst/rapid-pvst)

### Configure root priority
* to make an arbitrary bridge the root bridge
  * spanning-tree vlan (num) root primary/secondary
  * this makes the selected switch have lowest priority 
* we can also have a backup root bridge
* priority configurations only apply in the vlan on which they are configured. This allows spanning tree load balancing
  * if you have several vlans, you can have a different root bridge for different vlans. Thus, different vlans will have different disables interfaces, and will leverage resources more efficiently 

### interface configuration
* to configure cost of an interface, enter the interface conig mode
* spanning-tree vlan (num) cost (cost) to change cost manually
* spanning-tree vlan (num) port-priority (priority num) to change port priority

## Rapid Spanning Tree Protocol
Old spanning tree can take up to 50 seconds to chagne topology. Responds in a few seconds. Default on most devices. CCNA only has RSTP

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
* show etherchannel load-balance
  * this will show which method it uses to determine which physical interface is used to transmit data. 
  * src-dst-ip means it determines this using source and destination ip addresses
  * traffic that flows from one source to one destination will always flow on the same interface
  * what if there is no ip packet or ip address? use mac address
* port-channel load-balance src-dst-mac
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
    * usually avoided, because you want to dynamically manipulate the etherchannel. If one interface fails, then the etherchannel will stop working when statically specified

* with etherchannel, only 8 interfaces max can be used
* to configure etherchannel:
* interface range g0/0,g0/3
  * channel-group (group num) mode (mode)
  * mode can be desirable or auto
    * auto + auto = nothing
    * desireable + anything = etherchannel 
* after you complete the port grouping, you can work on it like you would any single interface
  * interface port-channel (group number) [usually something like po(num)]
  * now you can run any port commands on it, like switchport mode trunk
* interfaces in group need same configrations, like speecd and duplex

* show etherchannel summary

### What about routed ports?
* broadcast storms are no concern on routed switches
* to enable etherchannel on routed switch, enter interface range config
  * no switchport
  * channel-group (num) active 

## Dynamic Routing
* in contrast to static routing. Static routing is manual configuration of routes with the ip route. 
* This involves configuring a dynamic routing protocol. Dynamic, because it isnt fixed

### Types of routes
* network route
  * to a network/subnet (mask length </32>)
  * host route: to a destination with mask length of /32

### Dynamic Routing
* when dynamic routing is enabled, the router connected to the lan address being advertised send out an advertisement, saying
* " this ip can be reached via me "
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
1. router rip, (rip config mode)
2. version 2, (to set to version 2)
3. no auto-summary 
   * auto summary automatically converts networks to classful networks, and advertises those networks as such
   * This is bad, disable it with this command
4. network (network ip)
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
  5. do show ip protocols
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
* router eigrp (autonomous system number), enter router config mode
  * autonomous system number basically is a grouping number. All routers with the same autonomous system number for EIGRP will be able to form an adjacency and share route information 
  * thus routers that want to communicate must have the same number
* no auto-summary
  * same as RIP, always do this to prevent advertisement of classful advertisement
* passive-interface (interface)
  * do this on any interface that has no EIGRP routers connected
* network (ip)
  * activate EIGRP on any interface that matches the IP range
  * command assumes classful, and looks for any IPs that match its network octets 
* we can also do something like 
  * netowrk 172.16.1.0 0.0.0.15
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
* do show ip protocols
* eigrp uses delay and bandwidth by default
* shows router ID as well to identify it within the AS, autonomous system
* Router ID is determined by:
  * manual configuration 
  * highest IP address on a loopback interface (virtual internal interface)
  * highest IP address on a physical interface
  * to change, do :
    * eigrp router-id (ip address to set as ID)
  * in the routing table:
    * do show ip route
    * EIGRP routes are indicated by D
    * RIP is indicated by R
    * metrics get very high, harder to understand

 
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

### Failsafe
* when standby router doesnt receive any hello, it goes to active
* since both routers shared a mac address and ip, with the VMAC and VIP, all that needs to be changes are the switch mac address tables. The clients already know where to send things
* when this happens, the standby, now active router sends gratuitous arp replies.
  * these are ARP replies sent without being requested. All switches will receive the ARP frames and update their mac address tables to forward to the now active router
* what if R1 Comes back online? it will become the standby router. The backup router wont auto give up its role. You can configure the original active router to take back the active state. This is called preemption

### HSRP
* Hot standby router protocol
  * cisco proprietary
  * active and standby router are elected
  * version 1
    * ipv4 only
  * version 2
    * ipv6 and groups
    * subnet support
  * multicast Ipv4 address:
    * v1: 224.0.0.2
    * v2: 224.0.0.102
  * Virtual mac address:
    * v1 = 0000.0c07.acXX (xx = hsrp group number)
    * v2 = 0000.0c8f.fXXX (xxx = hsrp group number)
  * load balancing
    * when you have multiple subnets and or vlans, you can configure a different active router for each subnet in order to load balance over several routers
    * different root bridge in each vlan
    * you can configure a different active router in each subnet as well
    * for example, 2 routers, one is used for the active and one as the standby for vlan1, and vice versa for vlan2
### VRRP
* virtual router redundancy protocol
  * open standard. 
  * Cisco can run it, nearly identical
  * instead of active and standby, it uses master and backup routers
  * functionally exactly the same 
  * multicast ipv4 address is 224.0.0.18
  * virtual mac address is different: 0000.5e00.01XX (XX = VRRP group number)
    * group number is in hexidecimal this time. C8 corresponds to 200 for instance
  * you can configure a different master for each subnet or vlan to load balance
  * all that is different is the naming scheme
  * remember: subnet is layer 3, vlan is layer 2

### GLBP
* gateway load balancing protocol
  * cisco proprietary
  * load balances among several routers in a single subnet
  * AVG, active virutal gateway is elected
  * up to four AVFs (active virtual forwarders) are assigned by the avg itself can be an avf too
  * each avf acts as a default gateway for some hosts
  * multicast ipv4 address is 224.0.0.102
  * virtual mac address: 0007.b400.XXYY (XX = GLBP group number, YY=AVF number)

### configuration
* HSRP
* HSRP is configured on the interface directly
  * interface (interface number)
  * configured with standby command
  * standby (group number)
    * good practice to match number with vlan number
    * the group numbers must match between routers
  * configure virtual ip
    * standby (group number) ip (Vip address)
  * configure if active router
    * standby (group number) priority (priority number)
    * highest priortiy will take the active
    * if any equal priorities, highest ip address value will become active
    * default is 200
  * preemption
    * standby (group number) preempt
    * enables preemption on selected router so that it retakes active after it is restarted on error. Only if it has highest priority
  * to change version:
    * standby version (1/2)
    * version 1 and 2 are not compatible

* both routers need same VIP
* show standby
  * show standby shows standby information