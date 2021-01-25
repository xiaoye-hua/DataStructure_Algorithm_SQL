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
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [-float("inf") for _ in range(len(nums))]
        dp_min = [float("inf") for _ in range(len(nums))]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for idx in range(1, len(nums)):
            dp_max[idx] = max(dp_max[idx-1]*nums[idx], dp_min[idx-1]*nums[idx], nums[idx])
            dp_min[idx] = min(dp_max[idx-1]*nums[idx], dp_min[idx-1]*nums[idx], nums[idx])
        # print(dp_max)
        # print(dp_min)
        return max(dp_max)