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
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        schedule = [[intervals[0]]]
        for idx in range(1, len(intervals)):
            current = intervals[idx]
            found_room = False
            room_idx = 0
            while room_idx<len(schedule) and not found_room:
            # for room_idx in range(len(schedule)):
                room_schedule = schedule[room_idx]
                if current[0]>=room_schedule[-1][1]:
                    schedule[room_idx].append(current)
                    found_room = True
                room_idx += 1
            if not found_room:
                schedule.append([current])
        return len(schedule)


        # print(intervals)

intervals = [[0, 30],[5, 10],[15, 20]]
res = Solution().minMeetingRooms(intervals)
print(res)