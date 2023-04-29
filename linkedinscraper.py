"""
linkedinscraper: A Python module for scraping LinkedIn.com


"""
from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv

__version__ = '0.1.0'

class LinkedInScraper:
    """
    A class for scraping data from LinkedIn
    """

    def __init__(self, username, password, headless=True, detach=False):
        """
        Initializes the LinkedInScraper class. Opens a new Selenium session

        :param username: LinkedIn username
        :param password: LinkedIn password
        :param headless: [optional] Use Selenium in headless mode. Default True
        :param detach: [optional] Detach selenium session so it stays open after
            execuion ends
        """
        self.username = username
        self.password = password
        # Track if the selenium session is logged in to LinkedIn
        self.logged_in = False

        # Create a selenium session
        options = Options()
        if headless:
            options.headless = True
        if detach:
            options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)


    def login(self):
        """
        Logs into LinkedIn with the provided username and password.

        :returns boolean: True if login successful, False otherwise
        """

        # Check if we are already logged in. linkedin.com/feed is only
        # accessible by a logged in user
        self.driver.get("https://linkedin.com/feed") 
        self.driver.implicitly_wait(2)
        if self.driver.current_url == "https://linkedin.com/feed":
            self.logged_in = True
            return True
        
        # Navigate to LinkedIn and login
        self.driver.get("https://linkedin.com")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, 'session_key').send_keys(self.username) # Enter username
        self.driver.find_element(By.ID, 'session_password').send_keys(self.password) # Enter password
        # Submit login form
        self.driver.find_element( 
            By.XPATH, 
            "//button[@data-id='sign-in-form__submit-btn' and contains(text(), 'Sign in')]"
        ).submit()
        self.driver.implicitly_wait(2)

        # Validate we are logged in
        self.driver.get("https://linkedin.com/feed") 
        self.driver.implicitly_wait(2)
        print(self.driver.current_url)
        if self.driver.current_url == "https://www.linkedin.com/feed/":
            self.logged_in = True
            return True
        self.logged_in = False
        raise AttributeError("Could not login to LinkedIn. Is your email and password correct?")


    def get_profile(self, profile_url):
        """
        Scrapes data from a LinkedIn profile

        :param profile_url: The URL of the LinkedIn profile to scrape
        :return: A dictionary containing scraped data from the profile
        """
        # Check if we are logged in
        if not self.logged_in:
            raise AttributeError("LinkedIn not logged in. Use login() to login before getting profile data")

        # Initialize a dict to store profile data
        profile = {}

        # Navigate to the profile
        self.driver.get(profile_url)
        self.driver.implicitly_wait(3)

        # Get name

        # Get headline

        # Get contact info

        # Get profile created year

        # Get current job title

        # Get current employer

        # Get about
        profile['about'] = self.driver.find_element(
            By.XPATH,
            "//div[@id='about']//following-sibling::div[2]//descendant::span[@aria-hidden='true']"
        ).text

        # Get experience

        # Get education

        # Get volunteering

        # Get skills

        # Get awards

        # Get languages

        # Get all sorts of other stuff. The list could go on for ages! 
        # This method should be for getting data from a linkedin profile, not
        # from companies or other parts of linkedin


# CLI version of module
def main():
    import argparse
    import sys
    import getpass

    help = """Scrapes interesting data from LinkedIn profile and exports it to a .json file. 
    usage: linkedinscraper.py profile_url [-o OUT_FILE]

    positional arguments:
      profile_url         LinkedIn profile URL to scrape.

    optional arguments:
      -h, --help          Show this help message and exit.
      -o OUT_FILE, --out_file OUT_FILE
                          The output file to write the scraped data to. default profile.json
    """
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('profile_url', metavar='profile_url', type=str, nargs='+')
    parser.add_argument('-o', '--out_file', metavar='out_file', type=str)
    args = parser.parse_args()

    # Check for creds in .env. If they are not there, prompt for creds 
    load_dotenv()
    username = environ['LINKEDIN_USERNAME']
    password = environ['LINKEDIN_PASSWORD']
    if username == None or password == None:
        print("LinkedIn username/password not found in environment variables")
        username = input("LinkedIn Email: ", type=str)
        password = getpass.getpass("Password: ", type=str)

    # Try to scrape a profile using LinkedInScraper
    try:
        scraper = LinkedInScraper(username, password, headless=False, detach=True)
        scraper.login()
        profile = scraper.get_profile(args.profile_url)
        print(profile)
    except Exception as error:
        print(error)
    
if __name__ == "__main__":
    main() 