from twocaptcha import TwoCaptcha
import os

def solveRecaptha22():

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
