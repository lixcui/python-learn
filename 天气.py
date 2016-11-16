from bs4 import BeautifulSoup as bsp
from urllib import request
import urllib
import re
url = 'https://www.zhihu.com/people/excited-vczh'
html = urllib.request.urlopen(url).read()


soup = bsp(html,'html.parser')
#print(soup.prettify())#prettify美化,以嵌套的方式打印出来
#print(soup.span.contents[0])
#for i in soup.head.children:#打印直接的子节点
    #print(i)
def zz(url):
    html = urllib.request.urlopen(url).read()
    html = html.decode()
    zhengz = re.findall(r'<span class="name">(.*?)</span>',html)#利用正则解析，但是取出来的还有两个，需要标记
    name = zhengz[0]
    zhengz2 = re.findall(r'class="topic-link" data-token=[0-9] data-topicid=[0-9]>(.*?)</a>',html)



    
    print(name,zhengz2)
    
zz(url)







'''
def depa(soup):
    for html in soup.select('.title-section'):
        name = soup.select('.name')[0].text
        bio = soup.select('.title-section')[0].text
        #topiclink = soup.select('.topic-link')[0].text
        
        job = soup.select('.content')[1].text
        #employment = soup.select('.info-wrap')[2].text
        
        print(name,bio,job)
depa(soup)
'''
