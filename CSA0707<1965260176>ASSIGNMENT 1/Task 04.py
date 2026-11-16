"""Nyquist and Shannon limits for the transmission media proposed for a campus."""
import math

def nyquist(bandwidth_hz, levels):
    return 2 * bandwidth_hz * math.log2(levels)

def shannon(bandwidth_hz, snr_db):
    snr_ratio = 10 ** (snr_db / 10)
    return bandwidth_hz * math.log2(1 + snr_ratio)

media = [("Telephone line", 3_100, 30), ("Cat6 pair", 250e6, 40),
         ("Wi-Fi 6 channel", 160e6, 25)]
for name, bw, snr in media:
    print(f"{name:<16} Shannon limit {shannon(bw, snr) / 1e6:10.2f} Mbps")
print(f"Nyquist, 3,100 Hz with 4 levels: {nyquist(3_100, 4) / 1e3:.1f} kbps")
