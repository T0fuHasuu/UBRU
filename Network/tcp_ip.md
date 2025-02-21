# Protocol

### What is protocol ?
- It's a set of rule for procedure communicating through network
- Protocols work together in a structured hierarchy called a Protocol Stack

### Binding process 
- Data transmission involves protocols communicating with each other and the network interface card (NIC)
- Multiple protocols (e.g., IPX/SPX or TCP/IP) can be bound to a single NIC.
- Binding typically occurs during OS installation, protocol installation, or protocol activation.
- This process ensures successful network connectivity.

### Device drivers
- Network interface cards (NICs) are just hardware and require drivers to function properly in a network.
- Drivers allow NICs to communicate with the operating system and network protocols for seamless operation.

### Driver with OSI 
- **Network interface card (NIC) drivers** operate at the **MAC sub-layer** of the **Data Link Layer** in the **OSI Model**.  
- The **MAC sub-layer** forwards data to the **Physical Layer** for transmission.  
- The driver enables the NIC to work with the **Redirector**, a network software component on the computer.  
- The **Redirector** helps manage network communication between devices.

### NDIS & ODI
- **NDIS (Network Device Interface Specification)** – Developed by **Microsoft** and **3Com**.  
- **ODI (Open Data-Link Interface)** – Developed by **Novell** and **Apple**.

### Key Standard 
- **OSI Reference Model** (industry-wide standard).  
- **SNA (Systems Network Architecture)** – Developed by **IBM**.  
- **DECnet** – Developed by **Digital**.  
- **NetWare** – Developed by **Novell**.  
- **AppleTalk** – Developed by **Apple**.  
- **TCP/IP** – The **standard protocol for the internet**.

### Application Layer
- **SMTP (Simple Mail Transfer Protocol)** – Sends **emails**.  
- **FTP (File Transfer Protocol)** – Transfers **files** over TCP/IP.  
- **TELNET** – Connects to **network devices** remotely.  
- **DNS (Domain Name System)** – Converts **domain names to IP addresses**.  
- **SNMP (Simple Network Management Protocol)** – Manages **network devices**.  
- **HTTP (Hypertext Transfer Protocol)** – Transfers **webpages** with text, images, audio, and video for web browsers.

### Transport Layer
**Transport Layer Protocols:**  
- Acts as a bridge between the **Application Layer** and **Internetwork Layer**.  

1. **TCP (Transmission Control Protocol)**  
   - **Connection-oriented** (establishes a connection before data transfer).  
   - Ensures **reliable** data delivery with error checking and retransmission.  

2. **UDP (User Datagram Protocol)**  
   - **Connectionless** (no prior connection setup).  
   - Faster but **less reliable** (no error checking or retransmission).  
   - Suitable for **small data transfers** or applications where speed matters (e.g., streaming, VoIP).

### Internetwork Layer
**Internetwork Layer (Network Layer in OSI Model):**  
- Handles the **routing of data** across networks via **routers**, facilitating communication between different networks over the internet.  
- Acts as the **data highway** where packets are routed, ordered, and transferred through **packet-switching**.  
- Houses the **IP (Internet Protocol)**, a core component of **TCP/IP**.  

Key protocols in the Internetwork Layer:  
- **IP (Internet Protocol)** – Routes data between networks.  
- **ARP (Address Resolution Protocol)** – Resolves IP addresses to MAC addresses.  
- **RARP (Reverse Address Resolution Protocol)** – Resolves MAC addresses to IP addresses.  
- **ICMP (Internet Control Message Protocol)** – Manages network communication errors and diagnostics (e.g., ping).

### Internet protocol 
**Internet Protocol (IP):**  
- Manages the **routing of packets** from the sender to the destination host.  
- Uses **routers** to connect different networks and transfer packets across them.  
- **Connectionless** protocol (no need to establish a connection before sending data).  
- Responsible for ensuring data reaches the correct **network** and **host**.

