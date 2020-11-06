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


# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         """
#         First try: can't handle  positve + negative
#         :param a:
#         :param b:
#         :return:
#         """
#         if a == 0:
#             return b
#         operate_and = (a&b) << 1
#         operate_xor = a^b
#         # print("*"*20)
#         # print(operate_and)
#         # print(operate_xor)
#         return self.getSum(operate_and, operate_xor)

# Input: a = 1, b = 2
# Output: 3
# Example 2:
#
# Input: a = -2, b = 3
# Output: 1
class Solution:
    def addOne(self, a: int) -> int:
        c = 1
        while c > 0:
            c1 = c & a
            a ^= c
            c = c1 << 1
        return a

    def negate(self, a: int) -> int:
        return self.addOne(~a)

    def getSum(self, a: int, b: int) -> int:
        # When both are negative
        if a < 0 and b < 0:
            return self.negate(self.getSum(self.negate(a), self.negate(b)))
        result = 0
        mask = 1
        carry = 0
        # Assuming 32 bit
        for i in range(32):
            ai = a & mask
            bi = b & mask
            result |= (ai ^ bi ^ carry)
            carry = (ai & bi | ai & carry | bi & carry) << 1
            mask <<= 1
        # Special case
        if result == 0xFFFFFFFF:
            return self.negate(1)
        return result

a = 2
b = 100
res = Solution().getSum(a, b)
print(res)