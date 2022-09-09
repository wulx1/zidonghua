#
# #
# # def sum(a,b):
# #     sum1 = a+b
# #     print(sum1)
# #     return sum1
# #
# #
# # sum1=sum(10,20)
# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError, Argument:
#         print("参数没有包含数字\n", Argument)
#
#
# # 调用函数
# temp_convert("xyz")
'''
深浅拷贝的区别
'''
import copy
# old_list=[1,2,"string",(1,2)]
# new_list = copy.copy(old_list)
# old_list[1] += 22
# old_list[2] +=  "s"
# old_list[3] += (3,)
# print("old list:",old_list)
# print("new list:",new_list)

'''
判断number是否位素数
'''
# number = 9
# for i in range(2,number):
#     print(i)
#     if number % i ==0:
#         is_prime = False
#         break
# else:
#     is_prime = True
# print(is_prime)

# for i in range(10):
#     print(i)
#     if i ==4:
#         break
# else:
#     print("hello")

#随机整数
# from random import randint
# res = randint(0,4)
# if res == 0:
#     print('num is 0',res)
# elif res==1:
#     print("num is 1",res)
# elif res ==2:
#     print('num is 3',res)
# elif res ==3:
#     print('num is 3',res)
# else:
#     print('num is 4',res)

from random import randint
res1 =randint(0,1)
res2 = randint(0,1)
if res1 ==0:
    if res2 != 0:
        print(res1,res2)
    else:
        print("无效")
else:
    if res2>0:
        print(res2,res1)
    else:
        print("无效")
