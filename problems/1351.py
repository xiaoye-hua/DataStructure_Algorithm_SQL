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
    def countNegatives(self, grid: List[List[int]]) -> int:
        self.length = len(grid[0])
        res = 0
        for lst in grid:
            negtive_idx = self.get_num_for_single_row(lst)
            res = res + (self.length - negtive_idx)
        return res

    def get_num_for_single_row(self, lst):
        if lst[0]<0:
            return 0
        elif lst[-1] >=0:
            return self.length
        begin_idx = 0
        end_idx = self.length - 1
        while begin_idx < end_idx:
            mid_idx = (begin_idx + end_idx) // 2
            if lst[mid_idx] >= 0 and lst[mid_idx + 1] < 0:
                return mid_idx + 1
            elif lst[mid_idx] < 0 and lst[mid_idx - 1] >= 0:
                return mid_idx
            else:
                if lst[mid_idx] >= 0:
                    begin_idx = mid_idx
                else:
                    end_idx = mid_idx


grid =[[3,2],[1,0]]
res = Solution().countNegatives(grid)
print(res)