from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


# cookie=driver.find_element(By.CSS_SELECTOR,"#money")
cookies = driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]")
store_=driver.find_elements(By.CSS_SELECTOR,"#store")
for x in store_:
    print(x.find_element())
# cookies=driver.find_element(By.CSS_SELECTOR,"#money").text
# time.sleep(10)
# enlgish=driver.find_element(By.CSS_SELECTOR,"#langSelect-EN")
# enlgish.click()
while True:

    print(cookies)
    for buy in store_list[::-1]:
        if int(buy.text)>=int(cookies):
            buy.click()
    cookie.click()



















































