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

x = 0
while True:
    client,addr = server.accept()
    x += 1
    print('Servicing client at %s'%addr[0])
    res = 'You have connected to %s, please stand by...'%host
    client.send(res.encode('UTF-8'))

    data_received = client.recv(1024)
    
    
    success_mes = 'Successfully Received'
    client.send(success_mes.encode('UTF-8'))


    #try and catch for decode 

    data = json.loads(data_received)
    

    directory = data["UID"]
    cwd = os.getcwd()
    newpath = os.path.join(cwd, "accounts", directory)
    if not os.path.exists(newpath):
       os.mkdir(newpath)

    
    working_file = os.path.join(newpath, data["File"])
    f = open(working_file, 'w') 
    f.write(data["Data"] + "\n")
    f.close()

    #check if there no data passed? 
    
    #successfully updated message 

    client.close()

    #print (data_received)




server.close()
