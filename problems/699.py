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
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """
        Inspired from huahua leetcode youtube video
        :param positions:
        :return:
        """
        intervals = []
        res = [0]
        for lst in positions:
            left = lst[0]
            right = lst[0] + lst[1]
            sildelength = lst[1]
            base_height = 0
            for interval in intervals:
                begin, end, current_height= interval
                if left>=end or right<=begin:
                    continue
                base_height = max(base_height, current_height)
            height = sildelength+base_height
            intervals.append(
                [left, right, height]
            )
            res.append(
                max(res[-1], height)
            )
        return res[1:]



positions = [[1, 2], [2, 3], [6, 1]]

# 1, 2, 2
# 2, 5, 5
# 6, 7, 1
# Output: [2, 5, 5]
# Explanation:
res = Solution().fallingSquares(positions)
print(res)