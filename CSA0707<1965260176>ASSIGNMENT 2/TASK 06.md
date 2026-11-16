# Task 06: IPv6, ICMP, Multicast, and SDN in a Smart City

## 1. IPv6 Address Compression & EUI-64 Derivation

### Shortest Form Derivation:
* Original Address: 2001:0db8:0000:0000:0000:ff00:0042:8329
* Rule 1 (Omit Leading Zeros): 2001:db8:0:0:0:ff00:42:8329
* Rule 2 (Compress Contiguous Zero Blocks): 2001:db8::ff00:42:8329

### EUI-64 Interface Identifier Derivation:
* Sensor MAC Address: 00:1A:2B:3C:4D:5E
1. Split MAC into two 24-bit halves: 00:1A:2B and 3C:4D:5E
2. Insert FFFE in the middle: 00:1A:2B:FF:FE:3C:4D:5E
3. Invert the 7th bit (Universal/Local bit) of the 1st byte (00 = 00000000 -> 02 = 00000010): 021A:2BFF:FE3C:4D5E
4. Full Link-Local Address: fe80::21a:2bff:fe3c:4d5e

---

## 2. Multicast MAC Mapping & ICMP Traceroute Mechanics

### Multicast MAC Address Mapping for 239.1.2.3:
* IPv4 Multicast MAC prefix: 01:00:5E:00:00:00
* Convert lower 23 bits of IP 1.2.3 to Hex: 01:02:03
* Resulting Multicast MAC: 01:00:5E:01:02:03
* Efficiency: A traffic camera streams one video frame to multicast IP 239.1.2.3. Hardware switches use IGMP snooping to replicate the stream only at ports connected to subscribed control rooms, avoiding source video duplication.

### Traceroute Mechanics via ICMP:
Traceroute transmits UDP/ICMP probes with incrementing Time-to-Live (TTL) values (1, 2, 3...). The 1st hop router decrements TTL to 0, drops the packet, and returns an ICMP Time Exceeded (Type 11 Code 0) message, revealing its IP address. The source increments TTL to 2, discovering the 2nd hop, repeating until the destination is reached.

---
## 3. OpenFlow Flow Table Rules & SDN Decision

### OpenFlow Rule Evaluation:
* Rule 1 (Priority 200): dst 10.5.0.0/16 -> Forward to Port 3
* Rule 2 (Priority 100): TCP port 80 -> Forward to Controller
* Rule 3 (Priority 0): Fallback -> DROP

### Traffic Evaluation:
1. HTTP Packet to 10.5.1.1 (TCP Port 80): Matches Priority 200 (10.5.1.1 is within 10.5.0.0/16). Priority 200 > 100, so the switch immediately forwards it out Port 3.
2. SSH Packet to 10.6.1.1 (TCP Port 22): Fails Priority 200 and Priority 100. Matches Priority 0 fallback rule -> PACKET IS DROPPED.

### SDN Adoption Judgment:
SDN is highly recommended for a 2-million sensor smart city because centralizing the control plane enables dynamic traffic engineering, automated network slicing for critical IoT data, and real-time security policy enforcement.

