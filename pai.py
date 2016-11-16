import re
import urllib
from urllib import request
url = 'https://www.zhihu.com/question/40189657/answer/98543164?group_id=761485263242268672#comment-140927460'
kmt = urllib.request.urlopen(url).read()
kmt = kmt.decode('utf-8')
pl = re.findall(r'(https://static.zhihu.com/static/revved/img/ios.*?\.png)',kmt)
a = 2
for i in pl:
    urllib.request.urlretrieve(i,'C:\\Users\\v-lixcui\\Desktop\\img\\'+ str(a) +'.png')
    a += 1



