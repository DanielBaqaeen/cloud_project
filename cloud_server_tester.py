import numpy as np
import multiprocessing as mp
import uuid
import random
import string
import os
import argparse

#file argument
#number of time argument

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, required=True)
parser.add_argument("-source", type=str)
args = parser.parse_args()

conc_tests = args.n

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def caller(): 
  UID= random_string(length = 10)
  File = uuid.uuid4().hex
  if args.source is None:
     command = "python ./cloud_client.py -uid " +  UID + " -file " + File + ".txt"
  else: 
     command = "python ./cloud_client.py -uid " +  UID + " -file " + File + ".txt -data " + args.source
  os.system(command)

cpus = int(round(mp.cpu_count() / 2 ))

if __name__ == '__main__':
    p1 = mp.Pool(cpus)
    for i in range(conc_tests):
        p1.apply_async(caller)
    p1.close()
    p1.join()