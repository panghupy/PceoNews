'''抓取雪球网新闻,每次登录需要重新获取cookie值'''
import random
import requests
import json
import time
from NewsAdd import add
from lxml import etree

kw = '科创板'
page = 10
cookie = '_ga=GA1.2.904009247.1552535807; device_id=d8ed28d578e79a42d8c76ee2d18c98f7; _gid=GA1.2.2003897327.1553045191; aliyungf_tc=AQAAAD7gagaGvgcA5LGEOkARff14xCM9; xq_a_token=682c39a460645dafb1ff41f67e0efccba8b0f118; xq_a_token.sig=Bg9acTC-woVSsS6DZvdAtd40CQU; xq_r_token=798a7cab8cd606f61a09fbac15374f1172b00607; xq_r_token.sig=sHSWFNmu_GqEUOK9A-6umfNgFcU; _gat=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1552958262,1553045191,1553070610,1553130168; u=801553130168701; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1553130175'
for index in range(5, page + 1):
    url = 'https://xueqiu.com/statuses/search.json?sort=time&source=news&q=%E7%A7%91%E5%88%9B%E6%9D%BF&count=20&page=' + str(
        index)

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Cookie': cookie,
        # 'Referer': 'https://xueqiu.com/k?q=%E7%A7%91%E5%88%9B%E6%9D%BF',
        'Host': 'xueqiu.com'
    }

    response = requests.get(url, headers=headers).content.decode()

    result = json.loads(response)
    print(result)
    for item in result['list']:
        try:
            title = etree.HTML(item['title']).xpath('string(.)')
        except:
            title = item['title']
        content = item['text'].replace('</p>', '\n</p>').replace('<p>',
                                                                 '<p style="line-height:2;font-size:18">\n')
        description = etree.HTML(item['description']).xpath('string(.)')[:40]
        link = item['source_link']
        print('正在抓取文章：', title)
        # result = add(title=title, content=content, description=description, link=link)
        # print(result['msg'])
    time.sleep(random.randint(3,7))