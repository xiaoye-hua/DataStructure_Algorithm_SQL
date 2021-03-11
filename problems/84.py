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
    def largestRectangleArea(self, heights: List[int]) -> int:
        # https: // www.youtube.com / watch?v = zx5Sw9130L0 & feature = emb_logo
        # heights.append(0)
        # stack = [-1]
        # ans = 0
        # for i in range(len(heights)):
        #     while heights[i] < heights[stack[-1]]:
        #         h = heights[stack.pop()]
        #         w = i - stack[-1] -1
        #         ans = max(h*w, ans)
        #     stack.append(i)
        # return ans
        heights.append(0)
        index_stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[index_stack[-1]]:
                h = heights[index_stack.pop(-1)]
                w = i - index_stack[-1] -1
                ans = max(ans, h*w)
            index_stack.append(i)
        return ans



height = [2,1,5,6,2,3]
# Output: 10
res = Solution().largestRectangleArea(height)
print(res)