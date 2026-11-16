"""CRC error detection for frames sent between two switches."""
def mod2_div(dividend, divisor):
    rem = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        if rem[i] == '1':
            for j in range(len(divisor)):
                rem[i + j] = '0' if rem[i + j] == divisor[j] else '1'
    return "".join(rem[-(len(divisor) - 1):])

def encode(data, gen):
    crc = mod2_div(data + "0" * (len(gen) - 1), gen)
    return data + crc

def check(frame, gen):
    return set(mod2_div(frame, gen)) == {"0"}

GEN = "1011"
frame = encode("1101011011", GEN)
print("transmitted:", frame)
print("no error   :", check(frame, GEN))
bad = frame[:4] + ("1" if frame[4] == "0" else "0") + frame[5:]
print("1-bit error:", check(bad, GEN))
burst = frame[:2] + "".join("1" if b == "0" else "0" for b in frame[2:5]) + frame[5:]
print("3-bit burst:", check(burst, GEN))
