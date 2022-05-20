from helper import Text
import bs4
import requests
import re
import sys


# Temporarlly Downloads the blackhat website to parse
def get_blackhat_html():
    try:
        res = requests.get("https://www.blackhat.com/html/bh-media-archives/bh-archives-2000.html")
        res.raise_for_status()
    except:
        print(f"{Text.ERROR}Error Downloading Blackhat website. Exiting...")
        sys.exit()
    
    return res


# From the html from the blackhat site parses out the presenters
def get_presenters(bh_html):
    # Gets the list of presentations from the webpage
    try:        
        blackhat = bs4.BeautifulSoup(bh_html.text, 'html.parser')
        presentations = blackhat.select('a[title="Black Hat USA 2000"][href]')
    except:
        print(f"{Text.ERROR}Error Parsing Blackhat website. Exiting...")
        sys.exit()

    # Returns the presenter names from the list of presentations
    return re.findall(r'([A-Za-z\.]+ *[A-Za-z\.]* *[A-Za-x]*)<', str(presentations)) + re.findall(r'([A-Za-z\.]+ *[A-Za-z\.]* *[A-Za-x]*) \&amp', str(presentations))


# From the blackhat websites gets all presenters from blackhat USA 2000
if __name__ == '__main__':
     # Prints out the the presenters from blackhat USA 200
    print(f"BlackHat USA 2000 Presenters: ")
    for presenter in get_presenters(get_blackhat_html()):
        print(f"-{Text.BLUE}{presenter}{Text.RESET}")