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
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] == ")":
                part = ")"
                current = part
                while len(stack) != 0 and current != "(":
                    current = stack.pop()
                    part = current+part
                if current == "(":
                    stack.append(part)
                else:
                    stack.append(part[:-1])
            else:
                stack.append(
                    s[idx]
                )
            idx += 1
        res = ""
        for ele in stack:
            if ele not in ["(", ")"]:
                res += ele
        return res


s = "(a(b(c)d)"
res = Solution().minRemoveToMakeValid(s)
print(res)


# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# Example 4:
#
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"