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
    def strongPasswordChecker(self, s: str) -> int:
        res = 0
        if len(s) < 6 or len(s) > 20:
            pass
        digit_num = 0
        low_num = 0
        upper_num = 0
        for ele in s:
            if ele.isdigit():
                digit_num += 1
            elif ele.islower():
                low_num += 1
            elif ele.isupper():
                upper_num += 1


s = "a"
res = Solution().strongPasswordChecker(s)
print(res)