import socket
import json
import argparse

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host   = socket.gethostname()
port = 8060
client.connect((host,port))
res = client.recv(1024)
print(res.decode('UTF-8'))

parser = argparse.ArgumentParser()
parser.add_argument("-uid", type=str, required=True)
parser.add_argument("-file", type=str, required=True)
parser.add_argument("-data", type=str)
args = parser.parse_args()

 

if args.data is None:
   info = {"UID":args.uid,"File":args.file,"Data":None}
   data = json.dumps(info)
   client.sendall(bytes(data,encoding="utf-8"))
   

else:  
   #open text file in read mode
   text_file = open(args.data, "r")
   data = text_file.read()
   text_file.close()
   info = {"UID":args.uid,"File":args.file,"Data":data}
   data = json.dumps(info)
   client.sendall(bytes(data,encoding="utf-8"))
#read whole file to a string

 
#close file


 



res = client.recv(1024)
print(res.decode('UTF-8'))

client.close()


