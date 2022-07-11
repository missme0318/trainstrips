from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
from twocaptcha import TwoCaptcha

import time
import os

def solveRecaptha(sitekey, pageurl):
    api_key = os.getenv('APIKEY_2CAPTCHA', '4bca3ca456af17b4be31f166e1ddb8aa')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=pageurl)

    except Exception as e:
        print(e)

    else:
        return result