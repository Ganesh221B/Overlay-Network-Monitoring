#!flask/bin/python

import sys
import socket
import threading
from flask import Flask
from flask import send_file
import os
import time
from multiprocessing import Process
import subprocess, shlex


app = Flask(__name__)


@app.route('/run/<string:clients>', methods = ['GET'])
def start_process(clients):
        address = clients.split('_')
        global gclients
        gclients = ' '.join(address)
        Process(target = start_a(clients)).start()
        return "please wait........"



#add New clients

@app.route('/add/<string:Newclients>', methods=['GET'])
def add_clients(Newclients):

#       gclients=start_process(clients)
	address = Newclients.split('_')
	addclients = ' '.join(address)
        stop_service()
        time.sleep(3)
        start_process(gclients+' '+addclients)
        return "clients added\n"

#delete clients

@app.route('/delete/<string:deleteclients>', methods=['GET'])
def delete_clients(deleteclients):
		 address = deleteclients.split('_')
		 delclients = ' '.join(address)
                 Newclients = gclients.replace(delclients,'')
                 stop_service()
                 time.sleep(3)
                 start_process(Newclients)
                 return "clients deleted\n"
				 
				 
				 
def start_a(clients):
        sw(clients).start()
        return "please wait \n"

		

		
		
		
class sw(threading.Thread):
        def __init__(self,clients):
              threading.Thread.__init__(self)
              self.clients = clients
        def run(self):
            start_service(self.clients)
			
		
	
if __name__=='__main__':
       app.run(host ='0.0.0.0')
