import socket

port = 20, 21, 22, 25, 5, 80, 110, 11, 123, 14, 161, 19, 46, 554, 87, 993, 99, 3389, 5631
ip = 'the_ip_address'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((ip, port))
if result == 0:
    print("Port is open")
else:
    print("Port is not open")