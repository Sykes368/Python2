from operator import contains
from helper import Text
import subprocess
import scapy.all as scapy
import re
import os
import sys
import psutil
import socket


# Checks for linux operating system and root/sudo permissions
def check_os_and_permissions():
    if not psutil.POSIX:
        print(f"{Text.ERROR}Script is only compatible with linux systems, and possibly other unix operating systems(UNTESTED)")
        sys.exit()

    if not os.geteuid() == 0:
        print(f"{Text.ERROR}Script must be used with sudo or as root.")
        sys.exit()
   
# Checks if an ip is valid
def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Gets the networks from all NICs and Virtual NICs on the system, except for loopback interfaces that start with 127.0.
# Returns a set list of networks in x.x.x.x/x format
def get_networks():
    networks = set()
    ip_networks =  str(subprocess.check_output("ip a | grep inet", shell=True))[2:-3].split('\\n')
    

    for inet in ip_networks:   
        inet = inet[4:].split(' ')
        if inet[0] == "inet":          
            if inet[1] not in networks and not inet[1].__contains__("127.0.") and validate_ip(inet[1]):
                net = re.sub('.[0-9]{1,3}/', '.0/', inet[1])
                networks.add(net)
    
    return networks


# Scans all addresses using ARP identify connected devices.
# Prints out the the amout of ARP replies and the IP + MAC of each device that replied
def arp_scan(network):
        ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=network), timeout=2, verbose=False)

        reply_count = str(ans).split(' ')[4][6:-1]

        if reply_count == "0":
            print(f"{Text.WARN}Did not receive any ARP replies from the {Text.BLUE}{network}{Text.RESET} network.")
            return 1
        else:
            print(f"{Text.SUCCESS}Received {Text.BLUE}{reply_count}{Text.RESET} ARP replies from the {Text.BLUE}{network}{Text.RESET} network.")
            print(f"\n{Text.INFO}All identified devices connected to the {Text.BLUE}{network}{Text.RESET} network:")
            ans.nsummary(lambda s, r: r.sprintf(f"\nIP Address  : {Text.BLUE}%ARP.psrc%{Text.RESET}\nMAC Address : {Text.BLUE}%Ether.src%{Text.RESET}\n"))
       
        return 0