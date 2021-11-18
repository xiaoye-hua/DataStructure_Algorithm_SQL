# -*- coding: utf-8 -*-
# @File    : insert_sort.py
# @Author  : Hua Guo
# @Disc    :


def insert_sort(lst, binary_search=False) -> None:
    if len(lst) <= 1:
        return lst
    for idx in range(1, len(lst)):
        ordered_right_boundary = idx-1
        while ordered_right_boundary >=0 and lst[ordered_right_boundary]>lst[idx]:
            lst[idx], lst[ordered_right_boundary] = lst[ordered_right_boundary], lst[idx]
            ordered_right_boundary -= 1
        # lst.insert(ordered_right_boundary+1, lst[idx])

alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)