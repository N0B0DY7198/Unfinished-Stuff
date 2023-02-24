import os, socket, time
from colorama import init
init(convert=True)
def pinger():
    ip = input("Host -> ")
    port = input("Port -> ")
    connced=False
    o_count=0
    of_count=0
    while True:
        sock=socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) #Our tcp socket
        sock.settimeout(1.5) #1.5 second timeout
        try:
            sock.connect((ip, int(port)))
            sock.shutdown(socket.SHUT_RD)
            connced = True
            o_count+=1
            print(f"[91m[SkeleSec][0m | [92m {ip}[0m:[92m{port} | Online (TCP) | Online Pings: {str(o_count)}/{str(of_count)}")
            time.sleep(0.5)
        except socket.timeout:
            of_count+=1
            print(f"[91m[SkeleSec][0m | [91m {ip}[0m:[91m{port} | Offline (TCP) | Online Pings: {str(o_count)}/{str(of_count)}")
banner=r"""
[91m┌───────────────[91m┐
[91m│[97;1m      .-. [91m     │    [97;1m╔╦╗ ╔═╗ ╔═╗[91m
[91m│[97;1m     (o.o)[91m     │    [97;1m ║  ║   ╠═╝[91m
[91m│[97;1m      |=| [91m     │    [97;1m ╩  ╚═╝ ╩[91m  
[91m│[97;1m     __|__[91m     ├────────────────────┐
[91m│[97;1m   //.=|=.\\[91m   │   [97;1m╔═╗┬┌─┌─┐┬  ┌─┐[91m  │
[91m│[97;1m  // .=|=. \\[91m  │   [97;1m╚═╗├┴┐├┤ │  ├┤[91m   │
[91m│[97;1m  \\ .=|=. //[91m  │   [97;1m╚═╝┴ ┴└─┘┴─┘└─┘[91m  │
[91m│[97;1m   \\(_=_)//[91m   │   [97;1m   ╔═╗┌─┐┌─┐[91m     │
[91m│[97;1m    (:| |:)[91m    │   [97;1m   ╚═╗├┤ │  [91m     │
[91m│[97;1m     || ||[91m     │   [97;1m   ╚═╝└─┘└─┘[91m     │
[91m│[97;1m     () ()[91m     ├────────────────────┘
[91m│[97;1m     || ||[91m     │    [97;1m╔═╗╦╔╗╔╔═╗[91m
[91m│[97;1m     || ||[91m     │    [97;1m╠═╝║║║║║ ╦[91m
[91m│[97;1m    ==' '==[91m    │    [97;1m╩  ╩╝╚╝╚═╝[91m
[91m└───────────────┘[91m[0m
"""
#we all know it need a banner makes our eyes happy frfr
print(banner)
print("""[1] TCP Ping.\n[2] Port Scan.\n[0] Exit.""")
opt=input("[SkeleSec->Tools]\n|->")
if opt == "1":
    pinger()
elif opt == "2":
    pass
elif opt == "3":
    pass
else:
    print("[Crit] Not a option :(")