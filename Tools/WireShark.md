# Wireshark

This file will be used to document my knowledge, skills, and things I learn along the way in Wireshark.

## What is Wireshark
At its core, Wireshark serves as a Network protocol analzer. Letting you capture and look at data packets that are traveling across the network in real time.

## First opening Wireshark
When you first open Wireshark you will be met with a list of different network interfaces on your system, such as, Wi-Fi, Ethernet, Loopback, or different adapters. You will notice a 'sparkline' to the side of each, which serves as a real time representation of packet activity on each interface. A flat line or no line means no traffic is being captured this way, but a active heartbeat like line means there is solid traffic actitivty. Just to start off, we will select Wi-Fi.

## Getting Started
After selecting Wi-FI you may get a little overwhelmed, but we will fix that soon. What you are seeing right now is every bit of traffic and communication on that Wi-Fi and if you are looking at your home wifi, apartment wifi or company wifi, there will be a LOT of traffic.

### Slimming it down
To minimize what we are looking at. We are going to filter by our/your IP address to be a bit more controlled. To find this information open command prompt and type in :ipconfig: and look for Ipv4 Address.

Once you have this, plug into the filter bar: 

ip.addr == *insert IP*

or for outgoing traffic only
ip.src == 192.168.29.155

and for incoming traffic only
ip.dst == 192.168.29.155

To thin it out even more to just see Website traffic do
tcp.port == 443 && ip.addr == xxx.xxx.xx.xxx


