from __future__ import print_function
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import subprocess
import os
import time
from subprocess import STDOUT, PIPE, Popen
import sys
import re
from threading import Thread
from SocketServer import ThreadingMixIn
import multiprocessing
import socket
import argparse

try:
	delay = 0
	USER = 'root'
	PASSWORD = 'root'
	DBNAME2 = 'db1'
	host = '192.168.1.9'
	port = '8086'
	metric = 'stats'
	umemo = ''
	umemo1 = 0
	umemo_avg = 0
	umemo_avg60 = 0
	fmemo = ''
	fmemo1 = 0
	fmemo_avg = 0
	fmemo_avg60 = 0
	rdiskio = ''
	rdiskio1 = 0
	rdiskio_avg = 0
	rdiskio_avg60 = 0
	wdiskio = ''
	wdiskio1 = 0
	wdiskio_avg = 0
	wdiskio_avg60 = 0
	cputil = ''
	cputil1 = 0
	cputil_avg = 0
	cputil_avg60 = 0
	rtt = ''
	rtt1 = 0
	rtt_avg = 0
	rtt_avg60 = 0 
	band = ''
	cputil = ''
	cputil1 = 0
	count1 = 0
	count1_1 = 0
	count2_1 = 0
	count2 = 0
	count3 = 0
	count3_1 = 0
	count4 = 0
	count4_1 = 0
	count5 = 0
	count5_1 = 0
	count6 = 0
	count6_1 = 0
	rtt = ''
	rtt1 = 0 
	dump = ''
	str1 = 'svmem'
	str2 = 'sdiskio'
	str3 = '64 bytes '
	str6 = 'Client connecting'
	str7 = 'TCP window size'
	str8 = '[  3] local '
	str9 = '[ ID] Interval       Transfer     Bandwidth'
	str10 = '[  3]'
	str11 = '[  4] local '
	str12 = '[  4]'
	str13 = "('CPU:', "
	band = ''
	band1 = 0
	proc = subprocess.Popen(['python', 'user.py'], stdout=subprocess.PIPE)
	for line in iter(proc.stdout.readline,''):
		delay = delay+1
		line = line.rstrip()
		fine = re.split(',',line)

#Filtering of Used memory and Free memory		

		if(line.find(str1) != -1):   
			fine1 = re.split(',',line) 
			umemo = fine1[3]
			umemo = umemo.replace(' used=','')
			umemo = umemo.rstrip()
			umemo1 = float (umemo)
			umemo1 = int (umemo1)
			count1 = count1 + 1
			if(count1 != 5):
				umemo_avg = umemo_avg + umemo1
			else:
				umemo_avg = umemo_avg/6
				count1_1 = count1_1 + 1
				if(count1_1 != 60):
					umemo_avg60 = umemo_avg60 + umemo_avg
				else:
					umemo_avg60 = umemo_avg60/60
					count1_1 = 0
				count1 = 0
			print("Used Memory : ",umemo)
			fmemo = fine1[4]
	                fmemo = fmemo.replace(' free=','')
	                fmemo = fmemo.rstrip()
			fmemo1 = float (fmemo)
			fmemo1 = int (fmemo1)	
			count2 = count2 + 1
			if(count2 != 5):
				fmemo_avg = fmemo_avg + fmemo1
			else:
				fmemo_avg = fmemo_avg/6
				count2_1 = count2_1 + 1
				if(count2_1 != 60):
					fmemo_avg60 = fmemo_avg60 + fmemo_avg
				else:
					fmemo_avg60 = fmemo_avg60/60
					count2_1 = 0	
				count2 = 0
			print("Free Memory : ",fmemo)

# Filtering of DiskIO Read Time and Write Time

		elif(line.find(str2) != -1):  
			fine1 = re.split(',',line)
			rdiskio = fine1[4]
			rdiskio = rdiskio.replace('read_time=','')
			rdiskio = rdiskio.rstrip()
			rdiskio1 = float (rdiskio)
			rdiskio1 = int (rdiskio1)
			count3 = count3 + 1
			if(count3 != 5):
				rdiskio_avg = rdiskio_avg + rdiskio1
			else:
				rdiskio_avg = rdiskio_avg/6
				count3_1 = count3_1 + 1				
				if(count3_1 != 60):
					rdiskio_avg60 = rdiskio_avg60 + rdiskio_avg
				else:
					rdiskio_avg60 = rdiskio_avg60/60
					count3_1 = 0
				count3 = 0
			print("DiskIO Read Time : ",rdiskio)
			wdiskio = fine1[5]
	                wdiskio = wdiskio.replace('write_time=','')
	                wdiskio = wdiskio.rstrip()
			wdiskio1 = float (wdiskio)
			wdiskio1 = int (wdiskio1)
			count4 = count4 + 1
			if(count4 != 5):
				wdiskio_avg = wdiskio_avg + wdiskio1
			else:
				wdiskio_avg = wdiskio_avg/6
				count4_1 = count4_1 + 1
				if(count4_1 != 60):
					wdiskio_avg60 = wdiskio_avg60 + wdiskio_avg
				else:
					wdiskio_avg60 = wdiskio_avg60/60
					count4_1 = 0	
				count4 = 0
			print("DiskIO Write Time : ",wdiskio)

