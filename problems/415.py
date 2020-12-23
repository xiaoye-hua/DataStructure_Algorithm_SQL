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


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_lst = list(num1)
        num2_lst = list(num2)
        num1_lst.reverse()
        num2_lst.reverse()
        res = []
        remain = 0
        idx = 0
        while idx < len(num2_lst) and idx < len(num1_lst):
            remain, left = divmod(int(num1_lst[idx])+int(num2_lst[idx])+remain,10)
            res.append(str(left))
            idx += 1
        if idx >= len(num1_lst):
            target_lst = num2_lst
        else:
            target_lst = num1_lst
        while idx < len(target_lst):
            remain, left = divmod(int(target_lst[idx])+remain,10)
            res.append(str(left))
            idx += 1
        if remain != 0:
            res.append(str(remain))
        res.reverse()
        return "".join(res)



num1 = "345"
num2 = "589"
res = Solution().addStrings(num1, num2)
print(res)