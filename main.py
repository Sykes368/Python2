from scapy.all import *
from helper import Text
import re

# Sniffs X packets and prints/saves info about each packet
def sniffer(num, save,filename):
    capture = sniff(filter='ip',prn=lambda s: (s.sprintf(f"Time: {Text.BLUE}%IP.time%{Text.RESET}\nProtocol: {Text.BLUE}%IP.proto%{Text.RESET}\nPort: {Text.BLUE}%IP.sport%{Text.RESET} \nSource IP: {Text.BLUE}%IP.src%{Text.RESET} \nDestination IP: {Text.BLUE}%IP.dst%{Text.RESET} \nFlags: {Text.BLUE}%IP.flags%{Text.RESET} \nData: {Text.BLUE}%Raw.load%{Text.RESET}\n")), count=num)

    # Writes output to pcap
    if save:
        wrpcap(f"{filename}.pcap", capture)
    
    # Prints Capture Summary
    print(capture)


# Gets User Input & Runs sniffer()
if __name__ == '__main__':
    print("Python Packet Sniffer!\n")
   
    num = input("Number of packets to capture [default: 10]: ") 
    if not re.match("^[0-9]+", num):
        num = 10
    
    save = input("Save output to pcap [y/N]? ")

    # Checks input and verifies pcap filename
    if re.match("y", save) or re.match("Y", save): 
        save = True
        filename = input("Pcap filename [default: out]: ")
        if filename==None or filename=="":
            filename="out"
    else:
        save = False
        filename=""

    sniffer(int(num), save, filename)