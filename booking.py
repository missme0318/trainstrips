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

    # train_booking_pageurl = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/bookingTicket'
    # train_booking_sitekey = '6LdHYnAcAAAAAI26IgbIFgC-gJr-zKcQqP1ineoz'
    # result = solveRecaptha(train_booking_sitekey, train_booking_pageurl)
    # code = result['code']
    code = '03ANYolqsbcM8U0WCI-FSVato_dGCXYPnVF_45sMg16nzrhqpjkK868ICFpnYMOUSWW5RFZdrSMx3HVK4ekIWaRBVsozqdlD6kzBDtRocj7KHx2t6055TVZyNZCK4bnh35RVH29Iyb5s33ld7Ia8QGVkEfBxjGiDeWionN2X1l-6l8cx1m19HcPvfbCH45k4rrnSbhs0wnEhvjStAmkJ08MB4yw03dE-xd7NMIT0monPzkILZNuHH_uhVU5vMDICp0wv4MNuc6Cv-C2BQZcqwK_Xgq6ewmMEn46vaSS2Vm7EK3Y3rb27-EnNcKtd_LPcginXzjlsSfWJXpr2pUGcZzF8VxsKEMj-qIa7xEtEHx0eNva5abdfYgTPuBBo5yyCKp0WCfWHNlIoOuBuRkYG6F0mbmnlED80wG1y7cToEI9K-Bbh2YQe2hQAniDQTTlgFHFfdpsdvzikEWixC0-roEbda4ES_QF-0K3o0xWvWXv5QAqAwJliB8VSlm-_-Aav77ePP0KKMEZWb9ZamBEgcb7tyez4GdJptbRYeODMFjaC0viI7N5ScMYxIjVutbbSfJXMVXSJFOWH6q9CRU_LLgdawF_6XHtxPvdwujZRi-hu2O1XS-gDEBC1vnIPJgegcGPkSPK3ZRYYZ6sypvx7jZp-ulV58cp5xCLjLCcLLPuy4TTItvrg58JFZ2RJbrMwLxojwSIld-7blbKUGCTA6WnQKISqsGdyV_6uU2_WtjYDX3EK3eV4rgMsKFaVbyAfBkIFFjGcE1nb7UMF7KPjRK74U7Qg0zVe_4ajOrLXVUBGs85yjkqPv5366-5KqhWXF2kXJlPzJ2tf9uHpG1uNso45HmMbu6arxwWdcAaooU9AreOHxT7bANK8jW_tLBSqJsKvw5vKJMk-bMg4UAB8ELRD8uR6AUOTmmy-ZJunUKyOwUqiT6WmjmSuDDgWPLSC8fkWjmNck0beQ6VIFN3yrw6tTWyX2qWWJM723PudtkbbckvKtDJ4TlbKmEXPGxzUH8m0c9hIr5u0qYxa_02PHcY5xJv5vWBavu-eXv5z10cEXk7Z9av-a2THpdAqfQz7MF8iaGxzz4N7JhvjNC4tRRzpeTSmGszMUMflpFJXO_turWi1dMgxxJZpIv7SrYf3AseiMVx4JCiWjDz_k8Zlb6mf6zH0dcHebUT-WZUgFjfDuptza52suGEQyETwKqKMtuYFOLk8we4AG2VJhP1jnefGVuLL26dPFKEvwJrT4p0AgtElzAveQJR1ngEVeg9W9ahehhGx-1sIivBkBNzwfRMXZASedG2mn7wlg3L0eBEgI9x8MULRPOsnAV-8suhprbh52efDl2g4Yj9bp2ZtOG4MBsHTB8O9B-Xv5nQZANGcKCPeOGcv33n8gbk1IIBuhn2DZ-c0UGzUNBF1UcBLedl-LZ4zXjkSm_cSBEJzfvL6jX-9myMyXzvyMRhZG28zy0rOoJbXS1PtVgTheRSWcfSVBHzFtdosSnO9mizkT4g2p8klNHqurozfswbEEnrthuWEAGGOnbYBpSApjDft5MZ3kRWVvAAaMPeZEEm0mjr9BeYqdRoq7Vf9N7ArJi37f32CUateliFmwDZFz6uEoMa2K8PIjMCmZ38Q'


    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)
    
    
    driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query')
    #driver.maximize_window()

    # driver.set_window_size(1600,1024)

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
    driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML = '" + code + "'")

    #time.sleep(3)
    try:
        driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[4]/input[2]').click()
        tickey_situation = 'stop3'

    
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
            driver.get_screenshot_as_file('finish.jpg')

    # tickey_situation = 'stop3'
    driver.quit()
    
    return tickey_situation