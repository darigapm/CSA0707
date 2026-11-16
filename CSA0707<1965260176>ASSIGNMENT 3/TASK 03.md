# Task 03: Why Does the Home Page Take 8 Seconds?

## 1. Mathematical Calculations & Page-Load Time Analysis
* **Context**: The university home page contains 1 HTML file and 80 small objects. Round-Trip Time (RTT) = 50 ms. Transmission time is negligible.

1. **Non-Persistent HTTP (1 Connection at a Time):**
   * Requires a TCP 3-way handshake (1 RTT) + HTTP GET/Response (1 RTT) = 2 RTTs per object.
   * HTML file: 2 RTTs = $2 \times 50 \text{ ms} = 100 \text{ ms}$.
   * 80 objects sequentially: $80 \times (2 \times 50 \text{ ms}) = 8,000 \text{ ms} = 8.0 \text{ seconds}$.
   * **Total Time:** $100 \text{ ms} + 8,000 \text{ ms} = 8,100 \text{ ms}$ (**8.1 seconds**).

2. **Persistent HTTP/1.1 (Without Pipelining):**
   * One TCP handshake for the base connection (1 RTT).
   * Base HTML fetched (1 RTT).
   * 80 objects fetched serially over the persistent connection, each taking 1 RTT.
   * **Total Time:** $1 \text{ RTT (handshake)} + 1 \text{ RTT (HTML)} + 80 \text{ RTTs (objects)} = 82 \text{ RTTs} = 82 \times 50 \text{ ms} = 4,100 \text{ ms}$ (**4.1 seconds**).

3. **Persistent HTTP/1.1 (With Pipelining):**
   * Base HTML fetched (2 RTTs total including handshake).
   * All 80 objects requested simultaneously in a single pipeline burst over the established connection (1 RTT).
   * **Total Time:** $2 \text{ RTTs} + 1 \text{ RTT} = 3 \text{ RTTs} = 3 \times 50 \text{ ms} = 150 \text{ ms}$.

4. **6 Parallel Non-Persistent Connections (Browser Standard):**
   * TCP handshakes and requests are batched across 6 parallel connections.
   * Number of waves for 80 objects = $\lceil 80 / 6 \rceil = 14$ waves.
   * Each wave takes 2 RTTs.
   * **Total Time:** $1 \text{ RTT (handshake)} + (14 \times 2 \text{ RTTs}) = 29 \text{ RTTs} = 29 \times 50 \text{ ms} = 1,450 \text{ ms}$ (**1.45 seconds**).

---

## 2. Protocol Limitations & Optimization Analysis
* **HTTP/2 Head-of-Line Blocking:** Although HTTP/2 multiplexes multiple streams over a single TCP connection, if a single TCP packet is dropped, TCP's reliable in-order delivery stalls the *entire* connection until the lost segment is retransmitted and recovered. All HTTP/2 streams wait together.
* **HTTP/3 over QUIC Solution:** QUIC operates on top of UDP and implements stream-level flow control and multiplexing. If a packet on stream 1 is lost, only stream 1 is delayed; streams 2, 3, and 4 continue delivering data uninterrupted, completely eliminating transport-layer head-of-line blocking.
* **Caching Response Headers:** Using `Cache-Control: max-age=86400` and `ETag` validators on static assets allows browsers to serve subsequent visits instantly from local cache without sending network requests, reducing repeat load time from seconds to milliseconds.
