from helper import Text
import socket
from datetime import datetime

# Scans all ports on a device given the hostname
def port_scanner(hostname):
    try:
        start_time = datetime.now()
        host_ip = socket.gethostbyname(hostname)
        print(f"Starting scan on {host_ip}")
        print("PORT\t:  STATUS")
        print("--------:--------")

        # Scans all ports & prints open ports
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
             
            connect = s.connect_ex((host_ip, port))
            if(connect == 0):
                print(f"{port}\t:  OPEN")
            s.close()
        end_time = datetime.now()
        print(f"Scan Took: {end_time - start_time}")
    except socket.gaierror:
        print(f"{Text.ERROR}Invalid hostname/IP")
    except socket.herror:
        print(f"{Text.ERROR}Socket herror occured")
    except socket.timeout:
        print(f"{Text.ERROR}Socket timed-out")
    except OverflowError:
        print(f"{Text.ERROR}Invalid port number. Port must be 1-65535")
    except KeyboardInterrupt:
        print(f"{Text.INFO}Keyboard Interrupt: Stopping Scan")

if __name__ == '__main__':
   port_scanner("localhost")