# Round-Trip Time calculation using ping function

		elif(line.find(str3) != -1):  
			fine1 = line.replace('64 bytes ','')
			fine1 = re.split(' ',fine1)
			rtt = fine1[4]
			rtt = rtt.replace('time=','')
			rtt = rtt.rstrip()
			rtt1 = float (rtt)
			rtt1 = int (rtt1)
			count5 = count5 + 1
			if(count5 != 5):
				rtt_avg = rtt_avg + rtt1
			else:
				rtt_avg = rtt_avg/6
				count5_1 = count5_1 + 1
				if(count5_1 != 60):
					rtt_avg60 = rtt_avg60 + rtt_avg
				else:
					rtt_avg60 = rtt_avg60/60
					count5_1 = 0	
				count5 = 0			
			print("Round Trip Time :",rtt)

# Bandwidth filtering section using iPerf function	

		elif(line.find(str10) != -1):		
			if(line.find(str8) != -1):
				dump = line
				print(dump)
			else:
				fine1 = line.replace('[  3] ','')
				fine1 = re.split(' ',fine1)
				band = fine1[len(fine1)-2]
				band = band.rstrip()
				band1 = float(band)
				band1 = int(band1)
				print("Bandwidth :",band1," Mbits/sec")

		elif(line.find(str12) != -1):		
			if(line.find(str11) != -1):
				dump = line
				print(dump)
			else:
				fine1 = line.replace('[  4] ','')
				fine1 = re.split(' ',fine1)
				band = fine1[len(fine1)-2]
				band = band.rstrip()
				band1 = float(band)
				band1 = int(band1)
				print("Bandwidth :",band1," Mbits/sec")
	
# CPU statistics filtering section

		elif(line.find(str13) != -1):
			cputil = line.replace("('CPU:', ",'')
			cputil = cputil.replace(')','')
			cputil1 = float (cputil)
			cputil1 = int (cputil1)
			count6 = count6 + 1
			if(count6 != 5):
				cputil_avg = cputil_avg + cputil1
			else:
				cputil_avg = cputil_avg/6
				count6_1 = count6_1 + 1
				if(count6_1 != 60):
					cputil_avg60 = cputil_avg60 + cputil_avg
				else:
					cputil_avg60 = cputil_avg60/60
					count6_1 = 0	
				count6 = 0
			print(cputil1)
# Rejecting unwanted data for efficient storage 

		else:
			dump = line
			print(dump)
	
# Insertion of data into influx database
	
		pointValues = {
			"measurement": metric,
				'fields':  {
				"CPU": cputil1,
				"CPU60": cputil_avg,
				"CPU1H": cputil_avg60,
				"Umem10": umemo1,
				"Umem60": umemo_avg,
				"Umem1H": umemo_avg60,	
				"Fmem10": fmemo1,
				"Fmem60": fmemo_avg,
				"Fmem1H": fmemo_avg60,
				"RdiskIO": rdiskio1,
				"RdiskIO60" : rdiskio_avg,
				"RdiskIO1H" : rdiskio_avg60,
				"WdiskIO": wdiskio1,
				"WdiskIO60" : wdiskio_avg,
				"WdiskIO1H" : wdiskio_avg60,
				"RTT": rtt1,
				"RTT60": rtt_avg,
				"RTT1H": rtt_avg60,
				"BandWidth": band1,
				},
				'tags': {
				"value": delay,
					},
				}
		dot = [pointValues]
		retention_policy="server_data2"
		client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME2)
		client.create_retention_policy(retention_policy, '5d', 2, default=True)
		client.write_points(dot,retention_policy=retention_policy)
		time.sleep(0.2)
except KeyboardInterrupt:
	sys.exit(0)