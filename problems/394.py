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
    def decodeString(self, s: str) -> str:
        stack = []
        for ele in s:
            if ele == "]":
                char = ""
                current_char = stack.pop()
                while current_char != "[":
                    char = current_char + char
                    current_char = stack.pop()
                num = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(
                    int(num) * char
                )
            else:
                stack.append(ele)
            # print("*"*20)
            # print(ele)
            # print(stack)
        return "".join(stack)

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
#
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz
s = "100[leetcode]"
# Output: "aaabcbc"
res = Solution().decodeString(s)
print(res)