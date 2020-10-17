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
    def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     """
    #     First try: failed:
    #     Second try:
    #     :param points:
    #     :return:
    #     """
        length = len(points)
        if length == 0:
            return 0
        points.sort(key=lambda x: (x[0], x[1]))
        common_start, common_end = points[0]
        res = 1
        for idx in range(1, length):
            start, end = points[idx]
            if common_start < start:
                common_start = start
            if common_end > end:
                common_end = end
            if common_start > common_end:
                res += 1
                common_end = end
                common_start = start
            idx += 1
        return res
    #     length = len(points)
    #     if length == 0:
    #         return 0
    #     points.sort(key=lambda x: (x[0], x[1]))
    #     # print(points)
    #     interval_idx = 0
    #     res = 0
    #     while interval_idx < length:
    #         first_interval = points[interval_idx]
    #         while interval_idx+1<length and points[interval_idx+1][0]<=first_interval[1]:
    #             interval_idx += 1
    #         res += 1
    #         interval_idx += 1
    #     return res






points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
res = Solution().findMinArrowShots(points)
print(res)