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
    def numDecodings(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        nums = [str(value) for value in list(range(1, 27))]
        dp = [0 for _ in range(length)]
        if s[0] in nums:
            dp[0] = 1
        if length>1:
            for idx in range(1, length):
                res = []
                if idx == 1:
                    if dp[idx-1] != 0 and s[idx] in nums:
                        dp[idx] += 1
                    if s[:2] in nums:
                        dp[idx] += 1

                else:
                    if dp[idx-1] != 0 and s[idx] in nums:
                        dp[idx] += dp[idx-1]
                    if dp[idx-2] != 0 and s[idx-1:idx+1] in nums:
                        dp[idx] += dp[idx-2]
                # print(dp)
        return dp[-1]

s = "226"
res = Solution().numDecodings(s)
print(res)