from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)
driver.get("https://linkedin.com")
username = driver.find_element(By.ID, "session_key")
username.send_keys("hahahahahhahahahahha")
password = driver.find_element(By.ID, 'session_password')
password.send_keys("hashdfahsdf")