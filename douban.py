
import requests
import re
import xlwt
import chardet
import os
import time
import threading

os.chdir(r'C:\Users\v-lixcui\Desktop\mssql')



def rzll():
    url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    html = requests.get(url).text
    a = re.findall(r'<a href="/tag/(.*?)">',html)#a是list 包含所有种类的图书
    return a

def rbook(a):
    time3 = time.time()
    for zhonglei in a:
        start = 0
        workbook = xlwt.Workbook()
        while start < 80:
            
            url2 = 'https://book.douban.com/tag/%s?start=%d'%(zhonglei,start)#每一种类里面的图书
            html2 = requests.get(url2).text
            b = re.findall(r'<a href="https://book.douban.com/subject/(.*?)/"',html2)
            row = 0
            col = 0

            worksheet = workbook.add_sheet('book'+str(start))#为每个excel内的sheet命名
            for ts in b:
                url3 = 'https://book.douban.com/subject/%s/'%ts#具体一本书的页面
                html3 = requests.get(url3).text
                try:
                    c1 = re.findall(r'<span property="v:itemreviewed">(.*?)</span>',html3)
                    c = re.findall(r'<span class="pl">.*?</span> (.*?)<br/>',html3)#提取图书具体信息
                    worksheet.write(row,col,c1[0])#写入图书具体数据到指定的sheet
                    worksheet.write(row,col+1,c[0])
                    worksheet.write(row,col+2,c[1])
                    worksheet.write(row,col+3,c[2])
                    worksheet.write(row,col+4,c[3])
                    worksheet.write(row,col+5,c[4])
                    worksheet.write(row,col+6,c[5])
                except UnicodeEncodeError:
                    print(str(c1)+'error')
                except IndexError:
                    print(str(c1)+'error')
                row += 1#为每条数据提供位置
            start += 20#控制每个页面的种类与sheet的命名
        workbook.save(zhonglei+'.xls')#保存excel表，以每一种类为一表
    time2 = time.time()
    print(time2-time3)
a = rzll()
rbook(a)







 







