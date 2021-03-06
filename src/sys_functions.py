''''
sys module functions
'''
import sys

class sys_functions(object):
    
    def  get_sys_version(self):
        '''
        sys.version
        A string containing the version number of the Python interpreter plus additional information on the build number and compiler used. 
        This string is displayed when the interactive interpreter is started. Do not extract version information out of it, 
        rather, use version_info and the functions provided by the platform module.
        '''
        return  sys.version
        
    def get_sys_version_info(self):
        '''
        sys.version_info
        A tuple containing the five components of the version number: major, minor, micro, releaselevel, and serial. All values except releaselevel 
        are integers; the release level is 'alpha', 'beta', 'candidate', or 'final'. The version_info value corresponding to the 
        Python version 2.0 is (2, 0, 0, 'final', 0). The components can also be accessed by name, so sys.version_info[0] is equivalent to 
        sys.version_info.major and so on.
        '''
        return sys.version_info

    def get_api_version(self):
        '''
        sys.api_version
        The C API version for this interpreter. Programmers may find this useful when debugging version conflicts between Python 
        and extension modules.
        '''
        return  sys.api_version

    def get_thread_info(self):
        '''
        sys.thread_info
        A struct sequence holding information about the thread implementation.
        Attribute        Explanation
        name            Name of the thread implementation:
                        'nt': Windows threads
                        'pthread': POSIX threads
                        'solaris': Solaris threads
        lock            Name of the lock implementation:
                        'semaphore': a lock uses a semaphore
                        'mutex+cond': a lock uses a mutex and a condition variable
                        None if this information is unknown
        version         Name and version of the thread library. It is a string, or 
                        None if these informations are unknown.
        '''
        return  sys.thread_info
    
    
if __name__ == '__main__':
    
    thisObj = sys_functions()
    print('pythan ahd c version: \n',thisObj.get_sys_version())
    print('version_info', thisObj.get_sys_version_info())
    print('api version', thisObj.get_api_version())
    print('thread info ', thisObj.get_thread_info())