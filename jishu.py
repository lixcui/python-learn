sj = {}


str1 = '''ABCDEFGHIJKASFEWRASDFSADFEWTRYADGFFDSGERHVAFDVXZCVSADWETAJLKFJAHGIUOAWEANFNLKCVMKASLHDFJJEWITOIUWHTIUWHFJASKJD
FKAJSDKFJKSJDKFJLMNOPQRSTUVWXYZ'''
for i in str1:
    if i in sj:
        sj[i] += 1
    else:
        sj[i] = 1
print(sj)
