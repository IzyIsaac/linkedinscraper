from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
profile_url = input("Please paste the linkedin URL you want to scrape: ")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get("https://linkedin.com")
driver.implicitly_wait(2)
username_field = driver.find_element(By.ID, 'session_key')
username_field.send_keys(environ['LINKEDIN_USERNAME'])
password_field = driver.find_element(By.ID, 'session_password')
password_field.send_keys(environ['LINKEDIN_PASSWORD'])
submit = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-btn--full-width')
submit.submit()
driver.implicitly_wait(5)
driver.get(profile_url)
driver.implicitly_wait(5)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
about_div = soup.find('div', {"id": "about"})
print(about_div)