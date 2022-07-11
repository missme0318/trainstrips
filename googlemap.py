import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

def web_get_address(web):
    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)
    
    driver.get(web)

    try:
        address = driver.find_element(By.CLASS_NAME, 'm6QErb .rogA2c').text
    except:
        address = '無地址提供'
        
    try:
        time = driver.find_element(By.CLASS_NAME, 'm6QErb .OqCZI').text.split('\n')[0].split('⋅')[0]
    except:
        time = '無提供時間'
    driver.quit()
    return address, time

def input_wanted(search):
    address, limittime = [], []
  
    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)
    
    # driver.set_window_size(1024, 960)

    driver.get(f'https://www.google.com.tw/maps/search/{search}/@23.546162,120.6402133,8z?hl=zh-TW/data=!4m4!2m3!5m1!2e1!6e5')
    
    driver.implicitly_wait(2)

    operation = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
    
    name_type = operation.find_elements(By.CLASS_NAME, 'Nv2PK')
    websites = operation.find_elements(By.TAG_NAME, 'a')

    name = [i.text.split('\n')[0] for i in name_type]
    comment = [i.text.split('\n')[1][:3] for i in name_type]
    website = [str(i.get_attribute('href')) for i in websites]


    web_get_address(website[0])
    # for i in website:
    #     addr, time = web_get_address(str(i))
    #     address.append(addr)
    #     limittime.append(time)

    mapinfo = ''
    for i in zip(name, comment, website):
        count = int(name.index(i[0]))
        if count < 3 :
            mapinfo += f'{i[0]}\n{i[1]}顆星\n{i[2]}\n\n'

    driver.quit()

    return mapinfo

