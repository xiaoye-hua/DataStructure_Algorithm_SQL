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
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        import heapq
        courses.sort(key=lambda x: x[1])
        # print(courses)
        total_time = 0
        max_heap = []
        for info in courses:
            duration, end_time = info
            total_time += duration
            heapq.heappush(max_heap, -duration)
            while total_time>end_time:
                max_duration = -heapq.heappop(max_heap)
                total_time -= max_duration
        return len(max_heap)



courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
res = Solution().scheduleCourse(courses)
print(res)