import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

load_dotenv(".env")

print("INSTAGRAM FOLLOWING BOT!")
SIMILAR_ACCOUNT=input("Enter the username you want to follow: ")


USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")



class Instafollower:
    def __init__(self):
        options = Options()
        options.add_argument("--incognito")
        self.driver=webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 5)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        username_box=self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='text']")))
        username_box.send_keys(USERNAME)
        time.sleep(3.5)

        password_box=self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='password']")))
        password_box.send_keys(PASSWORD)

        time.sleep(3.3)
        password_box.send_keys(Keys.ENTER)
        time.sleep(4.2)

        try:
            save_login_prompt = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and text()='Not now']"))
                )
            time.sleep(1.1)
            save_login_prompt.click()
        except:
            pass
        time.sleep(1.4)

        try:
            notification_prompt = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not')]"))
            )
            notification_prompt.click()
        except:
            pass
        time.sleep(2.8)
        search=self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"[aria-label='Search']"))
        )
        search.click()
        time.sleep(3.3)

        search_input=self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"[aria-label='Search input']"))
        )
        time.sleep(2.5)
        search_input.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)

    def follow_account(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        followings = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Follow')]")
            )
        )
        time.sleep(1.8)
        followings.click()
        time.sleep(10)



instabot=Instafollower()
instabot.login()
instabot.follow_account()
