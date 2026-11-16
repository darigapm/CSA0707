# Task 06: Count the Round Trips Before the First Byte (QUIC & TLS 1.3)

## 1. Handshake Round-Trip Time (RTT) Analysis
* **Context**: Mobile network RTT = 100 ms.

1. **TCP + TLS 1.2:**
   * TCP 3-way handshake: 1 RTT
   * TLS 1.2 handshake: 2 RTTs
   * **Total Setup Time before 1st byte request:** $1 + 2 = 3 \text{ RTTs} = 300 \text{ ms}$.

2. **TCP + TLS 1.3:**
   * TCP 3-way handshake & TLS 1.3 key exchange are combined:
   * TCP handshake (1 RTT) + TLS 1.3 flight.
   * **Total Setup Time:** $1.5 \text{ to } 2 \text{ RTTs} = 150 - 200 \text{ ms}$.

3. **QUIC (First Visit):**
   * QUIC combines transport and cryptographic handshake into a single flight.
   * **Total Setup Time:** **1 RTT** ($100 \text{ ms}$).

4. **QUIC with 0-RTT Resumption:**
   * Using pre-shared cryptographic keys from a previous session, application data can be sent immediately in the first packet.
   * **Total Setup Time:** **0 RTT** ($0 \text{ ms}$ delay before sending the first byte).

---
## 2. Security Risks & Engineering Decisions
* **0-RTT Replay Attack Risk:** An attacker can intercept and duplicate a 0-RTT packet (e.g., a financial transaction request). Because the server processes 0-RTT data before verifying the complete handshake, sensitive actions like money transfers must never use 0-RTT.
* **QUIC Connection ID & Mobility:** QUIC identifies connections using a cryptographically random Connection ID rather than source/destination IP-port tuples. When a phone switches from Wi-Fi to 5G, its IP address changes, but QUIC packets retain the same Connection ID, allowing the session to continue seamlessly without dropping or resetting.
* **Firewall Traversal:** Because QUIC runs over UDP, corporate firewalls that only inspect TCP traffic or block unrecognized UDP ports may drop QUIC packets, requiring applications to gracefully fall back to TCP/HTTPS.
