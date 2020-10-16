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
    def largestNumber(self, nums: List[int]) -> str:
        """
        Inspired from discussion: https://leetcode.com/problems/largest-number/discuss/213599/Thinking-Process-in-Python
        :param nums:
        :return:
        """
        from functools import cmp_to_key
        def comp_func(x, y):
            if int(x+y) > int(y+x):
                return 1
            elif int(x+y) == int(y+x):
                return 0
            else:
                return -1
        nums = [str(value) for value in nums]
        nums.sort(key=cmp_to_key(comp_func), reverse=True)
        return str(int("".join(nums)))

nums = [3,30,34,5,9]
# Output: "9534330"
res = Solution().largestNumber(nums)
print(res)