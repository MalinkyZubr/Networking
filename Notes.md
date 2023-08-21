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
* `show ip interface brief``
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
2. show ip interface brief
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
* enter interface configuration `interface (ethernet type) (interface number)
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
* to configure a route, `ip route (destination-address) (mask) (next hop)`. I give this packet to you, you deal with the route.
* ip route 0.0.0.0 0.0.0.0 (router interface IP address)
* the next hop will figure out how to get the packet where it needs to go
* ROUTERS WILL DROP PACKETS WITH UNKNOWN DESTINATIONS. THEY WILL NEVER FLOOD
* unless we configure our routes (or do dynamic routing, later), we cannot send packets to unknown destinations, eg dstinations not in the routing table
* How do we get around this? This command: `ip route (destination IP) (mask) (exit-interface)`. Instead of next hop we specify exit interface. where should we send packets as a route of last resort? to whatever is at the end of the interface. Gateway of last resort is not added however, because this is for specifric networks. But what does this mean? it is technically a direct connection to the destination IP. It is basically saying, "I will give this packet to whatever is connected on this interface, and they will route it where it needs to go". And so, when the packet gets to the router on the connected interface, its own routing will carry out the rest of the work.
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
* enable ip routing using `ip routing` which allows to build IP table. without this intervlan routing wont work
* enter selected interface
* then in the interface, run `no switchport`, so that the port becomes a layer 3 routed port
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
    * what if two switches have two connections between them? the interface connected to the lowest port id is the root port. TO identify this do `show spanning-tree`. STP port id = port priority (def 128) + port number. the NEIGHBOR switch's port id is used to identify root port in this case
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

NOTE THAT ALL GROUP NUMBERS ARE IN HEXIDECIMAL
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

## TCP and UDP
## Layer 4 
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
1. ipv6 unicast routing (enable routing for ipv6)
2. interface (interface)
3. ipv6 address (ipv6 address)
4. no shutdown

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
  1. from config mode, enter int (interface)
  2. ipv6 address (/64 address network portion)/64 eui-64
  3. no shutdown
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
      * access-list (number) deny | permit source_ ip wildcard-mask
      * access-list 1 deny 1.1.1.1 0.0.0.0, where 1.1.1.1 is the ip and 0.0.0.0 is the wildcard mask, specifying it as a /32 ip
      * you could also use access-list 1 deny host 1.1.1.1
      * if you just enter access-list 1 deny 1.1.1.1, it will block that specific ip, since the wildcard mask defaults to 0.0.0.0.
      * in order to permit all other connections, you would add:
        * access-list 1 permit any
        * or, access-list 1 permit 0.0.0.0 255.255.255.255 (ip wildcard combo is the same as any)
      * to add a comment, you can add a remark
        * access-list 1 remark ## (description) ##
      * to see list of access lists:
        * ip lists: do show ip access-lists
        * all lists: do show access-lists
      * do show running-config | include access-list to only show access list entries
    * method set 2
      * enter the config mode for the ACL
        * ip access-list standard 1
        * example:
          * deny 192.168.1.1
          * permit any
  * applying the ACL
    * interface (interface number)
    * ip access-group (number) (in | out)

##### NAMED
* standard named: identified by name
  * to config named ACLs, you must enter named acl config mode
      * ip access-list standard (acl-name)
    * once in the config mode, you can add the ACEs
      * deny | permit source_ip wildcard-mask
      * add remarks the same as with the numbered acls
      * interface (interface)
      * ip access-group (acl name) in | out
      * show access-lists
      * show running-config | section access-list

##### Advantages of config mode
* easily delete ACEs with the no command
  * if you try to delete a specific entry when in global config mode, it will just delete the whole acl
  * no (entry number)
  * this easily deletes 
  * on the other hand if you try to delete from global config mode, you can only delete the entire ACL
* you can insert new entries between other entries by specifying sequence number
  * in global config, if you add an ACE, it just gets appended to the end of the ACL with a number 10 higher than the previous
  * this is why the incrememnt on the numbered acls is 10, if it was just 1 you could insert a new number between 3 and 4. Dont take for granted python datastructures man!

##### Resequencing ACLs
* ip access-list resequence (acl-id) (starting-sequence-nuber) (increment)
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
  * access-list (number) (permit | deny) (protocol/port) (src ip) (dest ip)
