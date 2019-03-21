'''每次运行程序时，需手动重新获取TOKEN和Cookie值'''

import requests
import time
import json
import random


# 发表文章
def add(title, content, description, link):
    '''

    :param title:文章标题
    :param content: 文章内容 h5
    :param category:  分类1-6 eg:'[1]'
    :return:
    '''
    TOKEN = 'c4da74f4220b9e72a4eaa4a97c1fe2b7'
    # 系统时间
    PUBLISHTIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:-3]
    # 添加文章的接口
    add_new_url = 'https://xiouwang.vip.webportal.top/ajax/news_h.jsp?cmd=add&_nmid=undefined&src=0&_TOKEN=' + TOKEN

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Cookie': '_cliid=vlpAbxZQW0VUVpGV; grayUrl=; loginCacct=xiouwang; loginSacct=lizhilei; loginUseSacct=1; _siteFlag1=0; loginSign=zcOUWUmTu3JS9SvYvCtEuecWeVjH9keWuVUxzVX0EA28Texw_q5UwN6F8r5RkHSxS8Eqw27vUlyVQdaIfR7VR5rXOZLcu8rfk_snv2N_ObA; _firstEnterManageFrame=true; _FSESSIONID=mMPmF6pJ9wWXfn4i',
        'Referer': 'https://xiouwang.vip.webportal.top/manage_v2/newsEdit.jsp?fromManage=true&popupID=7875'
    }
    # 存放图片
    pic_list = ['ABUIABACGAAg886o5AUouO2qgwQwgAU4qQM',
                'ABUIABACGAAg2cnH5AUo_ej5ygMwpgQ4ygI',
                'ABUIABACGAAg_svH5AUo9vCDiwUwpgQ4ygI',
                'ABUIABACGAAguM3H5AUoyojnywEwpgQ4ygI',
                'ABUIABACGAAg5c7H5AUonfyb1QcwpgQ4ygI',
                'ABUIABACGAAgpdHH5AUovZaGyQYwpgQ4ygI',
                'ABUIABACGAAg5tHH5AUowJiagAQwpgQ4ygI',
                'ABUIABACGAAgndPH5AUo69q5kAEwpgQ4ygI',
                'ABUIABACGAAg89PH5AUooOaumwIwpgQ4ygI',
                'ABUIABACGAAgx9XH5AUowKqdjQcwpgQ4ygI',
                'ABUIABACGAAg4NbH5AUo6PrP8gIwpgQ4ygI',
                'ABUIABACGAAg09jH5AUo9IrKywEwpgQ4ygI',
                'ABUIABACGAAgrNnH5AUo-Kna5gMwpgQ4ygI',
                'ABUIABACGAAgxNrH5AUooJiDDzCmBDjKAg',
                'ABUIABACGAAg4NrH5AUoqpiTmgEwpgQ4ygI',
                'ABUIABACGAAg59vH5AUo2urobjCmBDjKAg',
                'ABUIABACGAAgiNzH5AUokK--wgUwpgQ4ygI',
                'ABUIABACGAAgn9zH5AUov_7f5gMwpgQ4ygI',
                'ABUIABACGAAg8NzH5AUoqMbiigUwpgQ4ygI',
                'ABUIABACGAAgwd3H5AUogK_--AQwpgQ4ygI',
                'ABUIABACGAAg3N3H5AUoyIuqsAQwpgQ4ygI',
                'ABUIABACGAAg_N3H5AUo8tW9vwUwpgQ4ygI',
                'ABUIABACGAAgvt7H5AUo_MGtggcwpgQ4ygI',
                'ABUIABACGAAgn9-H5AUosMzPrQQwpgQ4ygI',
                'ABUIABACGAAgst-H5AUo5pT_4QQwpgQ4ygI',
                'ABUIABACGAAgyd-H5AUo5_yyLjCmBDjKAg',
                'ABUIABACGAAg2ODH5AUoouj-sQQwpgQ4ygI',
                'ABUIABACGAAgp_HH5AUo446I2wIwpgQ4ygI',
                'ABUIABACGAAgu_HH5AUooLD8rAEwpgQ4ygI',
                'ABUIABACGAAg0eHH5AUo2JrLpAYwpgQ4ygI',
                'ABUIABACGAAgjfLH5AUo6PmplAcwpgQ4ygI',
                'ABUIABACGAAgovLH5AUo4Lnl9gcwpgQ4ygI',
                'ABUIABACGAAguPLH5AUoitTTSDCmBDjKAg']
    # 随机获取一张cover
    cover_code = random.choice(pic_list)
    form_data = {
        'title': title,  # 文章标题
        'date': PUBLISHTIME,  # 发表时间
        'keyword': '',
        'desc': '',
        'content': content,  # 文章内容
        'mobiContent': '',
        'author': '',
        'source': '',
        'browserTitle': title,
        'flag': 0,
        'link': link,
        'pictureId': cover_code,
        'summary': description,
        'authMemberLevelId': -1,
        'authCus': 'true',
        'nlPictureId': '',
        'cusUrlAddress': '',
        'groupIds': "[" + str(random.randint(1, 6)) + "]",  # 文章分类1-6
        'attachIds': [],
        'wxShareIcon': {"tt": 0, "dt": 0, "it": 0, "tit": "", "cont": "", "id": ""}
    }
    try:
        response = requests.post(url=add_new_url, headers=headers, data=form_data).content.decode()
        result = json.loads(response)
        return result
    except:
        return None
# print(add(title='go', content='no', description='no', link='no'))
