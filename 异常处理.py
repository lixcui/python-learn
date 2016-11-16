import random
try:
    a = int(input('请输入：'))
    print(random.randint(1,a))
except ValueError:
    print('输入错误')

    
