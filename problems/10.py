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
#     def isMatch(self, s: str, p: str) -> bool:
#         pass

class Solution(object):
    def isMatch(self, s, p):
        """
        Inspired from youtube video: regular expression dynamic programming
        :param s:
        :param p:
        :return:
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for col in range(1, len(p)+1):
            if p[col-1] == "*":
                # s[0] can not be "*"
                dp[0][col] = dp[0][col-2]
        for row in range(1, len(s) + 1):
            for col in range(1, len(p) + 1):
                if p[col-1] == "*":
                    dp[row][col] = dp[row][col-2]
                    if s[row-1] == p[col-2] or p[col-2] == ".":
                        if dp[row-1][col]:
                            dp[row][col] = dp[row-1][col]
                if s[row-1] == p[col-1] or p[col-1] == ".":
                    dp[row][col] = dp[row-1][col-1]
        # for idx, lst in enumerate(dp):
        #     print(idx)
        #     print(lst)
        return dp[-1][-1]


s = "aa"
p = "a*"
res = Solution().isMatch(s, p)
print(res)