# Task 07: Telemedicine Platform – Protocol Design from First Principles

## Stage 1: Problem Interpretation & Traffic Requirements
* **Live Video Consultations:** Ultra-low delay (< 150 ms), high jitter tolerance, loss-tolerant (video codecs handle dropped frames), high bandwidth.
* **Patient Records & X-ray Images:** 100% reliable, zero data corruption, ordered delivery, loss-averse.
* **Instant Messaging (Chat):** Reliable, session-oriented, low latency.
* **DNS Service Lookups:** Fast UDP queries with caching.

## Stage 2: Candidate Protocol Comparison & Calculations
* **Protocol Matrix:** QUIC for video & chat (low RTT, multiplexed), TCP/TLS 1.3 for X-rays & records (strict reliability), HTTP/3 over QUIC for web portals.
* **TCP Throughput Limit Calculation:**
  * Window size = $64 \text{ KB} = 65,535 \text{ bytes}$.
  * RTT = $300 \text{ ms} = 0.3 \text{ s}$.
  * Max Throughput = $\frac{\text{Window Size}}{\text{RTT}} = \frac{65,535 \times 8 \text{ bits}}{0.3 \text{ s}} = \frac{524,280 \text{ bits}}{0.3 \text{ s}} = 1.747 \text{ Mbps}$.
  * *Impact on X-rays:* A high-resolution DICOM X-ray image (e.g., 20 MB) will take over 90 seconds to transfer over a single TCP window at 300 ms RTT unless window scaling (TCP Window Scale Option) is enabled.

## Stage 3: Implementation & Verification
* Evaluated socket communication under simulated 4G conditions (`tc netem` with 200 ms delay and 3% packet loss). Measured successful fallback and reliable transmission streams.

## Stage 4: Design Defence & Upgrades
* **Justification:** QUIC prevents video call freezing caused by packet loss on other streams, while TCP guarantees lossless X-ray delivery.
* **5G Upgrade Path:** Moving to 5G reduces RTT to 10–20 ms and increases bandwidth, raising TCP/QUIC throughput limits past 100 Mbps and eliminating video stutter entirely.
