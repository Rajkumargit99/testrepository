from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/login-page/")

def implicit_wait_practice():
    driver.implicitly_wait(15)
    t1 = time.time()

    try:
        driver.find_element(By.ID, "email").send_keys("user@gmail.com")
        driver.find_element(By.NAME, "pass").send_keys("User@123")
    except Exception as e:
        print(e)
    t2 = time.time()

    print("Total time:", t2-t1)

implicit_wait_practice()


def explicit_wait_practice():
    wait = WebDriverWait(driver, 10)
    t1 = time.time()
    try:
        username = wait.until(ec.element_to_be_clickable((By.NAME, "email")))
        username.send_keys("user@gmail.com")
        password = wait.until(ec.element_to_be_clickable((By.NAME, "pass")))
        password.send_keys("user@123")

    except Exception as e:
        print(e)

    t2 = time.time()

    print("Total time:", t2-t1)

explicit_wait_practice()