# Wireshark Filters Reference

This README provides a curated list of common Wireshark display filters and explains what each one is used for. Display filters are used after packet capture to analyze specific network traffic by narrowing down the packet list.

---

## What Are Display Filters?

Display filters in Wireshark allow you to inspect specific types of packets or traffic patterns within a capture file. These filters help in diagnosing issues, tracing protocols, or simply understanding traffic behavior.

---

## Common Wireshark Display Filters

| **Filter**                         | **What It Does**                                                                 |
|-----------------------------------|----------------------------------------------------------------------------------|
| `ip.addr == 192.168.1.1`          | Shows all traffic to or from the IP address `192.168.1.1`.                       |
| `ip.src == 192.168.1.1`           | Shows only traffic originating **from** `192.168.1.1`.                           |
| `ip.dst == 192.168.1.1`           | Shows only traffic **going to** `192.168.1.1`.                                   |
| `tcp.port == 80`                  | Filters packets using TCP port 80 (commonly HTTP).                              |
| `udp.port == 53`                  | Filters for DNS queries/responses using UDP port 53.                             |
| `http`                            | Displays only HTTP protocol traffic.                                             |
| `dns`                             | Displays only DNS traffic.                                                      |
| `tcp`                             | Shows all TCP traffic.                                                           |
| `udp`                             | Shows all UDP traffic.                                                           |
| `icmp`                            | Filters only ICMP packets (like ping).                                           |
| `tcp.flags.syn == 1`              | Displays TCP SYN packets (used in the beginning of TCP handshakes).              |
| `tcp.flags.fin == 1`              | Shows TCP FIN packets, often signaling the end of a connection.                 |
| `tcp.analysis.retransmission`     | Filters for TCP retransmissions, helpful for identifying packet loss.           |
| `eth.addr == aa:bb:cc:dd:ee:ff`   | Filters packets involving the specific MAC address.                             |
| `frame contains "password"`       | Searches for packets that contain the string “password” in the payload.         |
| `tcp.stream eq 1`                 | Isolates one TCP conversation (useful when following a specific stream).        |
| `ip.ttl < 10`                     | Filters packets with TTL (Time to Live) values less than 10.                    |
| `ssl` or `tls`                    | Displays SSL/TLS traffic (useful for HTTPS and encrypted data).                 |
| `arp`                             | Shows only ARP traffic (used for resolving IP to MAC addresses).                |

---

## How to Use

1. Open Wireshark and start or load a capture.
2. Enter any of the filters above in the **Display Filter** bar at the top.
3. Press **Enter** to apply the filter and view only matching packets.

---

## Tips

- Combine filters with logical operators:
  - `and`, `or`, `not`
  - Example: `ip.src == 192.168.1.1 and tcp.port == 443`
- Autocomplete helps avoid typos.
- Use `Follow > TCP Stream` to reconstruct conversations.

---
