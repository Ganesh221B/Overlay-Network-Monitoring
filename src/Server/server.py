import psutil
import os
import subprocess
import time
import datetime
import random
#from flask import jsonify
import argparse
import subprocess
import re
import sys
from threading import Thread
from SocketServer import ThreadingMixIn
import multiprocessing
import socket
from subprocess import STDOUT, PIPE, Popen

ping = 'ping' 
ippart = '8.8.8.8'
#pingpart = [ping, ippart]

def bnd():
	try:	
		while 1:
			os.system('iperf -s -p 2005')
			time.sleep(9)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)

def cpu():
	try:
		while 1:   
			cpu = psutil.cpu_percent()		
			print("CPU:",cpu)
			time.sleep(9)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)

def mem():
	try:
		while 1:
			mem = psutil.virtual_memory()
			print(mem)
			time.sleep(9)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)
		
def disk():
	try:	
		while 1:
			disk = psutil.disk_io_counters()
			print(disk)
			time.sleep(9)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)

def ping():
#	proc = subprocess.Popen(pingpart, stdout=subprocess.PIPE)
	os.system('ping -i 10 8.8.8.8')
	#time.sleep(100)
	sys.stdout.flush()


if __name__ == '__main__':
	try:
		p1 = multiprocessing.Process(target=bnd, args=())
		p2 = multiprocessing.Process(target=cpu, args=())
		p3 = multiprocessing.Process(target=mem, args=())
		p4 = multiprocessing.Process(target=disk, args=())
		p5 = multiprocessing.Process(target=ping, args=())
	
		p1.start()
		p2.start()
		p3.start()
		p4.start()
		p5.start()
	
		p1.join()
		p2.join()
		p3.join()
		p4.join()
		p5.join()
	except KeyboardInterrupt:	
		print('Done')
		sys.exit(0)
