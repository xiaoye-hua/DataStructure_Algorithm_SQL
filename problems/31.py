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
    def nextPermutation(self, nums: List[int]) -> None:
        """
        inspired from discussion: https://leetcode.com/problems/next-permutation/discuss/229211/Python-solution
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Two steps:
            1. find index a, change nums[a] to a bigger number --> we can only find the target number on the right of index a (Otherwise, the whole number will be smaller)
            2. change nums[a+1:] to the smallest number
        """
        if len(nums) == 0 or not nums:
            return
        idx = len(nums) -1
        while nums[idx-1]>=nums[idx] and idx-1>=0:
            idx -= 1
        if idx-1<0:
            nums.reverse()
        else:
            target_idx = idx-1
            idx = len(nums) - 1
            while nums[idx] <= nums[target_idx]:
                idx -= 1
            nums[idx], nums[target_idx] = nums[target_idx], nums[idx]
            begin_idx, end_idx = target_idx+1, len(nums)-1
            while end_idx-begin_idx>=1:
                nums[begin_idx], nums[end_idx] = nums[end_idx], nums[begin_idx]
                begin_idx += 1
                end_idx -= 1




        # n = len(nums)
        # for i in range(n-1, 0, -1):
        #     if nums[i] > nums[i-1]:
        #         j = i
        #         while j < n and nums[j] > nums[i-1]:
        #             idx = j
        #             j += 1
        #         nums[idx], nums[i-1] = nums[i-1], nums[idx]
        #         for k in range((n-i)//2):
        #             nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]
        #         break
        # else:
        #     nums.reverse()


# nput
# [1,3,2]
# Output
# [2,3,1]
# Expected
# [2,1,3]

nums = [1, 3, 2]
# expected: [2, 3, 2, 1, 4, 5]
res = Solution().nextPermutation(nums)
print(nums)