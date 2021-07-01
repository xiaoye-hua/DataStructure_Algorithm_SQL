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

import copy


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        begin_idx = 0
        end_idx = len(height) - 1
        max_height = 0
        while begin_idx < end_idx:
            if height[begin_idx] > max_height and height[end_idx] > max_height:
                curr_height = min(height[begin_idx], height[end_idx])
                inc = 0
                for idx in range(begin_idx, end_idx+1):
                    ele = height[idx]
                    if ele >= curr_height:
                        continue
                    elif ele > max_height:
                        inc += curr_height - ele
                    else:
                        inc += curr_height - max_height

                # to_remove = sum([min(curr_height, height[idx]) for idx in range(begin_idx, end_idx+1)])
                # inc = (max_height - curr_height) * (end_idx-begin_idx+1) - to_remove
                # print('*'*8)
                # print(height[begin_idx])
                # print(height[end_idx])
                # print(inc)
                res += inc
                max_height = curr_height

            if height[begin_idx] < height[end_idx]:
                begin_idx += 1
            else:
                end_idx -= 1
        return res


        #
        # Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        # Output: 6
        # Explanation: The
        # above
        # elevation
        # map(black
        # section) is represented
        # by
        # array[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1].In
        # this
        # case, 6
        # units
        # of
        # rain
        # water(blue
        # section) are
        # being
        # trapped.

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = Solution().trap(height)
print(res)


