"""UDP and TCP sockets on one machine: a time server answering three clients."""
import socket
import threading

def udp_server(sock):
    for _ in range(3):
        data, addr = sock.recvfrom(1024)
        sock.sendto(b"ACK:" + data, addr)

def tcp_server(sock):
    conn, _ = sock.accept()
    total = 0
    with conn:
        while True:
            chunk = conn.recv(4096)
            if not chunk:
                break
            total += len(chunk)
    print(f"TCP server received {total} bytes in order")

u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
u.bind(("127.0.0.1", 0))
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.bind(("127.0.0.1", 0))
t.listen(1)

threading.Thread(target=udp_server, args=(u,)).start()
th = threading.Thread(target=tcp_server, args=(t,))
th.start()

for name in ("lab1", "lab2", "lab3"):
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c.sendto(name.encode(), u.getsockname())
    reply, _ = c.recvfrom(1024)
    print("UDP", name, "->", reply.decode())
    c.close()

c = socket.create_connection(t.getsockname())
c.sendall(b"x" * 100_000)
c.close()

th.join()
u.close()
t.close()
