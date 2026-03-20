import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# driver.get("https://www.google.com")
# time.sleep(1)
# driver.find_element(By.XPATH, '//textarea[@jsname="yZiJbe"]').send_keys("goibibo")
# driver.find_element(By.XPATH, '//div[@class="zgAlFc"]').Search()
# driver.find_element(By.LINK_TEXT, "Best Flight Offers on Goibibo - Book Flights and Hotels").click()

driver.get("https://www.goibibo.com/")

try:
    driver.find_element(By.XPATH, '//span[@class="sc-koXPp bDtzaf"]').click()
except Exception as e:
    print(e)
time.sleep(2)
from_b = driver.find_element(By.XPATH, '//input[@placeholder="From"]')
from_b.click()
from_b.send_keys("Hyderabad").Select()
time.sleep(2)

to_b = driver.find_element(By.XPATH, '//input[@placeholder="To"]')
to_b.click()
to_b.send_keys("Delhi").Select()
time.sleep(2)

