from helper import Text
import bs4
import requests
import re


# From the blackhat websites gets all presenters from blackhat USA 2000
if __name__ == '__main__':
    # Temporarlly Downloads the website to parse
    res = requests.get("https://www.blackhat.com/html/bh-media-archives/bh-archives-2000.html")
    res.raise_for_status()
    
    # Gets the list of presentations from the webpage
    blackhat = bs4.BeautifulSoup(res.text, 'html.parser')
    presentations = blackhat.select('a[title="Black Hat USA 2000"][href]')
    
    # Gets the presenter names from the list of presentations
    presenters = re.findall(r'([A-Za-z\.]+ *[A-Za-z\.]* *[A-Za-x]*)<', str(presentations)) + re.findall(r'([A-Za-z\.]+ *[A-Za-z\.]* *[A-Za-x]*) \&amp', str(presentations))

    # Prints out the the presenters
    print(f"BlackHat USA 2000 Presenters: ")
    for presenter in presenters:
        print(f"-{Text.BLUE}{presenter}{Text.RESET}")