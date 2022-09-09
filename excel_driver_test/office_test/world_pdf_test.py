'''
pip install docx2pdf 安装工具包
导入工具包

'''
from docx2pdf import convert
import os
#单个转换
#convert("C:/Users/os_wulx/Desktop/lily.docx","C:/Users/os_wulx/Desktop/Test1.pdf")
#文件位置
path = ("C:/Users/os_wulx/Desktop/姜宇婷-设计师作品集&简历-13167338611")
#定义一个list，用来存放文件列表
files = []
for file in os.listdir(path):
    if file.endswith(".docx"):
        files.append(path+file)
for file in files:
    convert(file,file + '.pdf')
    print(file+'转换成功')
print('所有文件转换完成!!!')
quit()

