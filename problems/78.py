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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        tiles = nums
        self.res = [
            []
        ]
        for length in range(1, len(tiles) + 1):
            self.backtrack(current_lst=[], remain_tiles=list(tiles), length_left=length, begin_idx=0)
        return self.res

    def backtrack(self,current_lst, remain_tiles, length_left, begin_idx):
        if length_left == 0:
            self.res.append(current_lst)
        else:
            length_left -= 1
            for idx, tile in enumerate(remain_tiles):
                if idx >= begin_idx:
                    new_remain = remain_tiles.copy()
                    self.backtrack(current_lst+ [tile], new_remain, length_left, idx+1)
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]

nums = [1, 2,3]
res = Solution().subsets(nums)
print(res)