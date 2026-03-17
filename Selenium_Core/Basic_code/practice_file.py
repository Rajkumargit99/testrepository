from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://sqatools.in/login-page/")
driver.find_element(By.LINK_TEXT, "Login Page").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Email address or phone number']").send_keys("testuser@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("user@12345")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)
