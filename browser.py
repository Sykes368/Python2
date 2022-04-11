from helper import Text
from selenium import webdriver
import re


# Gets url from user and verifies the input is in a valid url format
def get_url():
    while(True):
        given_url = input(f"Enter website url [Format: www.<url>.com]:{Text.BLUE} ")
        url_regex = re.compile("www.[-a-zA-Z0-9@:%._\+~#=]+.com")

        if url_regex.match(given_url):
            url = "https://" + given_url
            return url

        # Allows user to exit by entering exit as the url
        elif given_url == "exit":
            exit(0)
        
        # Notifies about the invalid URL 
        print(f"{Text.WARN}{Text.YELLOW}Invalid URL.{Text.RESET} URL must be in '{Text.BLUE}www.<url>.com{Text.RESET}' format. ex: '{Text.BLUE}www.google.com{Text.RESET}'")


# Lanuches a firefox instance and returns the browser instance
def lanuch_firefox():
    print(f"{Text.INFO}Lanuching Firefox...")
    try:    
        browser = webdriver.Firefox()
        type(browser)
        print(f"{Text.SUCCESS}Firefox Lanuched Successfully")
        return browser
    except:
        print(f"{Text.ERROR}Failed to lanuch Firefox")

# Given a valid url and browser instance. Navigates browser to given url
def navigate_to(browser_instance, url):
    print(f"{Text.INFO}Navigating to '{Text.BLUE}{url}{Text.RESET}'")
    try:
        browser_instance.get(url)
        print(f"{Text.SUCCESS}Navigation Successful")
    except:
        print(f"{Text.ERROR}Failed to navigate to given URL")