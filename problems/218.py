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

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Approach one: inspired from huahua leetcode youtube
            first try: ETL
            second try : Inspired from https://leetcode.com/problems/the-skyline-problem/discuss/593234/Python-3-Heap
            third try: failed
        :param buildings:
        :return:
        """

        lst = []
        enter = []
        leave = []
        for b in buildings:
            enter.append([b[0], b[2], 0])
            leave.append([b[1], b[2], 1])
        enter.sort(key=lambda x: [x[0], x[2], -x[1]])
        leave.sort(key=lambda x: [x[0], x[2], x[1]])
        while len(enter) > 0 and len(leave)>0:
            if enter[0][0]<=leave[0][0]:
                lst.append(
                    enter.pop(0)
                )
            else:
                lst.append(
                    leave.pop(0)
                )
        while len(leave) != 0:
            lst.append(
                leave.pop(0)
            )
        while len(enter) != 0:
            lst.append(
                enter.pop(0)
            )

        max_heap = [0]
        res = []
        # lst = [[1, 3, 0], [1, 2, 0], [1, 1, 0], [2, 1, 1], [2, 2, 1], [2, 3, 1]]
        for value in lst:
            if value[-1] == 0:
                if value[1] > -max_heap[0]:
                    res.append(
                        [value[0], value[1]]
                    )
                heapq.heappush(max_heap, -value[1])
            else:
                self.remove_by_key(max_heap, value[1])
                # self.tombstones = {}
                # self.heap_remove(max_heap, value[1])
                if value[1]>-max_heap[0]:
                    res.append(
                        [value[0], -max_heap[0]]
                    )
        return res

    def remove_by_key(self, heap, key):
        # first try:
        # lst = []
        # max_height = -heapq.heappop(heap)
        # while max_height != key:
        #     lst.append(max_height)
        #     max_height = -heapq.heappop(heap)
        # for height in lst:
        #     heapq.heappush(heap, -height)

        # second try:
        heap.remove(-key)
        heapq.heapify(heap)

    # def heap_remove(self, heap, value):
    #     self.tombstones[value] = self.tombstones.get(value, 0) + 1
    #     while len(heap) and heap[0] in self.tombstones and self.tombstones[heap[0]]:
    #         self.tombstones[heap[0]] -= 1
    #         heapq.heappop(heap)



building = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

res = Solution().getSkyline(building)
print(res)
#
# Input
# [[1,2,1],[1,2,2],[1,2,3]]
# Output
# [[1,1],[1,2],[1,3],[2,0]]
# Expected
# [[1,3],[2,0]]