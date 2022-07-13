from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha

import time
import os


def solveRecaptha2():

    train_booking_pageurl = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/bookingTicket'
    train_booking_sitekey = '6LdHYnAcAAAAAI26IgbIFgC-gJr-zKcQqP1ineoz'

    api_key = os.getenv('APIKEY_2CAPTCHA', '4bca3ca456af17b4be31f166e1ddb8aa')
    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(sitekey=train_booking_sitekey, url=train_booking_pageurl)

    except Exception as e:
        print(e)

    else:
        code = result['code']

        return code


def booking_train2(bookinfo):

    identification = bookinfo.split('\n')[0]
    startwords = bookinfo.split('\n')[1]
    endwords = bookinfo.split('\n')[2]
    ridedatebook = bookinfo.split('\n')[3]
    trips = bookinfo.split('\n')[4]

    # chromeOption = webdriver.ChromeOptions()
    # chromeOption.add_argument("--lang=zh-CN.UTF8")
    # chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    # driver = webdriver.Chrome(chrome_options=chromeOption)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless") #無頭模式
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('blink-settings=imagesEnabled=false') 
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


    driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query')

    
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="pid"]').send_keys(identification)
    driver.find_element(By.XPATH, '//*[@id="startStation"]').send_keys(startwords)
    driver.find_element(By.ID, 'endStation').send_keys(endwords)
    date = driver.find_element(By.ID,'rideDate1')
    date.clear()
    date.send_keys(ridedatebook)
    driver.find_element(By.ID, 'trainNoList1').send_keys(trips)
    
    driver.find_element(By.ID, 'g-recaptcha-response')
    
    code = solveRecaptha2()
   
    driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML = '" + code + "'")
    
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[4]/input[2]').click()

    time.sleep(2)
    ticket_situation = f'進入最後一頁!'
    
    try:
        tripsacu = driver.find_element(By.CLASS_NAME, 'cartlist-id').text
        paidtime = driver.find_element(By.CSS_SELECTOR, 'span.red').text
        ticket_situation = f'訂購完成！{str(tripsacu)}\n請於{str(paidtime)}'

        time.slepp(5)
    except:
        ticket_situation = '資料有誤，請重新輸入'
    
    return ticket_situation