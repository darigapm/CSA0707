# Smart Campus Network Design and IP Address Management System

**Course:** CSA0707 (Computer Networks)  
**Name:** P.M.Dariga  
**Register Number:** 1965260176  
**Simulation Platform:** Cisco Packet Tracer  

## Project Summary
This project designs a campus network divided into four departments—**CSE**, **ECE**, **EEE**, and **Administration**—connected across two routers (**R1** and **R2**) over a point-to-point serial WAN link using **OSPF (Area 0)** and **VLSM** addressing under `192.168.10.0/24`.

## VLSM Subnet Allocation (`192.168.10.0/24`)
| Network | Subnet ID / Prefix | Subnet Mask | Usable Host Range | Broadcast | Gateway |
| :--- | :--- | :--- | :--- | :--- | :--- |
| CSE | `192.168.10.0/26` | `255.255.255.192` | `192.168.10.1 - 192.168.10.62` | `192.168.10.63` | `192.168.10.1` |
| ECE | `192.168.10.64/26` | `255.255.255.192` | `192.168.10.65 - 192.168.10.126` | `192.168.10.127` | `192.168.10.65` |
| EEE | `192.168.10.128/27` | `255.255.255.224` | `192.168.10.129 - 192.168.10.158` | `192.168.10.159` | `192.168.10.129` |
| Administration | `192.168.10.160/28` | `255.255.255.240` | `192.168.10.161 - 192.168.10.174` | `192.168.10.175` | `192.168.10.161` |
| R1-R2 WAN | `192.168.10.176/30` | `255.255.255.252` | `192.168.10.177 - 192.168.10.178` | `192.168.10.179` | N/A |

- **Reserved Range:** `192.168.10.180 - 192.168.10.255`
- **Utilization:** 147 assigned addresses out of 170 usable addresses in allocated subnets (86.5%)

## Verification & Testing
- **Interfaces:** `show ip interface brief` (`up/up` on active LAN and serial interfaces)
- **OSPF Neighbors:** `show ip ospf neighbor` (`FULL` state in Area 0, R1 ID `1.1.1.1`, R2 ID `2.2.2.2`)
- **Connectivity:** `ping 192.168.10.165` and `tracert 192.168.10.165` from `192.168.10.10`

## Files in This Repository
- `docs/Smart_Campus_Network_Design_Report.docx`
- `configs/R1.txt`
- `configs/R2.txt`
- `screenshots/image_1_topology.png`
- `screenshots/image_2_ip_config.png`
- `screenshots/image_3_interface_status.png`
- `screenshots/image_4_ospf_neighbor.png`
- `screenshots/image_5_ping_test.png`
- `screenshots/image_6_traceroute.png`
