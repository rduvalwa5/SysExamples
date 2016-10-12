'''
Created on Oct 9, 2016
@author: rduvalwa2

C1246895-osx:src rduvalwa2$ python3.5 py_arguments.py pwd ls hostname
sys.argv  ['py_arguments.py', 'pwd', 'ls', 'hostname']
sys.base_exec_prefix  /Library/Frameworks/Python.framework/Versions/3.5
sys.base_prefix  /Library/Frameworks/Python.framework/Versions/3.5
executing:  py_arguments.py
pwd
/Users/rduvalwa2/git/GitHub/SysExamples/src
ls
Py_Sys_Examples.py    py_arguments.py        py_script.py        testGit.txt
hostname
C1246895-osx.home

'''
#from sys import argv, sys
import sys
import subprocess

print('sys.argv ',sys.argv)

print('sys.base_exec_prefix ', sys.base_exec_prefix)
print('sys.base_prefix ',sys.base_prefix)
print('sys.builtin_module_names ',sys.builtin_module_names)
print('sys.byteorder ',sys.byteorder)

print('sys.copyright ',sys.copyright)


print('executing: ', sys.argv[0])
for i in range(len(sys.argv)):       
        if i > 0:
            print(sys.argv[i])
            subprocess.run(sys.argv[i])

print(sys._current_frames())
print(sys.exc_info())
print(sys.executable)
print('get allocated blocks ',sys.getallocatedblocks())
print('get allocated blocks ',sys.getallocatedblocks())
print(sys.getswitchinterval())
sys.setswitchinterval(1000)
print(sys.getswitchinterval())
sys._clear_type_cache()
print('get allocated blocks after clear cache',sys.getallocatedblocks())
print(sys.version_info)

#sys.call_tracing(sys.argv[0],sys.argv[1])