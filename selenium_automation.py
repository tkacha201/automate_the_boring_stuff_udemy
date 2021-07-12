import time
from selenium import webdriver

#opens up laptop.bg
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://laptop.bg/');
driver.maximize_window()

#searches for price of macbook
to_website = driver.find_element_by_css_selector('#branding > div > ul > li > a')
to_website.click()
search_box = driver.find_element_by_css_selector('#q')
search_box.send_keys('macbook')
search_box.submit()


#filter best sellers
filter_best_sellers = driver.find_element_by_class_name('bestsellers')
filter_best_sellers.click()

#get price of first item
first_laptop_price = driver.find_element_by_css_selector('#product_86230 > article > div.price-container > span.price')
print('The first laptop price is ' + first_laptop_price.text)

time.sleep(5) # Let the user actually see something!

driver.quit()

