'''
脚本功能：按照文件后缀名分门别类整理文件夹，并将同类型的文件移动到同个子文件夹中。
'''

import os
import shutil
src_folder = input('Type the source folder:\n输入你想整理的文件夹的绝对路径：')
des_folder = input('Type the destination folder:\n输入整理后文件放置的文件夹绝对位置：')
files = os.listdir(src_folder)
print('Files sorting now...\n文件整理中...')
for file in files:
    src_path = src_folder + file
    if os.path.isfile(src_path):
        des_path = des_folder + file.split('.')[-1]
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        shutil.move(src_path,des_path)
print('Done!\n文件整理完毕！')