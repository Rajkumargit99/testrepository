import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = "Edge"
driver = None

if browser == "Chrome":
    driver = webdriver.Chrome()
elif browser == "Firefox":
    driver = webdriver.Firefox()
elif browser == "Edge":
    driver = webdriver.Edge()

driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.booking.com/")
time.sleep(5)

try:
    driver.find_element(By.XPATH, "//button[@aria-label='Dismiss sign-in info.']").click()
except Exception as e:
    print(e)

input_field = driver.find_element(By.XPATH, "//input[@aria-label='Where are you going?']")
input_field.click()
time.sleep(3)
input_field.send_keys("Hyderabad")
option = driver.find_element(By.LINK_TEXT, "Hyderabad")
option.screenshot("option_snap.png")
option.click()

time.sleep(3)
driver.close()