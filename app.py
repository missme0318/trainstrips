from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

from searchtrips import search_trips
from booking import booking_train
from foods import delicious
from cancel import cancel_train
from recaptha import solveRecaptha

import time

app = Flask(__name__)

line_bot_api = LineBotApi('cBwUwzLyXqDhFhdsG/cglur32QRiBgbAi/3Xq3eby34MUg1zcQi2Ydb2/PPmtL0GbrhW84+TfO8nlWDjV2dTvCeSLrnhW0mA6efqIZ40zOlX1I7l47BrzXifLxD3pc5LEkQ7z0MtN4579ivGdoDK0QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('79a8d7930208c29ff1601c21c2683c37')



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
        image_message = ImageSendMessage(
            original_content_url = return_img_stream('./static/cancel_finish.png'),
            preview_image_url= return_img_stream('./static/cancel_finish.png'))
        line_bot_api.reply_message(event.reply_token, image_message)

        return


    if msg in ['hi', 'Hi!']:
        r = '歡迎訂購火車票\n我們有這些功能：\n1.查詢車次\n2.訂購車票\n3.取消車票\n4.尋找美食\n\n請輸入想執行的項目'
    elif '查詢車次' in msg:
        r = '請依格式輸入起終點.日期.時間\n例如：\n\n查詢\n高雄\n台北\n20220712\n13:00\n15:00'
    elif '查詢\n' in msg:
        tripsinfo = msg.replace('查詢\n','')
        r = search_trips(tripsinfo)
    elif '訂購車票' in msg:
        r = '請依格式輸入ID.起終點.日期.車次\n例如：\n\n訂購\nS223551400\n高雄\n台北\n20220712\n150'
    elif '訂購\n' in msg:
        bookinfo = msg.replace('訂購\n','')
        # code = solveRecaptha()
        r = booking_train(solveRecaptha(), bookinfo)
    elif '取消車票' in msg:
        r = '請依格式輸入ID/車次\n例如：\n\n取消\nSP223210741\n554'
    elif '取消\n' in msg:
        cancelinfo = msg.replace('取消\n','')
        r = cancel_train(cancelinfo)
    elif '尋找美食' in msg:
        r = '請輸入：尋找地區 食物\n例如：\n\n尋找\n台北火車站 甜點'
    elif '尋找' in msg:
        search = msg.replace('尋找','')
        r = delicious(search)
    elif 'code' == msg:
        r = solveRecaptha()
    else:
        r = '歡迎訂購火車票\n我們有這些功能：\n1.查詢車次\n2.訂購車票\n3.取消車票\n4.尋找美食\n\n請輸入想執行的項目'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
