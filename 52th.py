from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

IG_EMAIL="singumiku@gmail.com"
IG_PASS="mikumiku1111"
IG_LINK="https://www.instagram.com/"



class IgFollowerBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(100)


    def login(self):
        self.driver.get(url=IG_LINK)
        email_enter = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_enter.send_keys(IG_EMAIL)
        pass_enter = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_enter.send_keys(IG_PASS)
        login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]')
        login_button.click()
        time.sleep(5)
        self.driver.get(url=IG_LINK)
        nono = self.driver.find_element(by=By.XPATH,
                                        value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        nono.click()
    def find_followers(self):
        self.driver.get("https://www.instagram.com/narendramodi/followers")

        followers_button=self.driver.find_element(by=By.XPATH,value='//*[@id="mount_0_0_NW"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
        followers_button.click()
        for i in range(50):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)



    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


def main():
    follower=IgFollowerBot()
    follower.login()
    follower.find_followers()
    follower.follow()

if __name__=="__main__":
    main()
























































































