from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

URL="https://www.speedtest.net/"
PROMISED_DOWN=200
PROMISED_UP=200
CHROME_DR_PTH=""
TWITTER_EMAIL = "ajkalkdjlkadlakj@gmail.com"
TWITTER_PASSWORD = "jikadaklsdhklashjdakldhjasdklh"
TWITTER_URL="https://twitter.com/login?lang=en"

class TwitterComplaint:
    def __init__(self):
        self.down=float("inf")
        self.up=float("inf")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("start-maximized")
        chrome_options.page_load_strategy='none'
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
    def get_speed(self):

        self.driver.get(url=URL)
        self.driver.implicitly_wait(100)
        speed_button = self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        speed_button.click()
        # time.sleep(50)
        refrence_id=self.driver.find_element(by=By.CSS_SELECTOR,value="#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.test-meta > div > div > div.result-item.result-item-inline.result-item-align-center.result-item-id > div.result-data > a")
        self.link=refrence_id.get_attribute("href")
        print(self.link)
        self.up=float(self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.down=float(self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(self.up,self.down)
    def tweet_complaint(self):
        self.driver.get(TWITTER_URL)
        email_enter=self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_enter.send_keys(TWITTER_EMAIL)
        pass_enter=self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_enter.send_keys(TWITTER_PASSWORD)
        login_button=self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
        login_button.click()
        tweet_add=self.driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div')
        tweet_add.click()
        tweet_add.send_keys("@ISP wadu heck bro ur speeds suck")
        tweet=self.driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        tweet.click()


def main():
    complaint=TwitterComplaint()
    complaint.get_speed()
    # time.sleep(100)
    if complaint.up<PROMISED_UP and complaint.down<PROMISED_UP:
        complaint.tweet_complaint()
    # else:
    #     print("GG")




if __name__=="__main__":
    main()
