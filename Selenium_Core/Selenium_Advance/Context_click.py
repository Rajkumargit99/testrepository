import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

import pyautogui
action = ActionChains(driver)
def context_click_or_right_click():
    driver.get("https://automationexercise.com/")
    button_list = driver.find_elements(By.XPATH, "//button[text()='Test Cases']")
    for elem in button_list:
        try:
            action.context_click(elem).perform()
            time.sleep(2)
            pyautogui.press("up")
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(2)
        except Exception as e:
            print(e)

context_click_or_right_click()

