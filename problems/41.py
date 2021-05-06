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
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        inspired from discussion https://leetcode.com/problems/first-missing-                   positive/discuss/231337/Python-solution

        idx  0 --> n-1
        value 1 --> n+1
        res --> 1 --> n+1
        """
        # first_missing = [False] * (len(nums) + 1)
        for idx, value in enumerate(nums):
            while value <= len(nums) and value > 0:
                tmp = nums[value-1]
                nums[value-1] = float('inf')
                value = tmp
        print(nums)
        for idx, value in enumerate(nums):
            if value != float("inf"):
                return idx + 1
        return idx + 1


nums = [1, 2, 0]
# Output: 2
res = Solution().firstMissingPositive(nums)
print(res)