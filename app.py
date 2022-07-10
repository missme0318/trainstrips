from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import (MessageEvent, TextMessage, TextSendMessage,StickerSendMessage)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


app = Flask(__name__)

line_bot_api = LineBotApi('cBwUwzLyXqDhFhdsG/cglur32QRiBgbAi/3Xq3eby34MUg1zcQi2Ydb2/PPmtL0GbrhW84+TfO8nlWDjV2dTvCeSLrnhW0mA6efqIZ40zOlX1I7l47BrzXifLxD3pc5LEkQ7z0MtN4579ivGdoDK0QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('79a8d7930208c29ff1601c21c2683c37')


def input_wanted(search):
    address, limittime = [], []
    process = 'start'
    
    # chromeOption = webdriver.ChromeOptions()

    # chromeOption.add_argument("start-maximized")
    # chromeOption.add_argument('--headless')
    # chromeOption.add_argument('--no-sandbox')
    # chromeOption.add_argument('--disable-dev-shm-usage')
    # driver = webdriver.Chrome(chrome_options=chromeOption)

    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--lang=zh-CN.UTF8")
    chromeOption.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    driver = webdriver.Chrome(chrome_options=chromeOption)
        
        # driver = webdriver.Chrome()
        # driver.set_window_size(1024, 960)

    # driver = webdriver.Chrome(service=s, options=chromeOptions)
    driver.get('https://www.google.com.tw/maps/')
    try:
        
        title = driver.find_element(By.ID, 'searchboxinput')
        title.send_keys('高雄美食')

    #driver.maximize_window()

        driver.implicitly_wait(2)

        # 1st info
        operation = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')

        name_type = operation.find_elements(By.CLASS_NAME, 'Nv2PK')

        websites = operation.find_elements(By.TAG_NAME, 'a')

        name = [i.text.split('\n')[0] for i in name_type]
        driver.quit()
    except :
        process = 'non-start'
    
    return process

def testing(name):
    return name

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

        return


    if msg in ['hi', 'Hi!']:
        r = 'Hi!'
    elif '聊天' in msg:
        r = '我是機器人'
    elif '高雄美食' == msg:
        r = input_wanted('高雄美食')
    elif 'Poppy' == msg:
        r = testing(msg)
    else:
        r = '抱歉！說什麼？'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
