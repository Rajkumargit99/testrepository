from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)

driver.get("https://www.instagram.com")
time.sleep(2)

driver.find_element(By.NAME, "email").send_keys("raj_123")
driver.find_element(By.NAME, "pass").send_keys("Raj@123")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Forgotten password?").click()
time.sleep(2)