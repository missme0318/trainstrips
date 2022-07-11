from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
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
    

# 訂票

def booking_train(bookinfo):
    tickey_situation = 'nonnon'
     
    IDnum = bookinfo.split('\n')[0]
    startwords = bookinfo.split('\n')[1]
    endwords = bookinfo.split('\n')[2]
    ridedatebook = bookinfo.split('\n')[3]
    tripsnums = bookinfo.split('\n')[4]

    train_booking_pageurl = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/bookingTicket'
    train_booking_sitekey = '6LdHYnAcAAAAAI26IgbIFgC-gJr-zKcQqP1ineoz'
    result = solveRecaptha(train_booking_sitekey, train_booking_pageurl)
    code = result['code']

    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)


    railway = driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query')
        #driver.maximize_window()
    try:
        driver.set_window_size(1600,1024)

     
        
        idlocate = driver.find_element(By.XPATH, '//*[@id="pid"]')
        idlocate.send_keys(IDnum)


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
        driver.execute_script(
            "document.getElementById('g-recaptcha-response').innerHTML = '" + code + "'")

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[4]/input[2]').click()

        time.sleep(3)
        
        try:
            soldout= '均無符合條件車次，請調整訂票條件'
            soldout in driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/h4/strong').text
            tickey_situation = soldout

        except:
            try: 
                driver.find_element(By.XPATH, '//*[@id="order"]/div[3]/button').click()
                tickey_situation = 'stop1'
            except:
                tickey_situation = 'stop2'

                time.sleep(3)

                payment = driver.find_element(By.ID, 'paymentMethod')
                cash = Select(payment).options[1]
                Select(payment).select_by_visible_text(cash.text)

                time.sleep(3)

                driver.find_element(By.XPATH, '//*[@id="order"]/div[3]/button[2]').click()

                booking_code = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[2]/div[1]/div').text
                limittime = driver.find_element(By.XPATH, '//*[@id="content"]/div[6]/div/p').text
                limittime = limittime.replace('您可以透過以下方式取票，','')
                
                tickey_situation = f'訂購完成！{booking_code}\n{limittime}'
                #driver.get_screenshot_as_file('finish.jpg')
    except:
        tickey_situation = 'stop3'
   # driver.quit()
    
    return tickey_situation