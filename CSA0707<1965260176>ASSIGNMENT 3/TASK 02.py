"""TCP congestion window over 20 round trips: slow start, avoidance and loss."""
def simulate(losses, ssthresh=16, reno=True):
    cwnd, trace = 1, []
    for rtt in range(1, 21):
        trace.append(cwnd)
        if rtt in losses:
            ssthresh = max(cwnd // 2, 2)
            cwnd = ssthresh if reno else 1
        else:
            if cwnd < ssthresh:
                cwnd *= 2
            else:
                cwnd += 1
    return trace

for label, reno in (("Reno ", True), ("Tahoe", False)):
    tr = simulate({8, 14}, reno=reno)
    print(label, " ".join(f"{w:2d}" for w in tr), f"| segments sent {sum(tr)}")
