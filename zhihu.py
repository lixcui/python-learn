import urllib
import re
from urllib import request
url = r'https://www.zhihu.com/topic/19557525/hot'
html = urllib.request.urlopen(url).read()
html = html.decode()
lj = re.findall(r"(https://pic3.zhimg.com/.*?\.jpg)",html)
print(lj)
for a in lj:
    print(a)
for i in range(5):
    urllib.request.urlretrieve(lj[i],'C:\\Users\\v-lixcui\\Desktop\\'+str(i)+'.jpg')
