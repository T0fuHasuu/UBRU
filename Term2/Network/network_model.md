# Network Model 

### ISO Organization and OSI Model  
- The **Open Systems Interconnection (OSI Model)** is a standard for explaining communication and protocols in computer systems, developed by the **International Organization for Standardization (ISO).**  
- **Open Systems** means that different systems can communicate, even if they have different architectures.  
- The **OSI Model** is structured into **layers**, each with a specific name and function. It consists of **7 layers** in total.

### Concept of Communication Layers  
1. **Sender:** Writes a letter → Puts it in an envelope → Writes sender & receiver addresses → Drops it in a mailbox.  
2. **Middle Process:** The letter is collected → Sent to the post office → Sorted → Sent to the destination post office.  
3. **Receiver:** The letter is delivered → Opened → Read by the recipient.  

### Physical Layer  
- Handles the transmission of **bit streams** over a physical medium.  
- Defines **mechanical and electrical** specifications for interfaces and data transmission.  
- Manages **functionality and procedures** for devices to connect and communicate.

    #### Responsibilities of the Physical Layer  
    - **Interface & Medium:** Defines the connection between devices and transmission media, including the type of medium used.  
    - **Bit Representation:** Converts data into electrical or optical signals for transmission.  
    - **Data Rate:** Determines how many bits can be sent per second.  
    - **Bit Synchronization:** Ensures sender and receiver are aligned in timing for accurate data transfer.
    - **Transmission Mode:** Defines data flow direction—**Simplex, Half-Duplex, or Full-Duplex.**  
    - **Line Configuration:** Determines connection type—**Point-to-Point (direct) or Multipoint (shared).**  
    - **Physical Topology:** Specifies network layout, such as **Bus, Star, or Ring topology.**

### Data Link Layer  
- Transfers data **Hop-to-Hop** in **frames** and ensures it reaches the network reliably.  
- Detects and corrects **errors** caused by signal interference from the **Physical Layer.**

    #### Responsibilities of the Data Link Layer  
    - **Framing:** Divides data from the Network Layer into **frames** for transmission.  
    - **Physical Addressing:** Adds **source and destination addresses** (e.g., **MAC Address**) in the frame header.  
    - **Flow Control:** Manages data transfer speed to prevent data loss when the receiver can't process fast enough.
    - **Access Control:** Ensures only one device can use the shared transmission medium at a time.  
    - **Error Control:** Detects lost or duplicate data and retransmits if needed.  
    - **Error Detection:** Uses a **trailer** (extra bits) to check for errors in received data.

### Network Layer  
- Transfers **packets** from the source to the destination, even across multiple networks.  
- Unlike the **Data Link Layer** (which operates within a single link), the **Network Layer** handles communication across **different networks.**

    ### Network Layer Responsibilities  
    - **Logical Addressing:** Uses addresses like **IP Address** to identify devices independently of hardware.  
    - **Routing:** Chooses the best path for data to travel across networks, ensuring fast delivery. Routers determine the path using **logical addresses** for source and destination.

### Transport Layer  
- Ensures **Process-to-Process** communication, delivering data correctly between processes (applications) running on different hosts.

    ### Transport Layer Responsibilities  
    - **Port Addressing:** Assigns **Port Addresses** (Service-Point Address) to ensure correct delivery of data to specific processes on the destination computer.  
    - **Segmentation and Reassembly:** Breaks data into smaller **segments** for transmission and reassembles them at the destination.  
    - **Connection Control:** Supports both **connectionless** (UDP) and **connection-oriented** (TCP) communication.  
    - **Flow Control:** Manages data flow between sender and receiver at the process level.  
    - **Error Control:** Ensures data integrity by detecting and retransmitting lost or corrupted data during **Process-to-Process** communication.

### **Session Layer**  
- Manages communication between hosts and controls data exchange. It allows simplex, half-duplex, or full-duplex communication.  
- A session begins with initiation, continues with data exchange, and ends when the communication concludes.  
- **Dialog Control**: Allows two systems to exchange information, with communication starting and ending with session management.  
- **Synchronization**: Ensures recovery if communication fails, by using checkpoints to restart from specific points in the data.  

### Presentation Layer Responsibilities
- **Data Translation:** Translates data between different formats, ensuring compatibility between systems that use different character encoding (e.g., ASCII, Unicode, EBCDIC).
- **Encryption and Decryption:** Secures data by encrypting it before transmission and decrypting it at the destination.
- **Data Compression:** Reduces data size for efficient transmission, decompressing it at the receiver.

### Application Layer Responsibilities
- **User Interface & Access:** Provides a user interface for network access, enabling services like email, data access, and file transfer.
- **File Transfer, Access, and Management:** Allows users to remotely access, manage, and transfer files between host computers.
- **Mail Service:** Software for sending, receiving, and storing electronic mail (email).

## Questions Summary
- **OSI Model Layers:** What are the layers of the OSI model, and what does each layer do?
- **Encapsulation and Decapsulation:** Explain the principles of encapsulation and decapsulation in the OSI model.
- **UDP Protocol:** Explain how the UDP protocol works as connectionless communication.
- **TCP Protocol:** Explain how the TCP protocol works as connection-oriented communication.
