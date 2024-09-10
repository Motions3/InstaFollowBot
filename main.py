import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
from dotenv import load_dotenv

load_dotenv()

# Environment Constants
SIMILAR_ACCOUNT = "chrishemsworth"
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        # Login Access
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div['
                                                    '2]/div/button[1]').click()
        sleep(3)
        username = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTAGRAM_PASSWORD, Keys.RETURN)
        sleep(10)

    def find_followers(self):
        # Directs you to targetted account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        sleep(5)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='followers').click()
        sleep(5)

        # Scroll popup to unlock all followable accounts
        scrollable_popup = self.driver.find_element(by=By.XPATH,
                                                    value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
        sleep(3)

    def follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR,
                                            value="div.x1dm5mii > div > div > div > div > div > button")
        for button in buttons:
            try:
                print(button.text)
                button.click()
                sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
