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
user=driver.find_element_by_id("username")
user.send_keys('helenlaz@mail.ru')
password_user=driver.find_element_by_id("password")
password_user.send_keys("vladilen0vna")
driver.find_element_by_css_selector('[name=login]').click()
driver.find_element_by_id("menu-item-40").click()
time.sleep(5)
driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/html5-forms/']").click()
some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class= 'product_title entry-title']"), "HTML5 Forms"))
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
time.sleep(5)
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_link_text("HTML").click()
items_count = driver.find_elements_by_class_name("attachment-shop_catalog")
if len(items_count)==3:
    print("3")
else:
    print("no")
driver.find_element_by_id("menu-item-40").click()
status_selector_sort=status_selector.get_attribute("value")
if status_selector_sort=="menu_order":
    print("on")
else:
    print("off")
status_selector = driver.find_element_by_class_name("orderby")
select = Select(status_selector)
status_selector_sort=status_selector.get_attribute("value")
if status_selector_sort=="menu_order":
    print("on")
else:
    print("off")
select.select_by_index(5)
status_selector = driver.find_element_by_class_name("orderby")
select = Select(status_selector)
status_selector_sort=status_selector.get_attribute("value")
if status_selector_sort=="price-desc":
    print("on")
else:
    print("off")
driver.find_element_by_id("menu-item-40").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);") #скролл добавила из-за рекламы
driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/android-quick-start-guide/']").click()
time.sleep(5)
price_old=driver.find_element_by_css_selector(".price >del")
price_old_get_text=price_old.text
assert price_old_get_text=="₹600.00"
price_new=driver.find_element_by_css_selector(".price >ins")
price_new_get_text=price_new.text
assert price_new_get_text=="₹450.00"
face_book=WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div> .images")) )
face_book.click()
exit=WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close ")) )
exit.click()
driver.get("http://practice.automationtesting.in/")
time.sleep(5)
driver.find_element_by_id("menu-item-40").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 300);") #скролл добавила из-за рекламы
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
time.sleep(3)
item=driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
item_get_text=item.text
assert item_get_text=="1 Item"
basket_price=driver.find_element_by_css_selector(".wpmenucart-contents .amount")
basket_price_get_text=basket_price.text
assert basket_price_get_text=="₹180.00"
driver.find_element_by_id("wpmenucartli").click()
subtotal=WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
total=WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹183.60"))
driver.get("http://practice.automationtesting.in/")
time.sleep(5)
driver.find_element_by_id("menu-item-40").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
time.sleep(5)
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=165']").click() # "JS Data Structures and Algorithm" в стоке, добавила другую книгу по js
driver.find_element_by_id("wpmenucartli").click()
time.sleep(5)
driver.find_element_by_css_selector("tbody> .cart_item:nth-child(1)> .product-remove> .remove").click()
time.sleep(3)
driver.find_element_by_link_text("Undo?").click()
input=driver.find_element_by_css_selector("tbody .cart_item:nth-child(1) input")
input.clear()
input.send_keys("3")
driver.find_element_by_css_selector("[value='Update Basket']").click()
input_check=input.get_attribute("value")
assert input_check=="3"
time.sleep(5)
driver.find_element_by_css_selector("[value='Apply Coupon']").click()
error=WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))
driver.get("http://practice.automationtesting.in/")
time.sleep(5)
driver.find_element_by_id("menu-item-40").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
time.sleep(5)
driver.find_element_by_id("wpmenucartli").click()
checkout=WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")) )
checkout.click()
f_name=WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")) )
f_name.send_keys("Elena")
l_name=driver.find_element_by_id("billing_last_name")
l_name.send_keys("Lazareva")
email=driver.find_element_by_id("billing_email")
email.send_keys("helenlaz@mail.ru")
phone=driver.find_element_by_id("billing_phone")
phone.send_keys("89114097511")
driver.find_element_by_id("s2id_billing_country").click()
country=driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("russia")
time.sleep(3)
driver.find_element_by_class_name("select2-results-dept-0").click()
time.sleep(3)
address=driver.find_element_by_id("billing_address_1")
address.send_keys("Prazhskay")
city=driver.find_element_by_id("billing_city")
city.send_keys("Sankt-Petersburg")
state=driver.find_element_by_id("billing_state")
state.send_keys("Russia")
zip=driver.find_element_by_id("billing_postcode")
zip.send_keys("123456")
driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()
text=WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "body"), "Thank you. Your order has been received."))
