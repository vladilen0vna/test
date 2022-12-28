import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/selenium-ruby/']").click()
time.sleep(5)
driver.find_element_by_class_name("reviews_tab").click()
driver.find_element_by_class_name("star-5").click()
review=driver.find_element_by_id("comment")
review.send_keys("nice book")
name=driver.find_element_by_id("author")
name.send_keys("Elena")
email=driver.find_element_by_id("email")
email.send_keys('helenlaz@mail.ru')
driver.find_element_by_id("submit").click()