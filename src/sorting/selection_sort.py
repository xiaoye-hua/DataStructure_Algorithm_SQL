# -*- coding: utf-8 -*-
# @File    : selection_sort.py
# @Author  : Hua Guo
# @Disc    :


def selection_sort(lst) -> None:
    length = len(lst)
    for unordered_right_boundary in range(length-1, 0, -1):
        max_idx = 0
        for idx in range(0, unordered_right_boundary+1):
            if lst[idx] > lst[max_idx]:
                max_idx = idx
        lst[max_idx], lst[unordered_right_boundary] = lst[unordered_right_boundary], lst[max_idx]


alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)