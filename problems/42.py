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
    def trap(self, height: List[int]) -> int:
        # """
        # Approach two
        # :param height:
        # :return:
        # """
        # res = 0
        # if len(height) < 2:
        #     return res
        # previous = 0
        # begin, end = 0, len(height)-1
        # while begin<end:
        #     while begin<end and height[begin]<=previous:
        #         begin += 1
        #     while begin<end and height[end]<=previous:
        #         end -= 1
        #     # height_diff = min(height[begin], height[end])-previous
        #     # length = end-begin - sum([min(min(height[begin], height[end])-ele, 0) for ele in height[begin: end]])
        #     diff = sum([max(min(height[begin], height[end])-max(ele, previous), 0) for ele in height[begin: end]])
        #     # print(f"Previous: {previous}")
        #     # print(f"diff: {diff}")
        #     res += diff
        #     previous = min(height[begin], height[end])
        # return res
        res = 0
        left, right = 0, len(height) - 1
        max_height = 0
        while left < right:
            if height[left] > max_height and height[right] > max_height:
                new_max_height = min(height[left], height[right])
                diff = new_max_height - max_height
                duplicated = sum(
                    [min(diff, height[idx] - max_height) for idx in range(left + 1, right) if height[idx] > max_height])
                res = res + diff * (right - left - 1) - duplicated
                max_height = new_max_height
            # print(res)
            # print(left)
            # print(right)
            # print("******")
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
height = [0,1,0,2,1,0,1,3,2,1,2,1]
res = Solution().trap(height)
print(res)