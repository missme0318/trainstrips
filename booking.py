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

def solveRecaptha(sitekey, pageurl):
    
    api_key = os.getenv('APIKEY_2CAPTCHA', '4bca3ca456af17b4be31f166e1ddb8aa')
    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(sitekey=sitekey, url=pageurl)

    except Exception as e:
        print(e)

    else:
        code = result['code']
        return code

def booking_train(bookinfo):

    IDnum = bookinfo.split('\n')[0]
    startwords = bookinfo.split('\n')[1]
    endwords = bookinfo.split('\n')[2]
    ridedatebook = bookinfo.split('\n')[3]
    tripsnums = bookinfo.split('\n')[4]

    # train_booking_pageurl = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/bookingTicket'
    # train_booking_sitekey = '6LdHYnAcAAAAAI26IgbIFgC-gJr-zKcQqP1ineoz'
    # code = solveRecaptha(train_booking_sitekey, train_booking_pageurl)
    code='03ANYolquh_n3s2EW4jgVEOpESMAqQt30QcwV8sqlvVGy8JIfktkBW2EKvONg1BfwKgjmRTOjpn25wzVXB1ZNrtGCM0tUsWS_TUreDoC_602iudO_oXMd5HVeUM_8pJyt4-B4Hz7JYCJsYuXY4Gzf2fGP4JgK9WPpu5Yf0cILniMiNuPITKgNYGpNVumkcnxxoItKD-Fr2eTk5HJnU87oVfJovyS-2_1hQ1o_wBpY_P95_UaNnBI45HPkk2L1tdFauek8IGei2cD0majjTscY51pG69wqA3-GJPEh8itdsc0kqy-CUCBwg-ur_rrghzDQ-IO6AmYjZJkw4BSD5wZfMTkmBTmjdDwe__yzXkngA9cMKFZG0Tr48AYtoNKb8Toi6by-uSomMIPfBTKCGQO6CyESHSeGjF-rG2A0803tQZc95J9JX40xMGhk99vDsZJ2_nqc16cAoxWozTnOFHu1WOLfKpOhiJgvKEFkvOr0aenA-IJXen1JoB7lLYafv_YDpmnrTuJesxdlU30iYBEKWMW2e5PtCyIrlC1PSjz_0TSwtFULc2y8Ssvg_6qvXuXFNklhtuAWdMseKnVM2CpXNWFR7sMCEQ_Mbfly9O-3Rnaian2Ke2fYDQtaKE45UOFiB1ScwtxgfWKpjw8eQ5FzWUo5c4lV873-x6y4_aKQ1XvMKYj5G21DfcrfW8gqtmN7A2onKRn0Rp7IN8os2L-Koy0i3qNc952gl0OTJgmNpVA3JDDS7nPb4DincxnrkNE6aeF7pTFuIcsm0FFy_ofVV9-oOhUhkXTCSi7gzn0nnACMHEb63tCia3jW4NcX-W6OxHDCxLS4uSjLAUHbzUJuGq_6zt-2r1gKZ21IW4lxA-m4Y6o6rtNf6zdk0meLorAaKZAAdTh4O9wSYPWE5n-TybXf6T8ParDZPgBhGB5eIvDL9zSJuEzafg1afq6MBjM-HO7pI0ctAURRV5jj0JPxk_UOCsAM9sWYVWIB_WVP9Cc0erwqT6UAa_nd1d3AkdHtoWsbU2347quXggdc79khMpcbwu_aqDtwwTzLAehCmFuxG__UQLYS37QdR4iAbtRivhUVC-KdaT3OSXK6ZGQA-OG8V9gvAABlSg4H_4KYHltsE6J-4Qr45XfTkl5n6Fpe6s0VuyVNLd3jw8gqMtdZXUjU3W_JVgF6yUWVRKlnOZv1tVAHPA-gpvGFfuaGs0XzcjLLFr_oRJSNoxVtqpj3yvR2w011m9Q0Mc3MnvS6gZbrCjShDuVTp0NeHL2LlhizomwY5PmOUPewrn-PI28fSIE2dJB78Xs74MrLLTnJPy9csQGXXLm9LOSAcD8BbFclbJXgC3svztklHxCCbF2iRg2iuGwf1YceN7Ct7zausdIWvNIpCRpj4Bi3eThf20r66NNEY_oWKocQMXBKix28N4DQM3QvCrmcQkKed02nkXuZ5afPh6cIZt43uQNY8yMVrmMX8KBMzJ07HF5vkINGgkWRE7KKoBnT-yHFtN_vvVW9p09A196xSX3d68xXaBcDMtttKIKu-NIAJG1EexGwN-0F93AHBxORKDiacxw5oiyf98Mac8RmJJDghJ5kPthMR7S3yd5W5xtCb'

    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)
    
    driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query')
    
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

    time.sleep(2)
    
    driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[4]/input[2]').click()

    try:
        errormsg = driver.find_element(By.ID, 'errorDiv').text
        ticket_situation = errormsg
        driver.get_screenshot_as_file('static/finish.png')
            
    except:
        ripsnum = driver.find_element(By.CLASS_NAME, 'cartlist-id').text
        ticket_situation = f'訂購完成！{tripsnum}'
        driver.get_screenshot_as_file('static/finish.png')
        
    finally:
        driver.delete_all_cookies()
        driver.quit()  

    return ticket_situation






