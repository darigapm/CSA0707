"""Iterative DNS resolution through root, TLD and authoritative servers."""
SERVERS = {
    "root": {"in.": "tld-in", "com.": "tld-com"},
    "tld-in": {"ac.in.": "ns-ac"},
    "tld-com": {"example.com.": "ns-example"},
    "ns-ac": {"simats.ac.in.": "ns-simats"},
    "ns-simats": {"results.simats.ac.in.": "10.20.30.40"},
    "ns-example": {"www.example.com.": "93.184.216.34"},
}
cache = {}

def resolve(name):
    if name in cache:
        return cache[name], 0
    server, queries = "root", 0
    while True:
        queries += 1
        zone_dict = SERVERS[server]
        matching_key = max([k for k in zone_dict if name.endswith(k)], key=len)
        val = zone_dict[matching_key]
        if any(char.isdigit() for char in val):
            cache[name] = val
            return val, queries
        else:
            server = val

for n in ("results.simats.ac.in.", "www.example.com.", "results.simats.ac.in."):
    ip, q = resolve(n)
    print(f"{n:<24} {ip:<15} queries sent: {q}")
