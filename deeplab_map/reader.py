#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : reader.py
# @Author: WangYe
# @Date  : 2020/1/28
# @Software: PyCharm
import os
import csv
path_name = []
path = 'dataset'
path1 = path +'/'+ os.listdir(path)[0]
new_path = os.listdir(path1)  #image label

for i in new_path:
    path2 = path1 + '/' + i #dataset/train/image
    path3 = os.listdir(path2)  #image_0
    for j in path3:
        path4 = path2 + '/' + j
        image_name = os.listdir(path4)
        for k in image_name:
            name = path4 + '/' + k
            path_name.append(name)
length = int(len(path_name)/2)
image_path = path_name[:length]
label_apth = path_name[length:]
f = open('path_list.csv','w',encoding='utf-8',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(["image","label"])
for i in range(len(image_path)):
    csv_writer.writerow([image_path[i],label_apth[i]])#
    #csv_writer.writerow([1, 2])
    print([image_path[i],label_apth[i]])
f.close()


