from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


def cancel_train(cancelinfo):

    IDnum = cancelinfo.split('\n')[0]
    ticketnum = cancelinfo.split('\n')[1]

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless") #無頭模式
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('blink-settings=imagesEnabled=false') 
    
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


    driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip115/query')

    cancelID = driver.find_element(By.ID, 'pid')
    cancelID.send_keys(IDnum)

    cancelticketnum = driver.find_element(By.ID, 'bookingcode')
    cancelticketnum.send_keys(ticketnum)

    checkout = driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[7]/button').click()
    try:
        cancelclick = driver.find_element(By.ID, 'cancel').click()

        cancelclick2 = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div/div/div/div/div/div[4]/button[2]').click()

        driver.get_screenshot_as_file('./static/cancel_finish.png')

        cancelfinish1 = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[1]/dl/dd').text
        cancelfinish1 = cancelfinish1.replace('已取消 ', '')
        cancelfinish2 = driver.find_element(By.XPATH, '//*[@id="content"]/div[5]/div/div[1]/div[1]').text
        
        finish_text = f'{cancelfinish2}\n{cancelfinish1}'
    except:
        finishcancel = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/dl/dd').text
        if '已取消' in finishcancel:
            finish_text = finishcancel
        driver.get_screenshot_as_file('./static/cancel_finish.png')

    driver.delete_all_cookies()
    driver.quit()

    return finish_text