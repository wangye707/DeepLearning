#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : read1.py
# @Author: WangYe
# @Date  : 2020/2/6
# @Software: PyCharm
path = 'train.list'
with open(path,'w') as f:

    for i in range(1,99997):
        ss = str(i)
        if i<10000:
            while len(ss) < 5:
                ss = '0' + ss
        print(ss)
        s = 'train/images/'+ss+'.png'+' '+'train/labels/'+ss+'.png'+'\n'
        # f.write(s)