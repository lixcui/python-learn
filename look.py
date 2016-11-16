import re
import urllib
from urllib import request
url = 'http://tieba.baidu.com/p/4789324580'
html = urllib.request.urlopen(url).read()
print(html)
