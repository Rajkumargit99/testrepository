import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://sqatools.in/dummy-booking-website/")

fromcity_elem = driver.execute_script("return document.getElementById('fromcity')")
fromcity_elem.send_keys("Hyderabad")
time.sleep(2)
dest_city = driver.execute_script('return document.getElementById("destcity")')
dest_city.send_keys("Mumbai")
time.sleep(2)

title = driver.execute_script("return document.title")
print("Title", title)
time.sleep(2)

URL = driver.execute_script("return document.URL")
print("URL", URL)

win_hight = driver.execute_script("return window.outerHeight")
win_width = driver.execute_script("return window.outerWidth")

print("Hight", win_hight, "Width", win_width)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

driver.close()