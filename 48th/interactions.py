from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver= webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number_article=driver.find_element(By.CSS_SELECTOR,"#articlecount > a:nth-child(1)").text
search_lens=driver.find_element(By.CSS_SELECTOR,"#p-search > a > span.vector-icon.mw-ui-icon-search.mw-ui-icon-wikimedia-search")
search_lens.click()
search=driver.find_element(By.CLASS_NAME,"cdx-text-input__input")
search.click()
search.send_keys("Modi",Keys.ENTER)





















