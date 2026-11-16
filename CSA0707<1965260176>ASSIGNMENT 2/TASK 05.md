# Task 05: Why Does OSPF Treat 1 Gbps and 10 Gbps the Same?

## 1. OSPF Metric Formula & Default Reference Bandwidth Problem
OSPF (Open Shortest Path First) calculates interface costs dynamically using a reference bandwidth formula:

OSPF Cost = Reference Bandwidth / Interface Bandwidth

By default, Cisco IOS uses a Reference Bandwidth of 100 Mbps (100,000,000 bits per second).

### Default Cost Calculations:
* 10 Mbps Link: 100 Mbps / 10 Mbps = Cost 10
* 100 Mbps Link (FastEthernet): 100 Mbps / 100 Mbps = Cost 1
* 1 Gbps Link (GigabitEthernet): 100 Mbps / 1000 Mbps = 0.1 -> Rounds to 1
* 10 Gbps Link (TenGigabitEthernet): 100 Mbps / 10000 Mbps = 0.01 -> Rounds to 1

### Root Cause Analysis:
Because OSPF cost values are stored strictly as positive integers, any link speed equal to or exceeding the 100 Mbps reference bandwidth is truncated to a cost of 1. Consequently, 100 Mbps, 1 Gbps, and 10 Gbps links all share an identical cost of 1. This forces OSPF to treat 1 Gbps and 10 Gbps paths as equal-cost paths, causing traffic splitting or suboptimal routing over slower 1 Gbps links.

---

## 2. Reference Bandwidth Correction & Dijkstra's Algorithm

### Resolution Command:
To fix metric compression, we adjust the reference bandwidth to 10,000 Mbps (10 Gbps) on all routers:
```text
R1(config)# router ospf 1
R1(config-router)# auto-cost reference-bandwidth 10000
