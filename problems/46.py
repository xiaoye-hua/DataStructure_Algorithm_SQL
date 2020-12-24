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
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtracks(current_lst=[], remain_lst=nums)
        return self.res

    def backtracks(self, current_lst, remain_lst):
        if len(remain_lst) == 0:
            self.res.append(current_lst)
        for ele in remain_lst:
            new_remain = remain_lst.copy()
            new_remain.remove(ele)
            self.backtracks(current_lst+[ele], new_remain)


# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
nums = [1,2,3]
res = Solution().permute(nums)
print(res)