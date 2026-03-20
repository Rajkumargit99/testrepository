import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
action = ActionChains(driver)

def hover_to_the_element():
    menu_item = driver.find_element(By.XPATH, "//div[@id='menu']//a[text()='Tester’s Hub']")
    action.move_to_element(menu_item).perform()
    time.sleep(2)

    sub_menu_item = driver.find_element(By.XPATH, "//div[@id='menu']//span[text()='Demo Testing Site']")
    action.move_to_element(sub_menu_item).perform()
    time.sleep(2)

    sub2_menu_items = driver.find_element(By.XPATH, "//div[@id='menu']//span[text()='AlertBox']")
    action.move_to_element(sub2_menu_items).click(sub2_menu_items).perform()
    time.sleep(2)

# hover_to_the_element()

def drag_drop_element():
    frame_elem = driver.find_element(By.XPATH, "//iframe[contains(@src, 'photo-manager')]")
    driver.switch_to.frame(frame_elem)

    image1 = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//parent::li")
    trash_elem = driver.find_element(By.ID, "trash")

    action.drag_and_drop(image1, trash_elem).perform()
    time.sleep(2)

    for i in range(2, 5):
        image = driver.find_element(By.XPATH, f"//h5[text()='High Tatras {i}']//parent::li")
        trash_elem = driver.find_element(By.ID, "trash")
        action.drag_and_drop(image, trash_elem).perform()
        time.sleep(2)

#drag_drop_element()

def scroll_to_element_page():
    bottom_elem = driver.find_element(By.XPATH, "//div[@id='powered']/a[text()=' GlobalSQA']")
    action.scroll_to_element(bottom_elem).perform()
    time.sleep(5)
    action.click(bottom_elem).perform()
    time.sleep(2)

# scroll_to_element_page()

def scroll_to_with_amount():
    action.scroll_by_amount(500, 500).perform()
    time.sleep(2)

# scroll_to_with_amount()