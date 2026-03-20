import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://sqatools.in/dummy-booking-website/")

def select_by_visible_text_label(label):
    dropdown = driver.find_element(By.ID, "billing_country")
    time.sleep(1)
    select_obj = Select(dropdown)
    time.sleep(1)
    select_obj.select_by_visible_text(label)
    time.sleep(2)

select_by_visible_text_label("India")

def select_by_option_value(optional_value):
    dropdown = driver.find_element(By.ID, "billing_country")
    time.sleep(1)
    select_obj = Select(dropdown)
    time.sleep(1)
    select_obj.select_by_value(optional_value)
    time.sleep(2)

select_by_option_value("BD")

def select_by_index_position(index_value):
    dropdown = driver.find_element(By.ID, "billing_country")
    time.sleep(1)
    select_obj = Select(dropdown)
    time.sleep(1)
    select_obj.select_by_index(index_value)
    time.sleep(2)

select_by_index_position(2)

def locate_element_with_dynamic_dropdown():
    driver.get("https://www.booking.com")
    driver.maximize_window()
    time.sleep(1)
    input_f = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
    input_f.click()
    input_f.send_keys("Hyderabad")
    time.sleep(1)
    dpwn_parent = driver.find_element(By.XPATH, "//div[@id='autocomplete-results']//ul")
    dpwn_parent.find_element(By.XPATH, "//*[text()='Hyderabad']").click()
    time.sleep(4)

locate_element_with_dynamic_dropdown()
