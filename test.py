from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


def booking_train2(bookinfo):
    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument('–first run')
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)

    driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query')

   return 'OK'