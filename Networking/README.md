# 🌐 Complete Enterprise Networking Blueprint

This documentation serves as my deep-dive technical reference library for enterprise networking, mapped directly to the CompTIA Network+ architecture.

---

## 📅 Day 1: The OSI Model & Networking Devices

### 1. Architectural Deep-Dive: The 7-Layer OSI Model

*   **Layer 7: Application**
    * Here we interact with application itself. Common applications that would operate in this layer are HTTP,HTTPS,FTP,DNS,POP3 and others.
*   **Layer 6: Presentation**
    * This layer is responsible for putting all data into format as output. It is often combined with application layer . Here reference is character encoding, application encryption .(SSL/TLS) for encrypt/decrypt data.
*   **Layer 5: Session**
    * This layer provides communicatin management between devices . process like start or initilize session , stop and restart session is associated with layer.Here used are control protocols , tunneling protocols . 
*   **Layer 4: Transport**
    * Transport information from one device to another. Also called post office layer . The protocols often used and operate in this layer are TCP(Transmission Control Protocol) and UDP(User Datagram Prtotocol).
*   **Layer 3: Network**
    *Also known as routing layer. This layer is associated with IP Adresses.In this layer frames will be fragmented into smaller pieces in order to move between different types of network.Includes IP addresses , subnet masks,router , protocols .
*   **Layer 2: Data Link**
    * Often to refer as MAC Address layer because data link control(DLC) layer is commonly associated with network cards which are in our devices and we refer to as ethernet or wireless adapters and we refer to physical address on that device as data link control address or MAC address.(MAC)Media Access Control Address : Hardware address of particular adapter card.It is also known as switching layer.Its associated with ethernet frames,MAC address,Extended Unique Identifier (EUI-48,EUI-64),switches.
*   **Layer 1: Physical**
    * Its associated with cables,fiber optics,and signals.It describe physcial signals that we send through cable and fibers on our network. It does'nt have many protocols because getting signal from one part of network to another is its job.When we refer to physical layer problem of network we refer to OSI layer 1 ,Physical layer.Means we might have Bad cable,bad fiber.TROBLESHOOTING IN THIS LAYER IS RUNNING LOOPBACK TESTS,testing cables and fibers , swapping or checking adapter cards and make sure that other devices are properly working with the network.

---

### 2. Networking Devices

#### Router:
*   Operates in OSI layer 3 (Network layer).
*   Uses IP addresses to forward packets between different networks.
*   Connects LANs, WANs, fiber, and copper networks.
*   Determines the best path for data transmission.
*   Some switches also perform Layer 3 routing (Layer 3 Switches).

#### Switches:
* Operates mainly at OSI Layer 2 (Data Link Layer).
* Uses MAC addresses to forward frames.
* Built using ASIC (Application-Specific Integrated Circuit) for fast hardware-based switching.
* Modern switches may also support Layer 3 features and Power over Ethernet (PoE).

#### Access Point(AP):
* Provides wireless connectivity to devices.
* Bridges wireless clients with the wired network.
* Uses IEEE 802.11 Wi-Fi standards.
* Can be configured with security policies and authentication.

#### Wireless LAN Controller(WLC):
* Centrally manages multiple wireless access points.
* Simplifies configuration, monitoring, and firmware updates.
* Enforces consistent security policies across all APs.

#### Load Balancing:
* Load balancing distributes incoming network traffic across multiple servers.
##### Benefits
* Prevents server overload.
* Improves performance and response time.
* Increases availability and reliability.
* Provides fault tolerance if one server fails.
##### Types
* Hardware Load Balancer
* Software Load Balancer
* Cloud-based Load Balancer
##### Algorithms
* Round Robin
* Least Connections
* Weighted Round Robin
* Least Response Time

#### Proxy Server:
* A proxy server acts as an intermediary between users and the internet.
##### Functions
* Filters web traffic.
* Caches frequently accessed content.
* Improves security and privacy.
* Controls internet access.

#### Firewall:
* A firewall monitors and filters incoming and outgoing network traffic.
##### Functions
* Blocks unauthorized access.
* Allows legitimate communication.
* Protects against cyber attacks.
* Enforces security policies.
##### Types
* Packet Filtering Firewall
* Stateful Firewall
* Next-Generation Firewall (NGFW)
* Web Application Firewall (WAF)

#### IDS AND IPS:
##### IDS (Intrusion Detection System)
* Detects suspicious or malicious activity.
* Generates alerts.
* Does not block attacks automatically.
##### IPS (Intrusion Prevention System)
* Detects and automatically blocks malicious traffic.
* Works inline with network traffic.
* Provides real-time protection.

#### VPN(Virtual Private Network):
* A VPN creates an encrypted tunnel between users and the network.
##### Benefits
* Secure remote access.
* Protects sensitive data.
* Encrypts internet traffic.
* Maintains user privacy.

#### NAS Vs SAN:
##### NAS (Network Attached Storage)
* File-level storage.
* Connected through Ethernet.
* Easy to manage.
* Suitable for file sharing and backups.
##### SAN (Storage Area Network)
* Block-level storage.
* High-speed dedicated storage network.
* Offers higher performance.
* Commonly used in enterprise data centers.

#### Key Networking Concepts:
* MAC Address: Physical address used by switches.
* IP Address: Logical address used by routers.
* LAN: Local Area Network.
* WAN: Wide Area Network.
* PoE (Power over Ethernet): Supplies power and data through one Ethernet cable.
* ASIC: Hardware chip used for high-speed packet forwarding.