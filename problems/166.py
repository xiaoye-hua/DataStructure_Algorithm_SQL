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
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        """
        Inspired from discussion https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51110/Do-not-use-python-as-cpp-here's-a-short-version-python-code
        :param numerator:
        :param denominator:
        :return:
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = "-" if numerator*denominator<0 else ""
        result = [sign+str(n), "."]
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))
        index = stack.index(remainder)
        result.insert(index+2, "(")
        result.append(")")
        return "".join(result).replace(".(0)", "").replace("(0)", "")


a = 2
b = 1
# a = 1
# b = 2
res = Solution().fractionToDecimal(a, b)
print(res)