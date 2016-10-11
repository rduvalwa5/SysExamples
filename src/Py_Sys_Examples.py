'''
Created on Oct 9, 2016
@author: rduvalwa2

https://docs.python.org/3/library/sys.html
'''

import subprocess, os, sys

class sys_arg(object):
    '''
    sys.argv
    The list of command line arguments passed to a Python script. argv[0] is the script name 
    (it is operating system dependent whether this is a full pathname or not). 
    If the command was executed using the -c command line option to the interpreter, 
    argv[0] is set to the string '-c'. If no script name was passed to the Python interpreter, argv[0] is the empty string.
    To loop over the standard input, or the list of files given on the command line, see the fileinput module.
    '''

    def __init__(self, argv):
        '''
        Constructor
        '''
        self.argv = argv

    def get_argu_count(self):
        return len(self.argv)
        
    def print_arguments(self):
        for a in self.argv:
            print(a)
        
    def run_sys_call(self):
        for arg in self.argv:
            print(subprocess.run(arg) ) 
'''
if __name__ == '__main__':
    system_arguments = [['ls','-l'],['whoami'],['pwd']]
    a = sys_arg(system_arguments)
    print(a.get_argu_count())
    a.run_sys_call()
'''