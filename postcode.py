import requests
import pickle
payload = {'q':'马云','rlz':'1C1CHZL_zh-CNJP709JP709','oq':'马云','aqs':'chrome.0.69i59.1876j0j7','sourceid':'chrome','ie':'UTF-8'}


r = requests.get('http://www.google.com/search',params=payload,stream=True)
print(r.url)
print(r.status_code)#返回状态码
#print(r.text)#返回网页内容
print(r.encoding)
print(r.json)
#filename = open(r'C:\Users\v-lixcui\Desktop\vzch.xlsx','wb')
#obj = r.text
#pickle.dump(obj,filename)
#filename.close()
#fileexc = open(r'C:\Users\v-lixcui\Desktop\明细.xlsx','r')
#print(fileexc.read())






#with open(filename,'wb') as fd:
    #for chunk in r.iter_content(chunk_size):
        #fd.write(chunk)
#filename.close()
