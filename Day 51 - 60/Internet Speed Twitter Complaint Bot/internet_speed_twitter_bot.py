from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import time


TWITTER_EMAIL = "shermantaymkmk@gmail.com"
TWITTER_PASSWORD = "password"

internet_speed_twitter_bot = InternetSpeedTwitterBot()
speed = internet_speed_twitter_bot.get_internet_speed()
internet_speed_twitter_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, speed[0], speed[1])
