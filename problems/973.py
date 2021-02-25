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

from src.MinHeap import MinHeap


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        approach 1:  heapq module
        approach 2:  MinHeap
        """
        # import heapq
        # # distances = [self.get_distance(lst) for lst in points]
        # max_heap  = []
        # for lst in points:
        #     dis = self.get_distance(lst)
        #     if len(max_heap) == K:
        #         if dis < -max_heap[0][0]:
        #             heapq.heappop(max_heap)
        #             heapq.heappush(max_heap, [-dis, lst])
        #     else:
        #         heapq.heappush(max_heap, [-dis, lst])
        # return [value[1] for value in max_heap]


        # max_heap  = []
        max_heap = MinHeap(list_input=True)
        for lst in points:
            dis = self.get_distance(lst)
            if max_heap.size == K:
                if dis < -max_heap.lst[1][0]:
                    max_heap.pop()
                    max_heap.push([-dis, lst])
            else:
                max_heap.push([-dis, lst])
        return [value[1] for value in max_heap.lst[1:]]

    def get_distance(self, lst):
        import math
        x, y = lst
        return math.sqrt(x**2 + y**2)



# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)

points = [[3,3],[5,-1],[-2,4]]
K = 2
res = Solution().kClosest(
    points, K
)
print(res)