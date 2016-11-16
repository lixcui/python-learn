import urllib
import re
import os
from urllib import request
url2 = ['http://tieba.baidu.com/p/4762188597','http://tieba.baidu.com/p/4735336179','http://tieba.baidu.com/p/4711040477','http://tieba.baidu.com/p/4731335319','http://tieba.baidu.com/p/4721503659']
#html = urllib.request.urlopen(url).read()
#html = html.decode()
#lj = re.findall(r'(http://imgsrc.baidu.com/forum/w%3D580.*?\.jpg)',html)

#http://imgsrc.baidu.com/forum/w%3D580/sign=f1600ee93112b31bc76ccd21b61a3674/0958938fa0ec08fad3d0810951ee3d6d54fbda2c.jpg
#a = 59
#for i in lj:
    #urllib.request.urlretrieve(i,'C:\\Users\\v-lixcui\\Desktop\\img\\'+ str(a) +'.jpg')
    #a += 1

#http://imgsrc.baidu.com/forum/w%3D580/sign=8e59d768c8fc1e17fdbf8c397a91f67c/9e096b63f6246b60c1c3d20aecf81a4c500fa2fb.jpg
#http://imgsrc.baidu.com/forum/w%3D580/sign=47b475ea412309f7e76fad1a420f0c39/74e736d12f2eb93893ae1a8cd2628535e4dd6f88.jpg
#http://imgsrc.baidu.com/forum/w%3D580/sign=8ee82bb15b43fbf2c52ca62b807fca1e/bc82d158ccbf6c81c8be2251b43eb13532fa40f9.jpg
#http://imgsrc.baidu.com/forum/w%3D580/sign=aff9f6cc3ca85edffa8cfe2b795509d8/99cb39dbb6fd5266c3dea388a318972bd50736b0.jpg
class Myerror(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
def urlfun(url):
    a = 1
    for i in url:
        html = urllib.request.urlopen(i).read()#打开链接
        html = html.decode()#把所获得的网页转化为UNICODE字符
        lj = re.findall(r'(http://imgsrc.baidu.com/forum/w%3D580.*?\.jpg)',html)#构造一个正则匹配，匹配出所需要的图片链接，返回一个列表
        #与命名有关的，需要不重复命名
        f = os.makedirs(os.getcwd()+'\\'+str(a))
        a+=1
        
            
        for b in lj:#对一个网页取出来的链接进行循环，取出每一个图片的链接
            
            urllib.request.urlretrieve(b,f+str(a)+'.jpg')#对图片进行保存，用urllib.request.urlretrieve函数进行保存
                                                                                              #此函数的格式为urlretrieve（图片链接，图片的保存地址）
            a += 1#对命名进行规范
        
urlfun(url2)
