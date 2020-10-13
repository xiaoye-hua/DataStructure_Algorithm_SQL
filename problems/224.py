#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    """
    Approach one: inspired from https://leetcode.com/problems/expression-add-operators/
    """
    def calculate(self, s):
        s = "+(+" + s + ")"
        s = s.replace("++", "+").replace("+-", "-")
        # print(s)
        stack = []
        for string in s:
            if string == ")":
                total = 0
                while stack[-1] != "(":
                    num_str = stack.pop(-1)
                    # print(num_str)
                    total += int(num_str)
                stack.pop(-1)
                if stack.pop(-1) == "+":
                    sign = 1
                else:
                    sign = -1
                stack.append(
                    total * sign
                )
            elif string.isdigit() and stack[-1][-1] in "+-0123456789":
                stack[-1] += string
            elif string != " ":
                stack.append(string)
            # print(stack)
        return stack[-1]


    # """
    # Approach two
    # """
    # def calculate(self, s: str) -> int:
    #     self.s = s
    #     self.s_len = len(s)
    #     idx = 0
    #     res = 0
    #     # print(self.s_len)
    #     while idx < self.s_len:
    #         # print("#" * 20)
    #         # # print(idx)
    #         # print(res)
    #         # print(self.s[idx])
    #         if s[idx] == " ":
    #             idx += 1
    #             continue
    #         elif s[idx] in ["-", "+"]:
    #             add = s[idx] == "+"
    #             idx += 1
    #             while s[idx] == " ":
    #                 idx += 1
    #                 continue
    #             if s[idx] == "(":
    #                 new_num, idx= self.handle_parentheses(idx)
    #             else:
    #                 new_num, idx = self.get_num(idx)
    #             if add:
    #                 res += new_num
    #             else:
    #                 res -= new_num
    #         else:
    #             if s[idx] == "(":
    #                 res, idx= self.handle_parentheses(idx)
    #             else:
    #                 res, idx = self.get_num(idx)
    #         # print(res)
    #     return res
    #
    # def get_num(self, begin_idx):
    #     res = 0
    #     while begin_idx<self.s_len and self.s[begin_idx].isdigit():
    #         res = res*10 + int(self.s[begin_idx])
    #         begin_idx += 1
    #     return res, begin_idx
    #
    # def handle_parentheses(self, begin_idx: int):
    #     res = 0
    #     idx = begin_idx + 1
    #     while idx<self.s_len and self.s[idx] != ")":
    #         if idx == 8:
    #             print()
    #         if self.s[idx] == " ":
    #             idx += 1
    #             continue
    #         elif self.s[idx] in ["-", "+"]:
    #             add = self.s[idx] == "+"
    #             idx += 1
    #             while self.s[idx] == " ":
    #                 idx += 1
    #                 continue
    #             if self.s[idx] == "(":
    #                 new_num, idx = self.handle_parentheses(idx)
    #             else:
    #                 new_num, idx = self.get_num(idx)
    #             if add:
    #                 res += new_num
    #             else:
    #                 res -= new_num
    #         else:
    #             if self.s[idx] == "(":
    #                 res, idx = self.handle_parentheses(idx)
    #             else:
    #                 res, idx = self.get_num(idx)
    #     if idx < self.s_len and self.s[idx] == ")":
    #         return res, idx+1
    #     else:
    #         return res, idx



s = "(1+(4+5+2)-3)+(6+8)"
# Output: 3
# s = " 2-1 + 2 "
res = Solution().calculate(s)
print(res)


# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23