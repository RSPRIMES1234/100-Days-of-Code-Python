from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

angela_login_page="https://secure-retreat-92358.herokuapp.com/"



chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)
driver.get(angela_login_page)

first_name=driver.find_element(By.CSS_SELECTOR,"body > form > input.form-control.top")
first_name.click()
first_name.send_keys("Modi")

last_name=driver.find_element(By.CSS_SELECTOR,"body > form > input.form-control.middle")
last_name.click()
last_name.send_keys("Narendra")


email=driver.find_element(By.CSS_SELECTOR,"body > form > input.form-control.bottom")
email.click()
email.send_keys("Modi1111@gmail.com")

button=driver.find_element(By.CSS_SELECTOR,"body > form > button")
button.click()








































































