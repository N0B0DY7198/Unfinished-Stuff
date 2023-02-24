import requests
from scapy.all import *
from ip2geotools.databases.noncommercial import DbIpCity
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
nigger=s.getsockname()[0]
s.close()
def pc(packet):
    if packet.proto == 17:
        udp = packet.payload

def start():
    while True:
        x = sniff(filter="udp and port 6672", prn=pc, store=1, count=1)
        y = x[0][IP].src
        z = x[0][IP].dst
        if nigger == "192.168.0.102":
            pass
        else:
            print("-----------------------------------------------------------")
            try:
                print(f"Destination: IP Address: [{z}] Country: [{DbIpCity.get(z, api_key='free').country}] Region: [{DbIpCity.get(z, api_key='free').region}] City: [{DbIpCity.get(z, api_key='free').city}]")
            except:
                print(f"Destination: IP Address: [{z}] Country: [{DbIpCity.get(z, api_key='free').country}]")
            print("-----------------------------------------------------------")