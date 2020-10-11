#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        stack = []
        operator = "+"
        s += "+"
        for idx, string in enumerate(s):
            if string == " ":
                continue
            elif string.isdigit():
                number = number*10 + int(string)
            else:
                # string != " " and not string.isdigit():
                if operator == "+":
                    stack.append(number)
                elif operator == "-":
                    stack.append(-number)
                elif operator == "*":
                    stack.append(
                        stack.pop(-1) * number
                    )
                else:
                    # print(stack[-1])
                    # print(number)
                    stack.append(
                        int(stack.pop(-1)/number)
                    )
                operator = string
                number = 0
            # print(stack)
        return sum(stack)



s = "-5"
# Output: 3
res = Solution().calculate(s)
print(res)


# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23