import subprocess
from subprocess import Popen, PIPE, STDOUT
def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

#command = 'ls -l'.split()
#command = 'ls -l'.split()
#for line in run_command(command):
    #print(line)
    
#import subprocess
def runCommand():
    output = subprocess.getoutput("ls -l")
    print(output)