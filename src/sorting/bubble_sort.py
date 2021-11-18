# -*- coding: utf-8 -*-
# @File    : bubble_sort.py
# @Author  : Hua Guo
# @Disc    :

def bubbleSort(alist, ascending=True):
    for unordered_boundary in range(len(alist)-1,0,-1):
        for i in range(unordered_boundary):
            if ascending:
                if alist[i]>alist[i+1]:
                    alist[i], alist[i+1] = alist[i+1], alist[i]
            else:
                if alist[i]<alist[i+1]:
                    alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist, ascending=True)
print(alist)
bubbleSort(alist, ascending=False)
print(alist)