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
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # if len(nums) == 0:
        #     if lower == upper:
        #         return [str(lower)]
        #     else:
        #         return [str(lower) + "->" + str(upper)]
        # if lower != nums[0]:
        #     nums.insert(0, lower)
        # if upper != nums[-1]:
        #     nums.insert(-1, upper)
        idx = 0
        res = []
        while idx < len(nums)-1:
            if nums[idx+1] - nums[idx] == 1:
                begin_idx = idx
                while idx < len(nums)-1 and nums[idx+1] - nums[idx] == 1:
                    idx += 1
                res.append(str(nums[begin_idx]) + "->" + str(nums[idx]))
            else:
                res.append(str(nums[idx]))
            idx +=1
        if idx == len(nums)-1:
            res.append(str(nums[-1]))
        return res

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
nums = [0,1,2,4,5,7]
res = Solution().summaryRanges(nums)
print(res)