* config mode:
  * ip access-list extended {name | number}
    * (sequence number) (permit | deny) (protocol) (src ip) (dest ip)
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
  * source ip any blocks all
  * destination ip:
    * same a ssource IP
  * port numbers
    * to specify sourc eport, specify it after source host and wildcard
    * likewise, for destination port specify it after the destination host and wildcard
    * deny tcp (src ip and wildcar) eq (source port number) (destination ip) (destination wildcard) eq (destination port number)
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
* The CDP neighbor table hods for 180 seconds. If a device doesnt receive a message from a device in 180 seconds it drops the value from cdp table
* 2 versions of cdp, cdpv2 by default. cdpv1 is very old and obsolete

### CDP Commands
* show cdp: show cdp information
* show cdp traffic: show cdp history
* show cdp interface: show what interfaces have active cdp on them
* encapsulation: shows type of ethernet being used
* show cdp neighbors:
  * lists device ID, like switch1 or router4
  * connected interface, what interface is the device ID connected to?
  * holdtime, how much time is left to receive a new CDP advertisement?
  * capability, what these letters mean is on the top when command output
  * platform: model of neighboring device.
* to get additional information, do:
  * show cdp neighbors detail
  * shows vlan, and duplex setting
  * helps show vlan mismatch
* to get filtered output, do
  * show cdp entry (name, like R2)
* CDP overall is useful for debugging network structures
* to enable cdp
  * cdp run
* to disable cdp
  * no cdp run
* to enable or disable cdp on an interface
  * from interface config mode
    * cdp enable
    * no cdp enable

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
  * lldp run
* disable globally
  * no lldp run
* on interface
  * enable transmission 
    * lldp transmit
  * enable receiving
    * lldp receive
* for lldp you need to enable both transmission and reception
* lldp time config
  * lldp timer (seconds)
  * lldp holdime (seconds)
  * lldp reinit (seconds)
* show commands
  * show lldp, basic statuses
  * show lldp traffic: show traffic info
  * show lldp interface: show lldp info for each interface 
  * show lldp neighbor: the lldp connection table
  * show neighbors detail: show detailed table information
  * show lldp entry (name):  get detailed information for just one device name

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
* you can set the clock time using `clock set (hh:mm:ss) (DAY) (MONTH) (YEAR)`
* done from priveleged exec mode
* hardware and software clocks are separate, and can be configured separately
* hardware clock is calendar, software clock is clock
* hardware clock can be manually configured using `calendar set`
  * exactly the same as clock set 
* you can also sync the calendar and clock using `clock update-calendar` (set calendar time to clock) or `clock read-calendar`
* you can configure clock timezone using `clock timezone (timezone name) (hours offset from UTC)`
  * the timezone name doesnt do anything, just a label, thats why you need to specify time offset
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
* `show ntp status` shows synchornization status, and the stratum level of the host
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
  * DHCP tells a host what ip, subnet mask, and interface to use when it connects to a nework command
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
* `ip dhcp excluded-address (ipv4 address range)`: this specifies IP addresses that wont be allocated to DHCP clients
* `ip dhcp pool LAB_POOL` to create DHCP pool and enter DHCP config mode
  * subnet of addresses to be assigned to DHCP clients
  * also includes DNS server address and default gateway
* to configure this range of addresses for the DHCP pool: `network (network address) (network mask / prefix length)`
* `dns-server (ip)` configures what IP the dhcp will use as the default DNS server
* `default-router (router ip)` configures what IP dhcp will use as the default gateway IP
* `lease (num days) (hours) (minutes)` configures the standard lease time for DHCP or `lease infinite` (BAD IDEA)
* last 3 must be done in DHCP config mode
* `show ip dhcp binding` shows all current DHCP clients with DHCP addresses

### Router as DHCP Relay Agent
* enter interface config mode for interface connected to subnet with clients that want DHCP
* `ip helper-address (DHCP server address)` to say what the dhcp server address is. For this, you need to have a route, either static or dynamic to the dhcp server

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
* `logging buffered (buffer size) (level)` sets a buffer size for logging to the specified size, and enbales buffer logging
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
              * higher DP means more likely to drop packets in congestion
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
* 