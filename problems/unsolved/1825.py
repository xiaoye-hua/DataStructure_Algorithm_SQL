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

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m_list = []
        self.m_len = 0
        self.k = k
        self.m = m
        self.largest = []
        self.smallest = []
        self.num_idx = m
        self.remove_dict = {}

    def addElement(self, num: int) -> None:
        if self.m_len != self.m:
            self.m_len += 1
            if self.m_len == self.m:
                for idx, ele in enumerate(self.m_list):
                    heapq.heappush(self.largest, [ele, idx])
                    heapq.heappush(self.smallest, [-ele, idx])
                    if len(self.largest) > self.k:
                        heapq.heappop(self.largest)
                    if len(self.smallest) > self.k:
                        heapq.heappop(self.smallest)
        else:
            while self.largest[0][1] in self.remove_dict.keys():
                index = self.largest[0][1]
                heapq.heappop(self.largest)
                del self.remove_dict[index]
            while self.smallest[0][1] in self.remove_dict.keys():
                index = self.smallest[0][1]
                heapq.heappop(self.smallest)
                del self.remove_dict[index]
            value = self.m_list.pop(0)
            idx = self.num_idx
            self.remove_dict[idx] = value
            self.num_idx += 1
            if num >= self.

        self.m_list.append(num)

    def calculateMKAverage(self) -> int:
        if self.m_len < self.m:
            return -1
        else:
            for ele in self.m_list:
                heapq.heappush(self.largest, -ele)
                heapq.heappush(self.smallest, ele)
                if len(self.largest) > self.k:
                    heapq.heappop(self.largest)
                if len(self.smallest) > self.k:
                    heapq.heappop(self.smallest)
            return int((sum(self.m_list) + sum(self.largest) - sum(self.smallest)) / (self.m - 2 * self.k))


# ["MKAverage","addElement","addElement","calculateMKAverage","addElement","calculateMKAverage","addElement","addElement","addElement","calculateMKAverage"]
# [[3,1],[3],[1],[],[10],[],[5],[5],[5],[]]
obj = MKAverage(3, 1)
obj.addElement(3)
obj.addElement(1)
print(obj.calculateMKAverage())
obj.addElement(10)
print(obj.calculateMKAverage())