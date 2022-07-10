import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


def input_wanted(search):
    address, limittime = [], []
  
    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)
    
    # driver.set_window_size(1024, 960)

    driver.get(f'https://www.google.com.tw/maps/search/{search}/@23.546162,120.6402133,8z?hl=zh-TW/data=!4m4!2m3!5m1!2e1!6e5')
    

    #driver.maximize_window()

    driver.implicitly_wait(2)

    operation = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
    
    name_type = operation.find_elements(By.CLASS_NAME, 'Nv2PK')
    name = [i.text.split('\n')[0] for i in name_type]


    driver.quit()

    return name[0]