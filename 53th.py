from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import *
import requests


ZILLOW_CLONE="https://appbrewery.github.io/Zillow-Clone/"
FORM_LINK="https://docs.google.codadadad/eda/1FAIpdQLScL-asd?usp=asdasdasdasdask"
da
##########################################################################################
class AddDataToForm:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("detach", True)
        # chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        self.driver = webdriver.Chrome(options=chrome_options)
    def adddata(self,Address,price,link):
        self.driver.get(FORM_LINK)
        address_input=self.driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(Address)
        price_input = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(price)
        link_input = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input.send_keys(link)
        submit=self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit.click()



##########################################################################################


#
response=requests.get(ZILLOW_CLONE)
response.raise_for_status()

soup=BeautifulSoup(response.text,"html.parser")
property_list=soup.findAll(name="div",class_="StyledPropertyCardDataWrapper")

data_bot=AddDataToForm()

for property in property_list:
    link=property.find(name="a").get("href")
    Address=property.find(name="address").text.strip()
    price=property.find(class_="PropertyCardWrapper__StyledPriceLine").text.strip().replace("+","/").split("/")[0]

    data_bot.adddata(Address,price,link)

# print(property_list)