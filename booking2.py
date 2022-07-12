from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha

import time
import os
import base64



def solveRecaptha2(bookinfo):

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
        ticket_situation = booking_train(code, bookinfo)

        return ticket_situation


def booking_train2(code, bookinfo):

    IDnum = bookinfo.split('\n')[0]
    startwords = bookinfo.split('\n')[1]
    endwords = bookinfo.split('\n')[2]
    ridedatebook = bookinfo.split('\n')[3]
    tripsnums = bookinfo.split('\n')[4]

    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)

    driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query')

    idlocate = driver.find_element(By.XPATH, '//*[@id="pid"]')
    idlocate.send_keys(IDnum)
    try:
        start = driver.find_element(By.XPATH, '//*[@id="startStation"]')
        start.send_keys(startwords)

        end = driver.find_element(By.ID, 'endStation')
        end.send_keys(endwords)

        date = driver.find_element(By.ID,'rideDate1')
        date.clear()
        date.send_keys(ridedatebook)

        trips = driver.find_element(By.ID, 'trainNoList1')
        trips.send_keys(tripsnums)

        driver.find_element(By.ID, 'g-recaptcha-response')
        driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML = '" + code + "'")

        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[4]/input[2]').click()
        
        timle.sleep(2)
        try:
            tripsnum = driver.find_element(By.CLASS_NAME, 'cartlist-id').text
            paidtime = driver.find_element(By.CSS_SELECTOR, 'span.red').text
            ticket_situation = f'訂購完成！{str(tripsnum)}\n請於{str(paidtime)}'
        except:
            ticket_situation = '資料有誤，請重新輸入'
    except:
        ticket_situation = 'idlocate'

    return ticket_situation