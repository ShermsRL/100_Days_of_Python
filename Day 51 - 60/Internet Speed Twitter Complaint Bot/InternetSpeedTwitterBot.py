from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.PROMISED_UPLOAD_SPEED = 10
        self.PROMISED_DOWNLOAD_SPEED = 100
        self.chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"

    def get_internet_speed(self):
        driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        driver.get("https://www.speedtest.net/")
        time.sleep(30)

        start_button = driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]"
        )
        start_button.click()
        time.sleep(60)

        download_speed = driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        upload_speed = driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text
        return download_speed, upload_speed

    def tweet_at_provider(self, twitteremail, twitterpassword, downloadspeed, uploadspeed):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path=self.chrome_driver_path, chrome_options=chrome_options)
        driver.get("https://twitter.com/i/flow/login")
        time.sleep(15)

        email = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label"
        )
        email.send_keys(twitteremail)

        next_button = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"
        )
        next_button.click()
        time.sleep(2)

        sus_activity = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label"
        )
        sus_activity.send_keys("97622109")
        time.sleep(2)

        sus_activity_next = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div"
        )
        sus_activity_next.click()
        time.sleep(2)

        password = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label"
        )
        password.send_keys(twitterpassword)
        time.sleep(2)

        login_button = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div"
        )
        login_button.click()
        time.sleep(15)

        tweet_btn = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div"
        )
        tweet_btn.click()
        time.sleep(2)
        tweet_field = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div"
        )
        tweet_field.send_keys(f"Hey internet provider, why is my internet speed {downloadspeed}down/{uploadspeed}up "
                              f"when i pay for 100down/10up?")

        send_tweet = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div"
        )
        send_tweet.click()
