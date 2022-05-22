from helper import Text
import os.path as path
import socket
import sys
import ssl


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


# Returns a bool that is of whether or not the given domain has ssl
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

    