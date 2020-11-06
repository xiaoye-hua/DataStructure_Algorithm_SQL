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
    def hammingWeight(self, n: int) -> int:
        res = 0
        quotient = n
        while quotient != 0:
            quotient, reminder = divmod(quotient, 2)
            if reminder == 1:
                res += 1
        return res

n = 3
res = Solution().hammingWeight(n)
print(res)