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

import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.larger_part = []
        self.smaller_part = []

    def addNum(self, num: int) -> None:
        larger_len = len(self.larger_part)
        smaller_len = len(self.smaller_part)
        if len(self.larger_part) == len(self.smaller_part):
            if len(self.smaller_part) == 0:
                heapq.heappush(self.larger_part, num)
            else:
                if num <= -self.smaller_part[0]:
                    heapq.heappush(self.smaller_part, -num)
                else:
                    heapq.heappush(self.larger_part, num)
        elif larger_len > smaller_len:
            if num >= self.larger_part[0]:
                item = heapq.heappushpop(self.larger_part, num)
                heapq.heappush(self.smaller_part, -item)
            else:
                heapq.heappush(self.smaller_part, -num)
        else:
            if num <= -self.smaller_part[0]:
                item = heapq.heappushpop(self.smaller_part, -num)
                heapq.heappush(self.larger_part, -item)
            else:
                heapq.heappush(self.larger_part, num)

    def findMedian(self) -> float:
        # print(self.larger_part)
        # print(self.smaller_part)
        if len(self.larger_part) == len(self.smaller_part):
            return (self.larger_part[0] - self.smaller_part[0]) / 2
        elif len(self.larger_part) > len(self.smaller_part):
            return self.larger_part[0]
        else:
            return -self.smaller_part[0]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median_finder = MedianFinder()
        for lst in [nums1, nums2]:
            for value in lst:
                median_finder.addNum(value)
        return median_finder.findMedian()


nums1 = [1,2]
nums2 = [3,4]
res = Solution().findMedianSortedArrays(nums1, nums2)
print(res)