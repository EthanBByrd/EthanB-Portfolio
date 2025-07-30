# Wireshark: Capture and Analyze a File download

## Objective 
Use Wireshark to detect when a file, such as a PDF, EXE, ZIP) is downloaded from website.

This project will work best with unencryprepted HTTP traffic, if HTTPS is used, only the TLS handshake and domain name may be visible, **not the file details or contents**.

---

## Requirements
- Wireshark Installed
- Internet Access
- A test file hosted on a HTTP site

---

## Step 1: Start a packet capture
1. Open Wireshark
2. Select your active network interface (Wi-Fi or Ethernet)
3. Click **start capture**

---

## Step 2: Download a File

Download a file that uses HTTP (not HTTPS). For testing purposes, you can use:

- http://www.africau.edu/images/default/sample.pdf
- http://speedtest.tele2.net/1MB.zip
- http://ipv4.download.thinkbroadband.com/10MB.zip

Try to avoid HTTPS links since the file payload and header details will be encrypted.

---

## Step 3: Apply a Filter

After downloading the file, stop the capture and apply this filter to narrow down relevant traffic:

```wireshark
http
```

or for an even more narrow search

```wireshark
http and ip.addr == xxx.xxx.x.xxx
```

---

## Step 4: Locate the File Transfer

In the info column look for lines like

```wireshark
GET /1MB.zip HTTP/1.1
HTTP/1.1 200 OK (application/zip)
```

Click on the HTTP 200 OK packet and expand the Hypertext Transfer Protocol Section.
Look for:
 - Content Type (application/pdf, application/zip etc.)
 - Content length (file size in bytes)
 - Content-Disposition (May contain the file name)

## Step 4: Follow the TCP stream

To reconstruct the transfer:
1. Right click the
```wireshark
HTTP 200 OK packet.
```
3. Click Follow -> TCP Stream
4. This open the full exchange between client and server.
5. If the file is in plain text (e.g., TXT or CSV), you may see part or all of the content.
6. For binary files, the raw data will appear garbled, but you can Save As Raw for analysis.
