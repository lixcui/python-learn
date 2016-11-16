import urllib
import re
import http.cookiejar as cookielib
from urllib import request
#from bs4 import BeautifulSoup as bsp
import urllib.parse
import requests
url = 'https://www.zhihu.com'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
header = {"Host":"www.zhihu.com",
           "Referer":"https://www.zhihu.com/",
           "User-Agent":agent
    }

zhihu_session = requests.Session()
f = zhihu_session.get(url,headers=header)
f = f.content.decode()
print(f)


'''
headers = {'q':'知乎',
           'rlz':'1C1CHZL_zh-CNJP709JP709',
           'oq':'知乎',
           'aqs':'chrome..69i57j69i59j69i61j0l3.40276j0j8',
           'sourceid':'chrome',
           'ie':'UTF-8'
           }
'''

a = urllib.request.urlopen(url)
