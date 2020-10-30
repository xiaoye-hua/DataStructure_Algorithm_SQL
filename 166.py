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
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        return str(numerator/denominator)


#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:
#
# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# Example 4:
#
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
# Example 5:
#
# Input: numerator = 1, denominator = 5
# Output: "0.2"

a = 4
b = 333
res = Solution().fractionToDecimal(a, b)
print(res)