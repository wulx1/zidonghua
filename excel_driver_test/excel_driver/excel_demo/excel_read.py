import sys

import openpyxl

from excel_driver_test.excel_driver.web_keys.web_ui import WebDemo

sys.path.append('../web_keys/web_ui.py')
from excel_driver_test.excel_driver.web_keys import web_ui

'''
excel文件的读取流程
1.打开excel
2.读取指定的sheet页
3.获取sheet页的数据
'''
'''
自动化测试用例（基于关键字驱动+Excel数据驱动来实现）
1.启动浏览器
2.访问百度网址
3.实现一个搜索的输入
4.点击搜索的按钮，执行整个搜索流程
5.关闭浏览器
'''

#打开excel文件
excel = openpyxl.load_workbook('../excel_file/test.xlsx')
#指定需要的sheet页
#sheet = excel['sheet1']
#获取多个sheet页
sheets = excel.sheetnames
for sheet1 in sheets:
    sheet = excel[sheet1]
   # print(sheet.values)
    #print(type(sheet.values))
    for values in sheet.values:
        params = {}
        params['name'] = values[2]
        params['value'] = values[3]
        params['txt'] = values[4]
        #结合文件来进行判断
        if type(values[0]) is int:
            print(values)
            if values[1] == 'browser':


                wd = WebDemo(params['txt'])
            else:
                getattr(wd,values[1])(**params)
        else:
            pass

        #print(values)
    #获取excel中的参数内容


