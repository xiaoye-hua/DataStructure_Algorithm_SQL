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
    def reverseBits(self, n: int) -> int:
        bits = 32
        res = 0
        quotient = n
        for idx in range(bits):
            power = bits - idx -1
            quotient, remainder = divmod(quotient, 2)
            res += remainder * 2**power
        return res


n = -3
res = Solution().reverseBits(n)
print(res)