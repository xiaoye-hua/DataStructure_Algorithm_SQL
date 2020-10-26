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


class NumArray:

    def __init__(self, nums: List[int]):
        length = len(nums)
        self.dp = [0 for _ in range(length+1)]
        for idx in range(length):
            self.dp[idx+1] = self.dp[idx] + nums[idx]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

s = "aaabb"
k = 3
res = Solution().longestSubstring(s, k)
print(res)