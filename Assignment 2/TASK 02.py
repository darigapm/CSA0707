import math

def to_int(ip):
    a, b, c, d = map(int, ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d

def to_ip(n):
    return ".".join(str((n >> s) & 255) for s in (24, 16, 8, 0))

def vlsm(base, needs):
    addr = to_int(base)
    for name, hosts in sorted(needs, key=lambda x: -x[1]):
        total_needed = hosts + 2
        bits = math.ceil(math.log2(total_needed))
        block_size = 2 ** bits
        prefix = 32 - bits

        net_addr = addr
        bcast_addr = net_addr + block_size - 1
        first_host = net_addr + 1
        last_host = bcast_addr - 1

        print(f"{name:<11} {to_ip(net_addr)}/{prefix}  hosts {to_ip(first_host)} - {to_ip(last_host)}  bcast {to_ip(bcast_addr)}")
        addr += block_size
    return to_ip(addr)

needs = [("Labs", 100), ("Staff", 50), ("Library", 25), ("WAN link", 2)]
print("next free address:", vlsm("192.168.10.0", needs))
