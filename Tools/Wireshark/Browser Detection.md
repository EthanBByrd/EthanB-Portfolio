# Detecting the Browser you are on, using WireShark

This guide walks you through the process of capturing network traffic over Ethernet in Wireshark to identify which web browser is being used on a specific device.

---

## Requirements

- Wireshark installed
- Ethernet connection
- Administrative permissions
- Target device's local IP address

---

## Step 1: Find Your Local IP Address

1. Open Command Prompt.
2. Run the following:
   ```bash
   ipconfig
3. Find your IPv4 address

## Start Capturing
1. Open Wireshark
2. Select the correct interfact (Ethernet, wifi or whatever you are saying)

## Apply a Display Filter
   ```bash
ip.addr == xxx.xxx.x.xxx && http.request
```


## Visit a plain HTTP site
Most modern browsers use HTTPS, which encrypts headers. TO capture a visible User-Agent

Go to [Unecrypted HTTP Site](http://neverssl.com)

This site uses unencrypted HTTP, making headers readable.

## Find and Expand the right packet

1. Look for a packet with GET in the Info Column
2. Select the packet
3. In the Packet Details pane:
   - Expand: Hypertext Transfer Protocol
   - Locate: User=Agent

## Interpret The User-Agent String

Example: User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0


| Part                            | Meaning                                                                 |
|----------------------------------|-------------------------------------------------------------------------|
| `Mozilla/5.0`                   | Legacy compatibility marker (used by all modern browsers)              |
| `(Windows NT 10.0; Win64; x64)` | You're on Windows 10, 64-bit                                           |
| `AppleWebKit/537.36`           | You're using a browser built on the WebKit engine (Chrome/Edge)       |
| `(KHTML, like Gecko)`          | Another compatibility marker                                           |
| `Chrome/138.0.0.0`             | The browser is based on Chrome version 138                             |
| `Safari/537.36`                | Compatibility string (WebKit-based browsers report Safari for legacy)  |
| `Edg/138.0.0.0`                | You're using Microsoft Edge (Chromium-based) version 138               |

>  Note: Even on Windows 11, most browsers report `Windows NT 10.0` for compatibility.


