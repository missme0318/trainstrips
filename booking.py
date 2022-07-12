from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import 
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha

import time
import os
import base64

def solveRecaptha(sitekey, pageurl):
    api_key = os.getenv('APIKEY_2CAPTCHA', '4bca3ca456af17b4be31f166e1ddb8aa')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(sitekey=sitekey,url=pageurl,version="v2")

    except Exception as e:
        print(e)

    else:
        return result
    

# 訂票

def booking_train(bookinfo):

    IDnum = bookinfo.split('\n')[0]
    startwords = bookinfo.split('\n')[1]
    endwords = bookinfo.split('\n')[2]
    ridedatebook = bookinfo.split('\n')[3]
    tripsnums = bookinfo.split('\n')[4]

    train_booking_pageurl = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/bookingTicket'
    train_booking_sitekey = '6LdHYnAcAAAAAI26IgbIFgC-gJr-zKcQqP1ineoz'
    result = solveRecaptha(train_booking_sitekey, train_booking_pageurl)
    code = result['code']

    #code = '03ANYolqs4VAocwIHQt9LG4k_S6owjCETlIEK_0qm4z6_nTHRrUqmT7Gpl6U2FMLZRDUWN9el5Il9sweOA1aZn0qlWDX_opT9BkOtoQkYhVJkLo-FjdPECqlIEQIuGEgthcSIeR4dpaiC4rAx7mTOEZXCTYe3MLG3zIOrJxn2vVf0fCmtFJLeKNWBuWtlB0cm1rhgMykHPgXjA3thVMNhCccrB92s-80h5ADmQtsII2pYt508uqOhhHhy7ePHXNAcDQh2UjASSE4VQj1j8u-OEtF3-Q5ulu5KUAjGxZ77fLGZqrA_wpJvx_MVVIsrfzbPt2X8rcwDYBSL4TtYtm0mZnYW10o3jqBEyMEcH2GafbcWtF94RS_mdbBkf8Rsp5j-aecKV9Fp414NKv1eUV0SXJCqrqBY6kJAOxvPTGPMO4sZmzMHH3IIZeq3u8_tVCG8QDUjVpk42cVAUgGL_D48JfMbbTwYbkjf8GJr481q5jd_HRAWij0k4frZvijCGutrM3w931ktTdw99eU4JUV8dEviDOYPQ1wadWqjhtsg_FO6Q9JDRpuT8gV0mGDbx7Q3Xr9PwDeqnoKTBimuYb0_vWtoZInSnMYjm65KLLIniEwmdOg-uuqIv33LrEm5gfVnEr-yAGCxuNisy6IbwBSkUSVgCpcH0tUZdX18EbusBU9CKAuYsFKstQcII97jhR98nesPVoEPAfqiJI-ltIjsaMXu9wvLOKDJ3PphGkX0AVZhO9CyqhPVfj3WYtziJv_Dt1YsIjMh0fDncamQpdEOeLiClgxVld2trPkFRPnDkkFVwHosrfhgQdqJlkQ7zWLtq9D4eVfsakyyTj0sylhZigVX-CcOjsuk_S327YzIAAB30JxhwZF_hmsAvK5xiQduXQsiHLIkqgIjFoWBRh-8-2CYW3cLVpsiki9xubXILh_Vtumv03BJj77PatIkFIPLqRq3Pe6qW8bWbIF7yGS6IFioqngyeZrPFPnRdsAHe6NqON-eCgE5-cV9TpicTbKubIjo5LtY3laEDQRfjN9IC0UEEZHLpq44OkdWwWm-P-PtX93ZQBNk-aF-ujP7hFljSrm5FClDdmx9GozQbUSuG3l2o9DywCYyFcHS-l1VHFkEcsa0F8WLbZMCup1uRKk_C6292t9hLalVSO6FMI1xFVI66JG0aUL7l6vzuI3eTMc4iHtIhxbOE91FsoebgxFqqJBwbDmiLROijkZUestjJAlV4ENzehkJFq_j060PPvQLWVZwwOGTiUp8OBo_qvUmOFDS_dn3GM3_AKcYwuHbZSBft7_ws72DSbZQ5vIFkQ0ho0KDay4DQFYkPxLWXmUSxNXozh_Y8YPJc3aiZqCguskNEyRsoR_GZuOg-wqm6eMofX1ZgPTuC1CwlLtiivrHzVtDZNWtSTbj20Wv9gfpJBGFbg2JLV3rjV0Usa8m8RkdMYk0ZKtCv2sWIBzWfJKx9G_i0VHBIOB7CGz7t6a9QaD8mek8taqrakM8uhe2g6G-4hR-QYNkkPouZTCz_aM7iG6n3uDlirvbxgibuMV8HjrFzIsldk0y6pqcs8VcPF-B5ZhkrJFJz06KCkPu1CFoBUySrWwgHu9ERReVjd1ix6lhUbagwujC0yg'

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

    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[4]/input[2]').click()

    try:
        errormsg = driver.find_element(By.ID, 'errorDiv').text
        ticket_situation = errormsg
        # driver.get_screenshot_as_file('./static/finish.jpg')
            
    except:
        ripsnum = driver.find_element(By.CLASS_NAME, 'cartlist-id').text
        ticket_situation = f'訂購完成！{tripsnum}'

        # paidtime = driver.find_element(By.CSS_SELECTOR, 'span.red').text
        # ticket_situation = f'訂購完成！{str(tripsnum)}\n請於{str(paidtime)}'
        # driver.get_screenshot_as_file('./static/finish.jpg')

        # try:   
        #     driver.find_element(By.XPATH, '//*[@id="order"]/div[3]/button').click()  
        #     # time.sleep(2)
            
        
        #     payment = driver.find_element(By.ID, 'paymentMethod')
        #     cash = Select(payment).options[1]
        #     Select(payment).select_by_visible_text(cash.text)

        #     # time.sleep(2)

        #     driver.find_element(By.XPATH, '//*[@id="order"]/div[3]/button[2]').click()

        #     booking_code = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[2]/div[1]/div').text
        #     limittime = driver.find_element(By.XPATH, '//*[@id="content"]/div[6]/div/p').text
        #     limittime = limittime.replace('您可以透過以下方式取票，','')

        #     ticket_situation = f'訂購完成！{booking_code}\n{limittime}'
        #     # driver.get_screenshot_as_file('./static/finish.jpg')

        # except:
        #     ticket_situation = '訂購完成！'+str(tripsnum)
    driver.delete_all_cookies()
    driver.quit()

    
        
    return ticket_situation

