import os
import subprocess
import multiprocessing as mp
import numpy as np
import socket
import json

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host   = socket.gethostname()
port   = 8060
server.bind((host,port))
server.listen(10)

if not os.path.exists("accounts"):
    os.mkdir("accounts")

while True:
    client,addr = server.accept()
    print('Servicing client at %s'%addr[0])
    res = 'You have connected to %s, please stand by...'%host
    client.send(res.encode('UTF-8'))

    data_received = client.recv(1024)
    data = json.loads(data_received)


    directory = data["UID"]
    cwd = os.getcwd()
    newpath = os.path.join(cwd, "accounts", directory)


    if data["Data"] is None and not os.path.exists(newpath):
      os.mkdir(newpath)
      success_mes = 'Successfully created an account, no data updated'
      client.send(success_mes.encode('UTF-8'))  
    
    elif data["Data"] is None and os.path.exists(newpath):
        success_mes = 'Welcome back, no data updated'
        client.send(success_mes.encode('UTF-8')) 
   
    elif not os.path.exists(newpath):
      os.mkdir(newpath)
      working_file = os.path.join(newpath, data["File"])
      f = open(working_file, 'w') 
      f.write(data["Data"] + "\n")
      f.close()
      success_mes = 'Successfully created an account and saved the data'
      client.send(success_mes.encode('UTF-8')) 

    elif os.path.exists(newpath):
      working_file = os.path.join(newpath, data["File"])
      f = open(working_file, 'w') 
      f.write(data["Data"] + "\n")
      f.close()
      success_mes = 'Welcome back, successfully updated the data'
      client.send(success_mes.encode('UTF-8')) 
    

    client.close()

server.close()
