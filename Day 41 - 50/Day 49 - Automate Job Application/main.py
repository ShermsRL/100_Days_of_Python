from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102454443&keywords=python%20developer&location=Singapore&sortBy=R")

time.sleep(3)
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
time.sleep(3)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("shermantaymk@gmail.com")
password.send_keys("Shertayman1998")

login_page_sign_in = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
login_page_sign_in.click()
time.sleep(3)

dismiss_message = driver.find_element(By.XPATH, "/html/body/div[6]/aside/div[1]/header/div[3]/button[2]")
dismiss_message.click()

# Follow and save job tasking

# save_job = driver.find_element(
#     By.XPATH,
#     "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button")
# save_job.click()
#
# div_element = driver.find_element(
#         By.XPATH,
#         "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div")
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div_element)
#
# time.sleep(5)
#
# follow_job = driver.find_element(
#     By.XPATH,
#     "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[6]/section/section/div[1]/div[1]/button/span")
# follow_job.click()

# Scroll through the job and submit application
# div_element = driver.find_element(
#         By.XPATH,
#         "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[5]")
# driver.execute_script("arguments[0].scrollIntoView()", div_element)

num = 1
while num < 26:
        for num in range(num, num+4):
                job = driver.find_element(By.XPATH, f"/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{num}]")
                job.click()
                easy_apply = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button")
                easy_apply.click()
                cancel = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
                cancel.click()
                discard = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]")
                discard.click()
                # to apply for multiple jobs using easy apply, add in if else condition to check if can straight away submit application
                num += 1
        div_element = driver.find_element(
                By.XPATH,
                f"/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{num}]")
        driver.execute_script("arguments[0].scrollIntoView()", div_element)
        time.sleep(2)
        num += 4
