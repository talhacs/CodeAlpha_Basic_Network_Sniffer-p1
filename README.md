# CodeAlpha: Basic Network Sniffer

A lightweight, terminal-based network packet sniffer developed in Python using the Scapy library. This security tool dynamically intercepts network traffic, parses critical network layers, and extracts source/destination IPs, protocols, and raw payload data in real-time. 

*Note: This project was developed as a compulsory task for the CodeAlpha Cybersecurity Internship Program.*

## 🚀 Features
* **Real-time Packet Capture:** Sniffs incoming and outgoing network traffic smoothly with zero memory leaks.
* **Protocol Identification:** Decodes and flags major network protocols including TCP, UDP, and ICMP.
* **Payload Preview:** Extracts and displays hex-encoded payload snippets directly from data-carrying packets.
* **Graceful Termination:** Handles user interruption safely using clean keyboard break signals (`Ctrl+C`).

## 🛠️ How It Works
The script utilizes raw socket manipulation abstraction provided by **Scapy**:
1. **Sudo Privileges:** The tool requests kernel-level access to put the system's network interface card (NIC) into promiscuous/capture mode.
2. **Sniffing Loop:** The `sniff()` function runs an infinite packet listening loop without storing data in RAM (`store=False`), processing traffic dynamically.
3. **Layer Filtering:** For every frame captured, the program validates the presence of an `IP` layer.
4. **Data Extraction:** It parses the network headers to fetch IP strings and maps the transport layer protocol numbers. If a data payload is present inside a TCP or UDP packet, it slices the first 60 characters and prints them securely to the console.

## 📋 Requirements & Setup
This project is built for **Linux environments** (Ubuntu/Kali Linux).

### 1. System Dependencies
Ensure Python 3 and its packet manager are installed:
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### 2. Install Python Dependencies
Install the required Scapy library:
```bash
pip3 install scapy
```

## 💻 Usage Instructions
Run the script with root administrative permissions using `sudo`:
```bash
sudo python3 sniffer.py
```

### To Generate Test Traffic:
Open a second terminal tab and send quick network packets to check the sniffer output:
```bash
ping -c 4 8.8.8.8
```

## 📸 Output & Proof of Functionality
Below is the verified screenshot of the network sniffer running on Linux, capturing real-time network traffic headers and packet payloads successfully:

![Network Sniffer Screen Evidence](screenshot.png)


