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
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_half = []
        self.large_half = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if not self.large_half:
            heapq.heappush(self.large_half, num)
        else:
            if num >= self.large_half[0]:
                heapq.heappush(self.large_half, num)
                if len(self.large_half) - len(self.small_half) == 2:
                    self._move_root(self.large_half, self.small_half)
            else:
                heapq.heappush(self.small_half, -num)
                if len(self.small_half) - len(self.large_half) == 1:
                    self._move_root(self.small_half, self.large_half)
        # while len(self.large_half) - len(self.small_half) > 1:
        #     self._move_root(self.large_half, self.small_half)
        # while len(self.small_half) - len(self.large_half) > -1:
        #     self._move_root(self.small_half, self.large_half)
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            return (self.large_half[0] - self.small_half[0]) / 2
        else:
            return self.large_half[0]

    def _move_root(self, from_heap, to_heap):
        value = heapq.heappop(from_heap)
        heapq.heappush(to_heap, -value)

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())
param_2 = obj.findMedian()