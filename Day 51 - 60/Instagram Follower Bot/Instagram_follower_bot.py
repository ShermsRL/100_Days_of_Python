from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from InstaFollower import InstaFollower
import time

SIMILAR_ACCOUNT = "playstationasia"
INSTA_USERNAME = "ShermanTayPython"
INSTA_PASSWORD = "password"

instabot = InstaFollower()
instabot.login(INSTA_USERNAME, INSTA_PASSWORD)
time.sleep(15)
instabot.find_followers(SIMILAR_ACCOUNT)
instabot.follow()

