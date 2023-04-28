from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

linkedin_address = "url here"
email = "email here"
password = "password here"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)
driver.get("https://linkedin.com")
driver.implicitly_wait(2)
username_field = driver.find_element(By.ID, 'session_key')
username_field.send_keys(email)
password_field = driver.find_element(By.ID, 'session_password')
password_field.send_keys(password)
submit = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-btn--full-width')
submit.submit()