import urllib.request
import os
import threading

os.chdir(r'C:\Users\v-lixcui\Desktop\bqb')
def bq1():
    for i in range(1326,1375):
        urllib.request.urlretrieve('http://q.qqbiaoqing.com/down/013/%s.eif'%i,'%s.eif'%i)
    
    
    #url = 'http://q.qqbiaoqing.com/down/013/1313.eif'
def bq2():
    for a in range(1376,1405):
        urllib.request.urlretrieve('http://q.qqbiaoqing.com/down/013/%s.eif'%a,'%s.eif'%a)
def bq3():
    for b in range(1375,1405):
        urllib.request.urlretrieve('http://q.qqbiaoqing.com/down/013/%s.eif'%b,'%s.eif'%b)

def main():
    bqone=threading.Thread(target=bq1,name='B1')
    bqtwo=threading.Thread(target=bq2,name='B2')
    #bqthree=threading.Thread(target=bq3,name='B3')
    bqone.start()
    bqtwo.start()
    #bqthree.start()
    bqone.join()
    bqtwo.join()
    #bqthree.join()



if __name__ == '__main__':
    main()
    
