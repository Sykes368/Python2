import os.path as path
import socket
import sys
import ssl


## Contents of helper.py added here to condense to 1 file
# Color codes & quick access to error, and warning message prefixes
class Text:
    # Colors
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GRAY = '\033[37m'
    # Formatting + Reset all
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    # Prefixes
    ERROR = f'{GRAY}[{RED}!!{GRAY}]{RESET} '
    WARN = f'{GRAY}[{YELLOW}!{GRAY}]{RESET} '
    INFO = f'{GRAY}[{BLUE}*{GRAY}]{RESET} '
    SUCCESS = f'{GRAY}[{GREEN}*{GRAY}]{RESET} '


# Returns a list of domains, that were read from the given file
def read_domains_txt(filename):
    
    if path.exists(filename):
        try:        
            domains = open(filename, 'r')            
        except:
            print(f"{Text.ERROR}Error while reading {Text.BLUE}{filename}{Text.RESET}. Exiting...")
            sys.exit()
    else:
        print(f"{Text.ERROR}Domain List File '{Text.BLUE}{filename}{Text.RESET}' Not Found.")
        sys.exit()

    return domains.readlines()


# Returns a bool that is whether or not the given domain has ssl
def check_ssl(domain):
        context = ssl.create_default_context()
        
        try:
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    return True
        except ssl.SSLCertVerificationError:
            return False
        except:
            print(f"{Text.ERROR}Error checking SSL. Exiting...")
            sys.exit()


# Writes the table of domains and ssl status to terminal and the file certificate_log.txt
def write_results(results):
    try:
        output = open("certificate_log.txt", 'w')
        for result in results:
            print(result)
            output.write(result + "\n")
    except:
        print(f"{Text.ERROR}Error writing results to {Text.BLUE}certificate_log.txt{Text.RESET}. Exiting...")
        sys.exit()
    
    print(f"\n{Text.SUCCESS}Results were saved to {Text.BLUE}certificate_log.txt{Text.RESET}!")


# Creates the results list and sends it to write_results
if __name__ == '__main__':
    results = ["Status    : Domain","----------:----------------"]

    for domain in read_domains_txt("domains.txt"):
        domain = domain.strip()

        if check_ssl(domain):
            results.append(f"Secure    : {domain}")
        else:
            results.append(f"Insecure  : {domain}")

    write_results(results)

    