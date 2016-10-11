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

'''
C:\Users\Randall Duval\GitHub_Workspace\SysExamples\src>python py_arguments.py ls pwd whoami hostname env
executing:  py_arguments.py
ls
Py_Sys_Examples.py  py_arguments.py  py_script.py  testGit.txt
pwd
/cygdrive/c/Users/Randall Duval/GitHub_Workspace/SysExamples/src
whoami
c1246895-win64-\randall duval
hostname
C1246895-WIN64-Air
env
!::=::\
!C:=C:\Users\Randall Duval\GitHub_Workspace\SysExamples\src
!ExitCode=00000001
ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\Randall Duval\AppData\Roaming
COMMONPROGRAMFILES=C:\Program Files (x86)\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=C1246895-WIN64-
COMSPEC=C:\Windows\system32\cmd.exe
FIREFOX_HOME=C:\Program Files (x86)\Mozilla Firefox_v31
FP_NO_HOST_CHECK=NO
HOMEDRIVE=C:
HOMEPATH=\Users\Randall Duval
JAVA_HOME=C:\Program Files (x86)\Java\jre1.8.0_40
LOCALAPPDATA=C:\Users\Randall Duval\AppData\Local
LOGONSERVER=\\C1246895-WIN64-
NUMBER_OF_PROCESSORS=2
OS=Windows_NT
PATH=/cygdrive/c/ProgramData/Oracle/Java/javapath:/cygdrive/c/Program Files (x86)/Java/jre1.8.0_40/bin:.:/cygdr
ive/c/Windows/system32:/cygdrive/c/Windows:/cygdrive/c/Windows/System32/Wbem:/cygdrive/c/Windows/System32/Windo
wsPowerShell/v1.0:/cygdrive/c/Program Files (x86)/Mozilla Firefox_v31:/cygdrive/c/python-3.5.0-embed-amd64:/usr
/bin:/cygdrive/c/python-3.5.0-embed-amd64
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
PROCESSOR_ARCHITECTURE=x86
PROCESSOR_ARCHITEW6432=AMD64
PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 69 Stepping 1, GenuineIntel
PROCESSOR_LEVEL=6
PROCESSOR_REVISION=4501
ProgramData=C:\ProgramData
PROGRAMFILES=C:\Program Files (x86)
ProgramFiles(x86)=C:\Program Files (x86)
ProgramW6432=C:\Program Files
PROMPT=$P$G
PSModulePath=C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
PUBLIC=C:\Users\Public
PYTHONHOME=C:\python-3.5.0-embed-amd64\
PYTHON_HOME=C:\python-3.5.0-embed-amd64\
SCITE_USERHOME=C:\Users\Randall Duval\AppData\Local\AutoIt v3\SciTE
SESSIONNAME=Console
SYSTEMDRIVE=C:
SYSTEMROOT=C:\Windows
TEMP=/cygdrive/c/Users/RANDAL~1/AppData/Local/Temp
TMP=/cygdrive/c/Users/RANDAL~1/AppData/Local/Temp
USERDOMAIN=C1246895-WIN64-
USERNAME=Randall Duval
USERPROFILE=C:\Users\Randall Duval
WINDIR=C:\Windows
TERM=cygwin
HOME=/home/Randall Duval
'''