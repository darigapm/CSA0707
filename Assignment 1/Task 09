"""Link utilisation of stop-and-wait and sliding-window protocols on different links."""
def utilisation(frame_bits, rate_bps, distance_m, window, speed=2e8):
    tx = frame_bits / rate_bps
    prop = distance_m / speed
    a = prop / tx
    u = min(1.0, window / (1 + 2 * a))
    return u, a

links = [("Campus LAN, 200 m, 1 Gbps", 1e9, 200),
         ("City fibre, 50 km, 1 Gbps", 1e9, 50_000),
         ("Satellite, 36,000 km, 10 Mbps", 10e6, 36_000_000)]
for name, rate, dist in links:
    u1, a = utilisation(12_000, rate, dist, 1)
    u7, _ = utilisation(12_000, rate, dist, 7)
    u127, _ = utilisation(12_000, rate, dist, 127)
    print(f"{name:<31} a = {a:7.2f}  stop-and-wait {u1:6.1%}  "
          f"W=7 {u7:6.1%}  W=127 {u127:6.1%}")
