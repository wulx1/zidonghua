'''
脚本功能：个人学习python笔记，借助python实现纯英文大小写字母随机密码、英文大小写字母+数字随机密码、英文大小写字母+标点符号随机密码、英文大小写字母+数字+标点符号复杂随机密码等多种形式的密码生成，也可用于生成激活码并保存到本地txt文档
author：larrywons
'''


'''
import string, random
length = int(input("The Password Length You Want to Set： \n请输入你想设置的密码长度:\n"))
for i in range(1):
    RandomPassword = ''.join(random.sample(string.ascii_letters,length))
    print(RandomPassword)
'''


'''
import string, random
length = int(input("The Password Length You Want to Set： \n请输入你想设置的密码长度:\n"))
passwd_num = int(input("How much passwds do you prefer to generate:\n你想生成几组密码供挑选？\n"))
for i in range(passwd_num):
    RandomPassword = ''.join(random.sample(string.ascii_letters,length))
    print(RandomPassword)
'''

'''
import string, random
length = int(input("The Password Length You Want to Set： \n请输入你想设置的密码长度:\n"))
passwd_num = int(input("How much passwds do you prefer to generate:\n你想生成几组密码供挑选？\n"))
source_str = string.ascii_letters + string.digits + string.punctuation
for i in range(passwd_num):
    RandomPassword = ''.join(random.sample(source_str,length))
    print(RandomPassword)
'''


'''
import string, random
length = int(input("The Password Length You Want to Set： \n请输入你想设置的密码长度:\n"))
passwd_num = int(input("How much passwds do you prefer to generate:\n你想生成几组密码供挑选？\n"))
passwd_type = input('What kind of passwd do you want to generate:\nL for letters only, D for letters & digits, P for letters & punctuation,default for complicate password\n请输入你要生成的密码类型：\nL表示仅英文大小写字母，D表示英文字母+数字，P表示英文字母+标点符号，默认英文字母+数字+标点符号、\n' )
for i in range(passwd_num):
    if passwd_type.title() == 'L':
        RandomPassword = ''.join(random.sample(string.ascii_letters,length))
    elif passwd_type.title() == 'D':
        RandomPassword = ''.join(random.sample((string.ascii_letters + string.digits),length))
    elif passwd_type.title() == 'P':
        RandomPassword = ''.join(random.sample((string.ascii_letters+string.punctuation),length))
    else:
        RandomPassword = ''.join(random.sample((string.ascii_letters+string.digits+string.punctuation),length))
    print(RandomPassword)
'''

import string, random
length = int(input("The Password Length You Want to Set： \n请输入你想设置的密码长度:\n"))
passwd_num = int(input("How much passwds do you prefer to generate:\n你想生成几组密码供挑选？\n"))
passwd_type = input('What kind of passwd do you want to generate:\nL for letters only, D for letters & digits, P for letters & punctuation,default for complicate password\n请输入你要生成的密码类型：\nL表示仅英文大小写字母，D表示英文字母+数字，P表示英文字母+标点符号，默认英文字母+数字+标点符号、\n' )
f = open('.mycode.txt','w')
for i in range(passwd_num):
    if passwd_type.title() == 'L':
        RandomPassword = ''.join(random.sample(string.ascii_letters,length))
    elif passwd_type.title() == 'D':
        RandomPassword = ''.join(random.sample((string.ascii_letters + string.digits),length))
    elif passwd_type.title() == 'P':
        RandomPassword = ''.join(random.sample((string.ascii_letters+string.punctuation),length))
    else:
        RandomPassword = ''.join(random.sample((string.ascii_letters+string.digits+string.punctuation),length))
    f.write('{0}\n'.format(''.join(RandomPassword)))
    print(RandomPassword)