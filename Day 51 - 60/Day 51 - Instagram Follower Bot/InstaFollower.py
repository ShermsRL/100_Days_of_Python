from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
import time

class InstaFollower:
    def __init__(self):
        self.chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, chrome_options=chrome_options)
        self.handle = 0

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/")
        time.sleep(10)

        input_username = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label"
        )
        input_username.send_keys(username)

        input_password = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label"
        )
        input_password.send_keys(password)
        input_password.send_keys(Keys.ENTER)

    def find_followers(self, account):
        self.driver.get(f"https://www.instagram.com/{account}")
        time.sleep(15)

        followers = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a"
        )
        followers.click()
        time.sleep(10)

        # test_btn = self.driver.find_element(
        #     By.XPATH,
        #     "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[1]/div/div[2]/button/div"
        # )
        # test_btn.click()
        # num = 6
        # while True:
        #     follower_list = self.driver.find_element(
        #         By.XPATH,
        #         f"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{num}]"
        #     )
        #     self.driver.execute_script("arguments[0].scrollIntoView()", follower_list)
        #     num += 6
        #     time.sleep(2)

    def follow(self):
        # num = 1
        # while num != 7:
        #     follow_button = self.driver.find_element(
        #         By.XPATH,
        #         f"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{num}]/div/div[2]/button"
        #     )
        #     follow_button.click()
        #     time.sleep(2)
        #     num += 1
        follower_list = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div"

        )
        # follow_button = self.driver.find_element(By.TAG_NAME, "div")
        # if follow_button in follower_list and follow_button.text == "Follow":
        #     follow_button.click()
        while True:
            follow_button = follower_list.find_element(By.CLASS_NAME, "_acan._acap._acas")
            try:
                follow_button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]"
                )
                cancel_button.click()
            finally:
                time.sleep(3)