 # Task 1 – Traffic Sizing

## 1. Traffic Calculations
- **Robot Controllers (40 units):** 40 × 200 bytes × 8 bits/byte × 500 Hz = 32 Mbps[cite: 2]
- **Vibration Sensors (600 units):** 600 × 50 bytes/sec × 8 bits/byte = 0.24 Mbps[cite: 2]
- **CCTV Cameras (24 units):** 24 × 4 Mbps = 96 Mbps[cite: 2]
- **Office Users (150 total, 10% active = 15 users):** 15 × 2 Mbps = 30 Mbps[cite: 2]

- **Total for 1 Production Line:** 32 + 0.24 + 96 + 30 = 158.24 Mbps[cite: 2]
- **Total for Plant (8 lines):** 8 × 158.24 Mbps = 1,265.92 Mbps (~1.27 Gbps)[cite: 2]

## 2. Analysis
- **Most Data:** CCTV cameras (96 Mbps per line)[cite: 2].
- **Strictest Delay:** Robot controllers (10 ms deadline)[cite: 2].
- **Same source?** No, they are different sources[cite: 2].
- **1 Gbps Uplink:** Adequate for 1 line (158.24 Mbps), but inadequate for 8 lines (1.27 Gbps)[cite: 2]. Shared queue without QoS delays robot control commands past 10 ms[cite: 2].

## 3. Delay Harm Ranking (100 ms delay)
1. **Robot Controllers:** Mechanical collisions / safety risk[cite: 2].
2. **Vibration Sensors:** Missed real-time predictive alarms[cite: 2].
3. **CCTV Cameras:** Video stutter/drops[cite: 2].
4. **Office Users:** Perceived slow web loading[cite: 2].

## 4. Alternative Concept Analysis
- CCTV motion-only (5% active): 96 Mbps × 0.05 = 4.8 Mbps[cite: 2].
- New Line Traffic = 67.04 Mbps; New Plant Traffic = 536.32 Mbps[cite: 2].
- **Decision:** 1 Gbps uplink is no longer the bottleneck[cite: 2].
