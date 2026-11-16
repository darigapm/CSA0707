"""Hamming(7,4) code: correct a single-bit error in a 4-bit sensor reading."""
def encode(d):
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    return [p1, p2, d[0], p3, d[1], d[2], d[3]]

def decode(c):
    c_bits = c[:]
    s1 = c_bits[0] ^ c_bits[2] ^ c_bits[4] ^ c_bits[6]
    s2 = c_bits[1] ^ c_bits[2] ^ c_bits[5] ^ c_bits[6]
    s3 = c_bits[3] ^ c_bits[4] ^ c_bits[5] ^ c_bits[6]
    pos = s1 + 2 * s2 + 4 * s3
    if pos != 0:
        c_bits[pos - 1] ^= 1
    data = [c_bits[2], c_bits[4], c_bits[5], c_bits[6]]
    return pos, data

word = encode([1, 0, 1, 1])
print("codeword       :", "".join(map(str, word)))
for flip in (None, 5):
    rx = word[:]
    if flip:
        rx[flip - 1] ^= 1
    pos, data = decode(rx)
    print(f"error at {str(flip):<4}: syndrome {pos}, data {''.join(map(str, data))}")
