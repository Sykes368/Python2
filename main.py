from helper import Text
from ipdata import ipdata
import subprocess
import sys
import re


# Setup ipdata API with API key
ipdata = ipdata.IPData('cff3528d8a2553aea9f2428cf9d8d79e41c2454a2a65f37ef72ccbc2')


# Checks if ipdata is installed & if not runs pip to install ipdata
def check_dependency():
    if 'ipdata' not in sys.modules:
        print(f"{Text.WARN}Package {Text.BLUE}ipdata{Text.RESET} is not installed.")
        print(f"{Text.INFO}Installing {Text.BLUE}ipdata{Text.RESET} using pip...")
       
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "ipdata"])
        except:
            print(f"{Text.ERROR}Failed to install {Text.BLUE}ipdata{Text.RESET}. Exiting...")
            exit(1)
        
        print(f"{Text.SUCCESS}Succussfully installed {Text.BLUE}ipdata{Text.RESET} package")


# Reads and validates ip given as cli argument. If invalid informs user and exits
def get_and_validate_ip():
    # Trys to read ip argument. Exits if not present
    try:
        ip = sys.argv[1]
    except IndexError:
        print(f"{Text.ERROR}No IP given.")
        print(f"{Text.INFO}Please give IP as command line argument eg. {Text.BLUE}./main.py <ip>{Text.RESET}")
        exit(2)

    # Checks if given ip is a valid public IPv4 address
    valid_ip = re.compile("^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))(?<!127)(?<!^10)(?<!^0)\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!192\.168)(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
    if not valid_ip.match(ip):
        print(f"{Text.ERROR}Invalid Public IPv4 Address: {Text.BLUE}{ip}{Text.RESET}")
        exit(3)

    return ip
    

# Gets and prints geoip data about the given ip
def get_geoip_info(ip):
    # Creates dictonary of geoip data about given ip
    try:
        geoipdata = ipdata.lookup(ip)
    except:
        print(f"{Text.ERROR}Error Getting GeoIP Data for {Text.BLUE}{ip}{Text.RESET}")
        exit(5)

    # Parses geoipdata and prints geoip information about given ip
    print(f"{Text.INFO}GeoIP data for {Text.BLUE}{ip}{Text.RESET}")
    print(f"   Latitude\t: {Text.BLUE}{geoipdata['latitude']}{Text.RESET}")
    print(f"   Longitude\t: {Text.BLUE}{geoipdata['longitude']}{Text.RESET}")
    print(f"   Time Zone\t: {Text.BLUE}{geoipdata['time_zone']['name']}{Text.RESET}")
    print(f"   Country\t: {Text.BLUE}{geoipdata['country_name']}{Text.RESET}")
    print(f"   City\t\t: {Text.BLUE}{geoipdata['city']}{Text.RESET}")
    print(f"   Postal Code\t: {Text.BLUE}{geoipdata['postal']}{Text.RESET}")
    print(f"   Organization\t: {Text.BLUE}{geoipdata['asn']['name']}{Text.RESET}")
    

if __name__ == '__main__':
    check_dependency()
    get_geoip_info(get_and_validate_ip())