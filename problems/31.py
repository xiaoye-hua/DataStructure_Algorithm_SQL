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


class Solution(object):
    def nextPermutation(self, nums):
        """
        inspired from discussion: https://leetcode.com/problems/next-permutation/discuss/229211/Python-solution
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 1:
            return
        idx = length -1

        while idx>=1:
            # if nums[idx] < current_min:
                # current_min = nums[idx]
                # min_idx = idx
            if nums[idx-1]>=nums[idx]:
                idx -= 1
            else:
                break
        # print(idx)
        # idx -= 1
        # print(idx)
        if idx == 0:
            nums.reverse()
        else:
            idx -= 1
            min_idx = None
            current_min = float("inf")
            for current_idx in range(idx+1, len(nums)):
                ele = nums[current_idx]
                if ele > nums[idx] and ele < current_min:
                    min_idx = current_idx
                    current_min = ele
            nums[idx], nums[min_idx] = nums[min_idx],  nums[idx]
            # print(nums)
            # print(idx)
            for first_idx in range(idx+1, length-1):
                for second_idx in range(first_idx+1, length):
                    if nums[second_idx] < nums[first_idx]:
                        nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]





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

nums = [2, 3, 1]
# expected: [2, 3, 2, 1, 4, 5]
res = Solution().nextPermutation(nums)
print(nums)