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
    def maxArea(self, height: List[int]) -> int:
        res = 0
        if len(height) < 2:
            return res
        begin, end = 0, len(height)-1
        while end>begin:
            res = max(res, (end-begin)*min(height[begin], height[end]))
            if height[begin]>=height[end]:
                end -= 1
            else:
                begin += 1
        return res

#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


height = [1,8,6,2,5,4,8,3,7]
res = Solution().maxArea(height)
print(res)