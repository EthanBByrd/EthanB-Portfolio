# Identifying OS with Wireshark

## Project Goal
Use Wireshark to capture TCP SYN packets from devices and analyze packet-level details to estimate the operating system. This technique relies on passive OS fingerprinting using values such as TTL, window size, and TCP options.

---

## Requirements
- Wireshark installed
- A network-connected device (Windows, macOS, Linux, Android, etc.)
- Internet access or internal traffic to generate TCP connections

---

## Steps

### Step 1: Start a Packet Capture
1. Open Wireshark.
2. Select your active network interface (Wi-Fi or Ethernet).
3. Click **Start Capture**.

---

### Step 2: Apply a Display Filter
Filter for TCP SYN packets (used to initiate new connections):

```wireshark
tcp.flags.syn == 1 and tcp.flags.ack == 0
```
### Step 3: Select and Inspect a Packet
Click on a packet in the filtered list and expand the following protocol layers:

- **Internet Protocol Version 4**
  - Look for the **Time To Live (TTL)** value
- **Transmission Control Protocol**
  - Locate the **Window Size Value**
  - Review the **TCP Options** (e.g., MSS, SACK Permitted, Timestamps, etc.)

These values vary slightly by operating system and will be used to estimate the OS in the next step.

---

### Step 4: Match Values to Known OS Fingerprints

| Operating System | TTL  | Window Size     | TCP Options           | Notes                          |
|------------------|------|------------------|------------------------|--------------------------------|
| Windows 10/11    | 128  | 65535            | SACK, Timestamps       | Common default Windows values  |
| macOS / iOS      | 64   | 65535            | SACK, Timestamps       | Similar to BSD systems         |
| Linux (Ubuntu)   | 64   | 29200 / 5840     | SACK, Timestamps       | May vary by distro             |
| Android          | 64   | Varies           | Often like Linux       | Manufacturer-dependent         |
| Cisco/Embedded   | 255  | Small (e.g., 4128)| Minimal or no options | Used in routers/switches       |

Use these traits as a reference to make an educated guess about the device's operating system.

---

### Step 5: Compare Multiple Devices
Repeat the process with different networked devices to gather more examples:

- Your personal computer
- A mobile phone
- A smart TV or gaming console
- Any other smart home or IoT device

Compare the values (TTL, Window Size, TCP Options) and see how different systems leave different "fingerprints."

