from helper import Text
import scanner


# Checks compatibility, gets all connected networks and run an arp scan on each network
if __name__ == '__main__':
    scanner.check_os_and_permissions()

    networks = scanner.get_networks()
    print(f"{Text.INFO}This device is connected to {Text.BLUE}{len(networks)}{Text.RESET} network(s): {Text.BLUE}{networks}{Text.RESET}")

    for network in networks:
        print(f"{Text.INFO}ARP Scanning the {Text.BLUE}{network}{Text.RESET} network.")
        scanner.arp_scan(network)