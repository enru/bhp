import socket

target_host = "127.0.0.1"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAABBBXXX", (target_host, target_port))

data, addr = client.recvfrom(4096)

print data

