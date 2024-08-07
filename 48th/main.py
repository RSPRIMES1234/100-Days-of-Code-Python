from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver= webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
list=driver.find_elements(By.CSS_SELECTOR,"#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li")
event_dict={}
for x,value in enumerate(list):
    date=value.find_element(By.CSS_SELECTOR,"time").get_attribute("datetime").split("T")[0]
    name=value.find_element(By.CSS_SELECTOR,"a").text
    event_dict[x]={"time":date,"name":name}


print(event_dict)




driver.close()













































































