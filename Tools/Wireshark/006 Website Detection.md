# Using Wireshark to Identify Which Sites a User Is Searching For

## Overview

This guide explains how to use Wireshark to determine which websites or domains a user is attempting to access. By capturing and analyzing DNS traffic, you can observe domain lookups before web connections are established.

> Note: This method shows domain-level activity (e.g., `google.com`), not full URLs (e.g., `google.com/search?q=...`) unless the site is unencrypted (HTTP).

---

## Requirements

- Wireshark installed
- Network access to the target device or interface
- The local IP address of the device you want to monitor

---

## Step 1: Start a Packet Capture

1. Launch Wireshark.
2. Select the network interface used by the target device (e.g., Wi-Fi or Ethernet).
3. Click **Start Capture**.

---

## Step 2: Apply a Filter to Show DNS Queries

Use this filter to see only DNS queries:

```wireshark
dns and dns.flags.response == 0
```

This will show outgoing DNS queries, but if we want to limit it to our down IP, add it to the filter using 

```wireshark
dns and dns.flags.response == 0 and ip.addr == xxx.xxx.x.xxx
```

---

## Step 3: Generate or Observe DNS traffic

Either
- Visit a website in a browser
- or in Terminal search up nslookup github.com or some other site

---

## Step 4: Locate the Domain name in Packets

Look in the info column for the website(s) you visited such as Github or Wikipedia

Click on the packet and expand the DNS (query) to see:
- Query Name: Wikipedia.org
- Query type: A for Ipv4 or AAAA for Ipv6

## Step 5: Filter for Specfific Domain
```wireshark
dns.qry.name contains "github"
```

## Additional Notes
- DNS requests show only the domain and not the full url or page
- HTTPS websites do not edxpose full URL paths
