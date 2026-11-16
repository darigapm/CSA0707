# Task 2 – Collision and Broadcast Domains

## 1. Domain Counting
- **Collision Domains:** 16+ collision domains (3 hub segments + 1 switch-to-router segment + 12 IP phone switch ports)[cite: 2].
- **Broadcast Domains:** 2 broadcast domains (separated by Router interfaces G0/0 and G0/1)[cite: 2].

## 2. OSI Layers & Devices
- **Hub:** Layer 1 (Physical)[cite: 2]
- **Switch:** Layer 2 (Data Link)[cite: 2]
- **Router:** Layer 3 (Network)[cite: 2]

## 3. Standards Table
| Protocol / Tech | Standard | Organization |
| :--- | :--- | :--- |
| Ethernet | IEEE 802.3 | IEEE |
| Wi-Fi | IEEE 802.11 | IEEE |
| IPv4 | RFC 791 | IETF |
| OSI Model | ISO/IEC 7498-1 | ISO |
| 5G | 3GPP / ITU | 3GPP / ITU |

## 4. Alternative Concept Analysis
Replacing hubs with unmanaged switches breaks collision domains (each port becomes its own collision domain), but does not reduce broadcast domains.
