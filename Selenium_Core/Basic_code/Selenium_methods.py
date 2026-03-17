from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://sqatools.in/dummy-booking-website/")

print("current url:", driver.current_url)

print("title:", driver.title)

heading = driver.find_element(By.TAG_NAME, "h1").text
print("heading:", heading)

radio_button = driver.find_element(By.ID, "oneway")

print(radio_button.is_displayed())
print(radio_button.is_enabled())
print(radio_button.is_selected())
time.sleep(2)
radio_button.click()
time.sleep(2)
print(radio_button.is_selected())
time.sleep(2)

# back
driver.back()
time.sleep(2)
#forward
driver.forward()
time.sleep(2)
#refresh
driver.refresh()
time.sleep(2)

#close
driver.close()