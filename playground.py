#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List
import copy
import collections
import string

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList

import copy



import heapq
def moveZerosToEnd(arr):
  zero_begin_idx = None
  idx = 0
  min_heap = []
  while idx < len(arr):
    # print('*'*20)
    # print('idx:' + str(idx))
    # print('Before:')
    # print('Zeor idx is :' + str(zero_begin_idx))
    #print('lst is: ' + str(lst))
    if zero_begin_idx is None:
      if arr[idx] == 0:
        zero_begin_idx = idx
    elif arr[idx] != 0:
      arr[idx], arr[zero_begin_idx] = arr[zero_begin_idx], arr[idx]
      heapq.heappush(min_heap, idx)
      if len(min_heap) != 0:
        zero_begin_idx = heapq.heappop(min_heap)
      else:
        zero_begin_idx = idx
    elif arr[idx] == 0:
      heapq.heappush(min_heap, idx)
    idx += 1
  return arr


arr = [0,1,2,3,0,0,1,1,6,4,1]

res = moveZerosToEnd(arr)

print(res)