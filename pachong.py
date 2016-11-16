import urllib
from urllib import request
url = urllib.request.urlopen('http://read.qidian.com/BookReader/_2fdrMLcMOxqqtWmhQLkJA2,3Z3QUKkyE0Pgn4SMoDUcDQ2.aspx').read()
print(url)
