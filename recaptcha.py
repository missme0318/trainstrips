from twocaptcha import TwoCaptcha
import os

def solveRecaptha22():
    pageurl = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/bookingTicket'
    sitekey = '6LdHYnAcAAAAAI26IgbIFgC-gJr-zKcQqP1ineoz'

    api_key = os.getenv('APIKEY_2CAPTCHA', '4bca3ca456af17b4be31f166e1ddb8aa')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=pageurl)

    except Exception as e:
        print(e)

    else:
        return (result['code'])