### Address resolution protocol 
**ARP (Address Resolution Protocol):**  
- Before an **IP packet** is sent to another host, the destination **MAC address** must be known.  
- ARP checks the **router's cache** for the destination MAC address.  
- If the address is not found, ARP broadcasts a request on the network.  
- Hosts with a matching address respond by sending their **MAC address** back to the sender.  
- The **router** then records the address in its **routing table** for future use.


### **RARP (Reverse Address Resolution Protocol):**  
- Works opposite of **ARP**, providing an **IP address** to a requesting machine based on its **MAC address**.  
- When a node requests an IP address, **RARP** checks the router's **routing table** for the IP.  
- If the IP is not found in the router's cache, RARP broadcasts a request on the network to get the **IP address** from the destination machine.  
- The requested **IP address** is then sent back to the requesting machine.

### **ICMP (Internet Control Message Protocol):**  
- Used for **sending status messages** related to data transmission.  
- Routers use ICMP to control **data flow** and manage **transmission speed** between routers.  
- Two types of ICMP messages:  
  - **Error Reporting** – Notifies of errors in data transmission.  
  - **Sending Query** – Handles inquiries about the transmission process.

### **Network Access Layer:**  
- Comprises the **Data Link** and **Physical Layers** of the **OSI Model**.  
- Establishes **physical connections** between different network architectures (e.g., Token Ring and Ethernet).  
- Expands to include protocols for **modems**, **data encryption**, **file transfers**, and other general communication tasks.

### **TCP/IP:**  
- TCP/IP is the **communication protocol** used for devices to communicate within a network, similar to how humans need a shared language to communicate.  
- **TCP (Transmission Control Protocol)** – Ensures reliable data transmission with error checking and connection management.  
- **IP (Internet Protocol)** – Handles the addressing and routing of packets across networks.  
- Together, **TCP/IP** is the **standard communication protocol** for the internet and most network systems.

### **TCP/IP:**  
- A **protocol suite** used for communication over the internet, widely adopted today.  
- Designed to enable communication from the **source** to the **destination** across networks.  
- Automatically finds alternative routes for data transmission, even if the current path has issues.  
- TCP/IP is the **standard communication language** for the internet, allowing devices of all types (microcomputers, minicomputers, mainframes) to connect to the internet.

### **TCP/IP Data Transmission Process:**  
- **Data** is divided into smaller parts called **packets**.  
- Each packet is tagged with **source** and **destination** information.  
- Packets are sent through **various routes** across the network, and they do not need to follow the same path or be in order.  
- **Routers** determine the best route for each packet.  
- Once all packets reach the destination, they are reassembled into the original message.  
- If any packet is lost, the system will **re-request** the missing packet until all data is complete.

### **IP Address:**
- An **IP address** consists of 4 bytes (32 bits).  
- It includes:
  - **Class Type**  
  - **Network Identifier (NetID)**  
  - **Host Identifier (HostID)**  

**Classes of IP Addresses:**
- **Class A**: `0.0.0.0` - `127.255.255.255`  
- **Class B**: `128.0.0.0` - `191.255.255.255`  
- **Class C**: `192.0.0.0` - `223.255.255.255`  
- **Class D**: `224.0.0.0` - `239.255.255.255` (Used for **Multicast Addresses**)  
- **Class E**: `240.0.0.0` - `255.255.255.255` (Reserved for **future use**)

### **CIDR (Classless Inter-Domain Routing) Notation:**
- **CIDR notation** combines the **IP address** and the **subnet mask** into a single string.
- Example: `128.10.0.0/16`  
  - **128.10.0.0** is the **network address**.  
  - `/16` indicates the **subnet mask** (16 bits set to 1), equivalent to **255.255.0.0**.  

**Subnet Mask:**
- **Subnet Mask**: `255.255.0.0`  
  - In **binary**: `11111111.11111111.00000000.00000000`
  - The **first 16 bits** are used for the network, and the remaining bits are used for hosts within the network.

### **Private IP Network Ranges:**
- **Class A (Private)**: `10.0.0.0` - `10.255.255.255`  
- **Class B (Private)**: `172.16.0.0` - `172.31.255.255`  
- **Class C (Private)**: `192.168.0.0` - `192.168.255.255`

