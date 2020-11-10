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
    def reorderSpaces(self, text: str) -> str:
        if not text:
            return ""
        words = []
        space_num = 0
        idx = 0
        while idx < len(text):
            ele = text[idx]
            if ele == " ":
                space_num +=1
                idx += 1
            else:
                w = ""
                while idx < len(text) and text[idx] != " ":
                    w += text[idx]
                    idx += 1
                words.append(w)
        res = None
        if len(words) == 1:
            res = words[-1] + " "*space_num
        else:
            quotient, remainder = divmod(space_num, len(words)-1)
            seq = " "*quotient
            res = seq.join(words) + " "*remainder
        return res



# Input: text = "  this   is  a sentence "
# Output: "this   is   a   sentence"
# Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
# Example 2:
#
# Input: text = " practice   makes   perfect"
# Output: "practice   makes   perfect "
# Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
# s = "aaabb"
text = "a"
res = Solution().reorderSpaces(text)
print(res)