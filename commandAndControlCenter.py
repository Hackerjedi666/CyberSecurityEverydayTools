import threading
import socket
import json
import base64

global s
ip = []
targets = []




def server():
	global clients
	while True:
		s.settimeout(1)
		try:
			target, ip = s.accept()
			targets.append(ip)
			print(str(targets[clients]) +  "---" + str(ips[clients]))
		except:




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("192.168.0.108", 1234))
s.listen(5)


clients = 0
