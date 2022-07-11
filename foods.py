import requests
from bs4 import BeautifulSoup

def delicious(sel):
    count=0
    content=''
    for i in range(1,3):
        url='https://ifoodie.tw/explore/高雄市/list/'+sel+'?page='+str(i)
        #print('Start parsing pttHot....')
        response = requests.get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        b=html_soup.find_all('div',class_='restaurant-info')
        
        for i in b:
            try:            
                score=i.find('div',class_='responsive').get_text()
            except :
                pass
            fscore=float(score)   #評分

            if fscore >= 4.8:
                name=i.find('a',class_='title-text').get_text()
                htt=('https://ifoodie.tw'+i.a['href'].split('-')[0]+'-'+name)
                response1 = requests.get(htt)
                html_soup1 = BeautifulSoup(response1.text, 'html.parser')
                d=html_soup1.find_all('div',class_='jsx-1969054371 info')
                if count < 3:  #輸出3筆資料
                    for ii in d:
                        time=ii.find('div',class_='jsx-1969054371 openingHourWrapper wrap').text 
                        tel=ii.find('a',class_='jsx-1969054371').text          #聯絡電話
                        addr=ii.find('span',class_='jsx-1969054371 detail').text  #地址
                        #goo=ii.find('span',class_='jsx-1969054371 map-outer').text
                        mapp='http://www.google.com.tw/maps/search/'+name   #google map
                        a='{}\n評分:{}\n{}\n聯絡電話:{}\n地址:{}\ngoogle map:{}\n\n\n'.format(name,score,time,tel,addr,mapp)
                        content+=a
                        count+=1
    if count == 0:
        content+='目前沒有推薦名單\n\n再給我多一點線索\n\n擴大範圍搜尋吧!\n\n例如：我要吃蛋糕'
                    
    return content