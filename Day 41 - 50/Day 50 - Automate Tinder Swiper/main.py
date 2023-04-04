from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

FACEBOOK_EMAIL = "shermantaymk@gmail.com"
FACEBOOK_PASSWORD = "-"

chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")
base_window = driver.window_handles[0]
time.sleep(15)


accept_cookies = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button")
accept_cookies.click()
time.sleep(5)

tinder_log_in = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span"
)
tinder_log_in.click()
time.sleep(5)

facebook_log_in = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]")
facebook_log_in.click()
time.sleep(25)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
email.send_keys(FACEBOOK_EMAIL)

password = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
password.send_keys(FACEBOOK_PASSWORD)

facebook_log_in_sub = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]")
facebook_log_in_sub.click()
time.sleep(10)

# continue_with_account = driver.find_element(
#     By.XPATH,
#     "/html/body/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/span/span")
# continue_with_account.click()

driver.switch_to.window(base_window)

allow_location_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
allow_location_button.click()
time.sleep(3)

not_interested_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[2]/span")
not_interested_button.click()
time.sleep(10)

pictures = driver.find_element(
    By.XPATH,
    "/html/body")
count = 0
while count < 100:
    pictures.send_keys(Keys.ARROW_LEFT)
    time.sleep(1)
    count += 1
