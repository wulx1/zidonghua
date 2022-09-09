# print("hello!python")
# print("hello! \' python")
# print("hello \npython")
# print('''hello
# my
# python''')
# print("您好，吃了吗！"+'张三')

# shopping_list = []
# s = 'hello '
# print(s.upper())
'''
编写一个计算求平均值的程序 ！！
'''
print("你好啊！这是一个计算平均值的程序，注意输入q中止程序")
user_input= input("请输入你要计算的数字：")
total = 0
count = 0
while user_input != "q" :
    num = float(user_input)
    total += num
    count += 1
    user_input = input("请继续输入你想要计算平均值的数字(注意输入q终止程序)：")
if count == 0:
    result = 0
else:
    result = total / count
print("你的计算结果为："+str(result))


