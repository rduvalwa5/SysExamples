'''
Created on Oct 9, 2016

@author: rduvalwa2
'''
from sys import argv
import subprocess


print('executing: ', argv[0])

for i in range(len(argv)):
       
        if i > 0:
            print(argv[i])
            subprocess.run(argv[i])

