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
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = 0
        for unique_num in range(1, k+1):
            count = max(count, self.helper(s, 1, unique_num))
        return count

    def helper(self, s, k, unique_num):
        start = end = cur_unique_num = no_less_thanK_num = count = 0
        # a->z  : 97->122
        char_map = [0] * 128
        while end < len(s):
            if char_map[ord(s[end])] == 0:
                cur_unique_num += 1
            char_map[ord(s[end])] += 1
            if char_map[ord(s[end])] == k:
                no_less_thanK_num += 1
            end += 1

            while cur_unique_num > unique_num:
                if char_map[ord(s[start])] == k:
                    no_less_thanK_num -= 1
                char_map[ord(s[start])] -= 1
                if char_map[ord(s[start])] == 0:
                    cur_unique_num -= 1
                start += 1
            if cur_unique_num == no_less_thanK_num:
                count = max(count, end - start)
        return count


# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

s = "aa"
k = 1
res = Solution().lengthOfLongestSubstringKDistinct(s, k)
print(res)