from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

# 訂票# 查詢

def search_trips(info):
    startwords = info.split('\n')[0]
    endwords = info.split('\n')[1]
    ridedate = info.split('\n')[2]
    starttimes = info.split('\n')[3]
    endtimes = info.split('\n')[4]

    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)
    
    seachurl = ('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime')
    driver.get(seachurl)

    start = driver.find_element(By.ID, 'startStation')
    start.send_keys(startwords)

    end = driver.find_element(By.ID, 'endStation')
    end.send_keys(endwords)

    date = driver.find_element(By.ID,'rideDate')
    date.clear()
    date.send_keys(ridedate)

    starttime = driver.find_element(By.ID, 'startTime')
    starttime.send_keys(starttimes)

    endtime = driver.find_element(By.ID, 'endTime')
    endtime.send_keys(endtimes)


    searchclick = driver.find_element(By.XPATH, '//*[@id="queryForm"]/div/div[3]/div[3]/input').click()

    ticketlist = driver.find_elements(By.CLASS_NAME,'trip-column')



    traintype, trips, starttime, arrivedtime, fare = [], [], [], [], []
    for i in ticketlist:
        tripslist = i.text.split(' ')
        traintype.append(tripslist[0])
        trips.append(tripslist[1])
        starttime.append(tripslist[6][-5:])
        arrivedtime.append(tripslist[7])
        fare.append(tripslist[15])
        
    driver.quit()
    
    tripsinfo = ''
    for traintype, tris, start, arrived, fare in zip(traintype, trips, starttime, arrivedtime, fare):
        tripsinfo += (f'車種:{traintype}\n車次:{tris}\n發車:{start}\n抵達:{arrived}\n車費:{fare}\n\n')

    return tripsinfo