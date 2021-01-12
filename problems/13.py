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
    def romanToInt(self, s: str) -> int:
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_value_map = dict(zip(romans, values))
        length = len(s)
        idx = 0
        res = 0
        while idx < length:
            if idx<length-1 and s[idx:idx+2] in roman_value_map.keys():
                res += roman_value_map[s[idx:idx+2]]
                idx += 2
            else:
                res += roman_value_map[s[idx]]
                idx += 1
        return res




num = "IV"
res = Solution().romanToInt(num)
print(res)

