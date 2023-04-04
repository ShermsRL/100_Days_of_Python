from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

language = driver.find_element(By.ID, "langSelect-EN")
language.click()
time.sleep(10)
dismiss = driver.find_element(By.XPATH, "/html/body/div[1]/div/a[1]")
dismiss.click()

time.sleep(10)
cookie = driver.find_element(By.ID, "bigCookie")
cursor_upgrade = driver.find_element(By.ID, "product0")
grandma_upgrade = driver.find_element(By.ID, "product1")
farm_upgrade = driver.find_element(By.ID, "product2")

upgrade_checker = 0

while True:
    cookie.click()
    if cursor_upgrade.is_displayed() and cursor_upgrade.is_enabled():
        cursor_upgrade.click()
    if grandma_upgrade.is_displayed() and grandma_upgrade.is_enabled():
        grandma_upgrade.click()
    if farm_upgrade.is_displayed() and farm_upgrade.is_enabled():
        farm_upgrade.click()
    upgrade_checker += 1
    if upgrade_checker >= 15:
        store_upgrade = driver.find_element(By.ID, "upgrade0")
        if store_upgrade.is_displayed() and store_upgrade.is_enabled():
            store_upgrade.click()

#implement a function that check the upgrade checker, if its high enough, stop upgrading cursor




