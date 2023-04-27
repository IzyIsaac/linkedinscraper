from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the email and password variables
email = "your_email_address"
password = "your_password"

# Launch Chrome using the ChromeDriver
driver = webdriver.Chrome()

# Navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Find the email and password fields and fill them in
email_field = driver.find_element_by_id("username")
email_field.send_keys(email)

password_field = driver.find_element_by_id("password")
password_field.send_keys(password)

# Submit the login form
password_field.submit()

# Wait for the page to load
driver.implicitly_wait(10)

# Verify that the user is logged in by checking the page title
if "LinkedIn" in driver.title:
    print("Login Successful!")
else:
    print("Login Failed.")
    
# Close the browser
driver.close()