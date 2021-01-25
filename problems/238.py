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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        p = 1
        for idx, value in enumerate(nums):
            res[idx] *= p
            p *= value
        p = 1
        for idx in range(len(nums) - 1, -1, -1):
            res[idx] *= p
            p *= nums[idx]
        return res
