"""How data is wrapped by each layer at the sender and unwrapped at the receiver."""
LAYERS = [("Application", "HTTP"), ("Transport", "TCP"), ("Network", "IP"),
          ("Data link", "ETH")]

def send(message):
    pdu = message
    for layer, tag in LAYERS:
        head = "[" + tag + "|"
        tail = "|FCS]" if tag == "ETH" else "]"
        pdu = head + pdu + tail
        print(f"{layer:<12} adds {tag:<5}->  {len(pdu)} bytes")
    return pdu

def receive(frame):
    pdu = frame
    for layer, tag in reversed(LAYERS):
        head = "[" + tag + "|"
        tail = "|FCS]" if tag == "ETH" else "]"
        assert pdu.startswith(head) and pdu.endswith(tail), f"{layer}: bad header"
        pdu = pdu[len(head):-len(tail)]
    return pdu

frame = send("GET /results")
print("on the wire:", frame)
print("delivered  :", receive(frame))
print(f"overhead  : {len(frame) - len('GET /results')} bytes for 12 bytes of data")
