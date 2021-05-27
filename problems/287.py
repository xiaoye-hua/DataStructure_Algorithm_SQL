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
    def findDuplicate(self, nums: List[int]) -> int:
        """
        First try: similar solution from problem 41 --> failed
        Second try:  user extro space
        :param nums:
        :return:
        """
        # # first_missing = [False] * (len(nums) + 1)
        # for idx, value in enumerate(nums):
        #     if idx == value-1:
        #         nums[idx] = float('inf')
        #     else:
        #         while value <= len(nums) and value > 0:
        #             tmp = nums[value-1]
        #             # if tmp == float("inf"):
        #             #     return value
        #             if nums[value-1] == float("inf"):
        #                 return value
        #             else:
        #                 nums[value-1] = float('inf')
        #             value = tmp
        # # print(nums)
        # # for idx, value in enumerate(nums):
        # #     if value != float("inf"):
        # #         return idx + 1
        # # return idx + 1

        num_lst = [float("inf")] * len(nums)
        for value in nums:
            if num_lst[value-1] != float('inf'):
                return value
            else:
                num_lst[value-1] = 1



# Input:\
nums = [1,3,4,2,2]
# Output: 3
res = Solution().findDuplicate(nums)
print(res)

# begin...
# [[True, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, Fals...
# end...
# [[True, False, False, False, False, False, False, False, False, False, False, False],
#  [False, True, False, False, False, False, False, False, False, False, False, False],
#  [False, False, True, False, True, False, False, False, False, False, False, False],
#  [False, False, False, True, True, False, False, False, False, False, False, False],
#  [False, False, False, False, True, False, False, False, False, False, False, False],
#  [False, False, False, False, False, True, False, True, False, False, False, False],
#  [False, False, False, False, False, False, True, True, False, False, False, False],
#  [False, False, False, False, False, False, False, True, False, False, False, False],

#  [False, False, False, False, False, False, False, False, True, False, True, True], s_idx=8 p_idx=11
#  [False, False, False, False, False, False, False, False, False, True, True, True],
#  [False, False, False, False, False, False, False, False, False, False, True, True],
#  [False, False, False, False, False, False, False, False, False, False, False]




