from helper import Text
from browser import *


# Gets url from user, lanuches firefox,  then navigates to the url
if __name__ == '__main__':
    print(f"{Text.INFO}This script requires that {Text.BLUE}geckodriver{Text.RESET} is in the PATH")
   
    url = get_url()
    firefox_instance = lanuch_firefox()
    navigate_to(firefox_instance, url)