import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
time.sleep(5)
emaile=driver.find_element_by_id("reg_email")
emaile.send_keys('helenlaz@mail.ru')
password=driver.find_element_by_id("reg_password")
password.send_keys("vladilen0vna")
driver.find_element_by_css_selector('[name=register]').click()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
time.sleep(5)
user=driver.find_element_by_id("username")
user.send_keys('helenlaz@mail.ru')
password_user=driver.find_element_by_id("password")
password_user.send_keys("vladilen0vna")
driver.find_element_by_css_selector('[name=login]').click()
some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#body"), "Logout"))