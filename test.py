from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch the browser and navigate to the application
driver = webdriver.Firefox()
driver.get("https://google.com")

# Test Case 1: Attempt XSS by entering a payload in the password field
password_input = driver.find_element("name","q")
password_input.send_keys('hi')
password_input.submit()
# Submit the form
submit_button = driver.find_element("By.CSS_SELECTOR",'button[type="submit"]')
submit_button.click()

# Check for presence of the XSS payload in the response
response = driver.page_source
if '<script>alert("XSS Attack");</script>' in response:
    print("XSS vulnerability detected!")

# Test Case 2: Test for input validation by entering a special character
password_input.clear()
password_input.send_keys('!@#$%^&*()')

# Submit the form
submit_button.click()

# Check for proper handling of special characters in the response
response = driver.page_source
if '!@#$%^&*()' not in response:
    print("Input validation issue detected!")

# Close the browser
driver.quit()
