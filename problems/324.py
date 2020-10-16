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
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Inspired from dicussion:https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
        Do not return anything, modify nums in-place instead.
        """
        import math
        nums.sort()
        half_idx = math.ceil(len(nums)/2)
        first_half = nums[:half_idx]
        second_half = nums[half_idx:]
        # print(first_half)
        # print(second_half)
        for idx in range(len(nums)):
            if idx%2==0:
                nums[idx] = first_half.pop(-1)
            else:
                nums[idx] = second_half.pop(-1)
        # return nums

nums = [4, 5, 5, 6]
Solution().wiggleSort(nums)
print(nums)