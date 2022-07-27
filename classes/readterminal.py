from subprocess import Popen, PIPE, STDOUT
import paramiko

command = "df"

    # Update the next three lines with your
    # server's information

host = ""
username = ""
password = ""



client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
#print(dir(client))
stdin, stdout, stderr = client.exec_command(command)
print(stdout.read().decode())
client.close()

del client, stdin, stdout, stderr

#from subprocess import Popen, PIPE

#with Popen(['ssh', '-T', '10.20.0.61', 'eduardo'],
           #stdin=PIPE, stdout=PIPE, stderr=PIPE,
           #universal_newlines=True) as p:
    #output, error = p.communicate("""            
        #ls -l
        #""")
    #print(output)
    #print(error)
    #print(p.returncode)
    
""" Parece que funciona
import subprocess
import sys

def runcmd(): 
    HOST="10.20.0.61"
    # Ports are handled in ~/.ssh/config since we use OpenSSH
    COMMAND="uname -a"

    ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    return iter(ssh.stdout.readlines())

runcmd()

"""

#fullString = 'ssh -o "ProxyCommand connect -H eduardo.osquel@10.20.0.21:3128 %h %p" -p 443 -N -D 1080 flyssh.mintplac@us1.flyssh.com'

""""
def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')
"""

#command = 'ls -l'.split()
#command = 'ls -l'.split()
#for line in run_command(command):
    #print(line)
    
    # Command to execute: ssh -o "ProxyCommand connect -H eduardo.osquel@10.20.0.21:3128 %h %p" -p 443 -N -D 1080 flyssh.mintplac@us1.flyssh.com
    
#import subprocess
#def runCommand():
#fullString = 'ssh -o "ProxyCommand connect -H eduardo.osquel@10.20.0.21:3128 %h %p" -p 443 -N -D 1080 flyssh.mintplac@us1.flyssh.com'
#output = subprocess.getoutput(fullString)
#print(output)
