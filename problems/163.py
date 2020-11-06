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
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            if upper - lower ==0:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
        if lower != nums[0]:
            nums.insert(0, lower-1)
        if upper != nums[-1]:
            nums.append(upper+1)
        # print(nums)
        idx = 0
        res = []
        while idx < len(nums)-1:
            while idx< len(nums)-1 and nums[idx+1] - nums[idx] == 1:
                idx += 1
            if idx == len(nums)-1:
                return res
            begin = nums[idx]
            end = nums[idx+1]
            if end - begin == 2:
                res.append(str(begin+1))
            else:
                res.append(
                    str(begin + 1) + "->" + str(end -1)
                )
            idx += 1
        return res

# []
# 1
# 1
# Input: \
nums = [0, 1]
lower = 0
upper = 1
# Output: ["2","4->49","51->74","76->99"]
# Explanation: The ranges are:
# [2,2] --> "2"
# [4,49] --> "4->49"
# [51,74] --> "51->74"
# [76,99] --> "76->99"
res = Solution().findMissingRanges(nums, lower, upper)
print(res)