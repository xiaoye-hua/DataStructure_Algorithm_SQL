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
    def multiply(self, num1: str, num2: str) -> str:
        """
        Inspired from discussion: https://leetcode.com/problems/multiply-strings/discuss/17615/Simple-Python-solution-18-lines
        :param num1:
        :param num2:
        :return:
        """
        position = [0] * (len(num2) + len(num1))
        pos = len(position)-1
        for n1 in reversed(num1):
            tmp_pos = pos
            for n2 in reversed(num2):
                position[tmp_pos] += int(n1) * int(n2)
                position[tmp_pos-1] += position[tmp_pos]//10
                position[tmp_pos] = position[tmp_pos]%10
                tmp_pos -= 1
            pos -= 1
        idx = 0
        while idx< len(position) and position[idx]==0:
            idx += 1
        if idx == len(position):
            res = "0"
        else:
            res = "".join([str(ele) for ele in position[idx:]])
        # print(position)
        return res
# # Input: num1 = "2", num2 = "3"
# # Output: "6"
# # Example
# # 2:
# #
# # Input: num1 = "123", num2 = "456"
# # Output: "56088"

# class Solution:
#     def multiply(self, num1, num2):
#         product = [0] * (len(num1) + len(num2))
#         pos = len(product) - 1
#
#         for n1 in reversed(num1):
#             tempPos = pos
#             for n2 in reversed(num2):
#                 product[tempPos] += int(n1) * int(n2)
#                 product[tempPos - 1] += product[tempPos] // 10
#                 product[tempPos] %= 10
#                 tempPos -= 1
#             pos -= 1
#
#         pt = 0
#         while pt < len(product) - 1 and product[pt] == 0:
#             pt += 1
#
#         return ''.join(map(str, product[pt:]))

num1 = "123"
num2 = "456"
res = Solution().multiply(num1, num2)
print(res)