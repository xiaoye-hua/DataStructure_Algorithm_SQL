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
    def encode(self, s: str) -> str:
        """
        Approach one: DFS with memory. inspired from https://leetcode.com/problems/encode-string-with-shortest-length/discuss/890402/Python-DFS-with-memo
        :param s:
        :return:
        """
        if not s:
            return s
        self.encode_map = {}
        self.dfs(s)
        # print(self.encode_map)
        return self.encode_map[s]

    def dfs(self, s):
        if not s:
            return s
        try:
            return self.encode_map[s]
        except:
            tmp_s = s
            for i in range(len(s)):
                cnt = self.get_repeat_cnt(s[:i+1], s[i+1:])
                for k in range(1, cnt+1):
                    origin_left_len = k*(i+1)
                    encode_left = self.dfs(s[:i+1])
                    tmp_left = "".join(
                        [str(k), "[", encode_left, "]"]
                    )
                    if origin_left_len < len(tmp_left):
                        tmp_left = s[:origin_left_len]
                    tmp_right = self.dfs(s[origin_left_len:])
                    tmp = tmp_left + tmp_right
                    if len(tmp) < len(tmp_s):
                        tmp_s = tmp
            self.encode_map[s] = tmp_s
            return self.encode_map[s]

    def get_repeat_cnt(self, s1, s2):
        if len(s1) > len(s2):
            return 0
        length = len(s1)
        idx = 0
        cnt = 1
        while idx+length<=len(s2) and s1 == s2[idx: idx+length]:
            cnt += 1
            idx += length
        return cnt

        # Input: s = "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
# a: a; aa:aa; aaa: aaa; aaaa: aaaa; aaaaa: 5[a]
s = "aaaaa"
res = Solution().encode(s)
print(res)

#
# class Solution:
#     def encode(self, s: str) -> str:
#         if not s:
#             return ""
#
#         encode_map = {}
#
#         def getRepeat(s1, s2):
#             if len(s1) > len(s2):
#                 return 0
#
#             l = len(s1)
#             i = 0
#             cnt = 1
#             while i + l <= len(s2) and s2[i:i + l] == s1:
#                 cnt += 1
#                 i += l
#             return cnt
#
#         def dfs(s, encode_map):
#             if not s:
#                 return ""
#
#             if s in encode_map:
#                 return encode_map[s]
#
#             sol = s
#             for i in range(len(s)):
#                 cnt = getRepeat(s[:i + 1], s[i + 1:])
#                 for k in range(1, cnt + 1):
#                     j = (i + 1) * k
#                     encode_first = dfs(s[:i + 1], encode_map)
#                     tmp_first = str(k) + "[" + encode_first + "]"
#                     if len(tmp_first) >= j:
#                         tmp_first = s[:j]
#                     tmp_second = dfs(s[j:], encode_map)
#                     tmp = tmp_first + tmp_second
#                     if len(tmp) < len(sol):
#                         sol = tmp
#             encode_map[s] = sol
#             print(encode_map)
#             return sol
#
#         return dfs(s, encode_map)