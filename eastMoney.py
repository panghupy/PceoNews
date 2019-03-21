import requests
import time

# 设置查询关键词
keyword = '科创板'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'api.so.eastmoney.com',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://so.eastmoney.com/news/s?keyword=%E7%A7%91%E5%88%9B%E6%9D%BF&pageindex=15',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie': 'qgqp_b_id=43fd514f6f3c0179c5ffd16220dd4e8b; st_si=26169771247780; Hm_lvt_e834f0bcb11ce14253b9eba75492b597=1552534941,1552534964; emshistory=%5B%22%E7%A7%91%E5%88%9B%E6%9D%BF%22%2C%22kechaungban%22%2C%22kechuangban%22%5D; Hm_lpvt_e834f0bcb11ce14253b9eba75492b597=1552536228; st_pvi=63490844202784; st_sp=2019-03-14%2011%3A42%3A16; st_inirUrl=https%3A%2F%2Fwww.google.com%2F; st_sn=15; st_psi=20190314120345306-118000300905-1500744344; st_asi=delete'
}

pageindex = 1
url = 'http://api.so.eastmoney.com/bussiness/Web/GetSearchList?'
params = {
    'type': 20,
    'pageindex': str(pageindex),
    'pagesize': 10,
    'keyword': keyword,
    'cb': 'jQuery112402875879227784153_1552536527483',
    '_': 1552536527484
}
# response = requests.get(url=url, headers=headers)
# print(response.content.decode())
print(time.time())
1552537579160
