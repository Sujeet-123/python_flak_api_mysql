from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.google.com")
time.sleep(5)


driver.maximize_window()
time.sleep(100)


def check_links():
    driver.f


