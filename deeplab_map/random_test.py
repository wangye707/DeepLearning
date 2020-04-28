#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : random_test.py
# @Author: WangYe
# @Date  : 2020/2/6
# @Software: PyCharm
path = 'train.list'
new_path = 'test.list'
with open(new_path,'w') as f1:
    with open(path) as f:
        lines = f.readlines()
        print(lines)
        for i in range(99999):
            if i%500==0:
                print(lines[i])
                # f1.write(lines[i])
