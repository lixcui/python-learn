import requests
import re
url = 'https://github.com/login'
user = '940163792@qq.com'
psw = '12345678qwe'
myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding':'gzip, deflate, sdch, br',
           'Accept-Language':'zh-CN,zh;q=0.8'
    }#模拟浏览器的request headers
sss = requests.Session()#为了模拟浏览器与服务器 持续的对话 创建这个对象
r = sss.get(url,headers=myheaders)#以get方式访问登陆界面


result = re.findall(r'<input name="authenticity_token" type="hidden" value="(.*)" />',r.text)#得到匹配结果

token = result[0]

my_data = {'commit':'Sign in',
           'utf-8':'✓',
           'authenticity_token:':token,
           'login':user,
           'password':psw}
url2 = 'https://github.com/session'
r2 = sss.post(url2,headers=myheaders,data = my_data)
print(r2.text)
