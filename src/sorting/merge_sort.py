# -*- coding: utf-8 -*-
# @File    : merge_sort.py
# @Author  : Hua Guo
# @Disc    :

def mergeSort(lst) -> None:
    length = len(lst)
    if length <= 1:
        return
    else:
        mid = length // 2
        left_half = lst[:mid]
        right_half = lst[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        left_idx = 0
        right_idx = 0
        total_idx = 0
        while left_idx<mid and right_idx<length-mid:
            if left_half[left_idx] < right_half[right_idx]:
                lst[total_idx] = left_half[left_idx]
                left_idx += 1
            else:
                lst[total_idx] = right_half[right_idx]
                right_idx += 1
            total_idx += 1
        while left_idx < mid:
            lst[total_idx] = left_half[left_idx]
            total_idx += 1
            left_idx += 1
        while right_idx < length-mid:
            lst[total_idx] = right_half[right_idx]
            total_idx += 1
            right_idx += 1

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)