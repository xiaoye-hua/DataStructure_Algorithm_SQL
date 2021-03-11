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
    def subarraySum(self, nums: List[int], k: int) -> int:
        # """
        # First try: brute force --> time limit exceed
        # :param nums:
        # :param k:
        # :return:
        # """
        # sum_lst = [0]
        # for n in nums:
        #     sum_lst.append(
        #         sum_lst[-1] + n
        #     )
        # res = 0
        # for begin in range(len(nums)):
        #     for end in range(begin+1, len(nums)+1):
        #         current = sum_lst[end] - sum_lst[begin]
        #         if current == k:
        #             res += 1
        # return res
        """
        Second Approach: hash table
        :param nums:
        :param k:
        :return:
        """
        previous_sum = {
            0:1
        }
        current_sum = 0
        res = 0
        for n in nums:
            current_sum += n
            res += previous_sum.get(current_sum-k, 0)
            try:
                previous_sum[current_sum] += 1
            except:
                previous_sum[current_sum] = 1
        return res

nums = [-1,-1,1]
k = 0
res = Solution().subarraySum(nums, k)
print(res)