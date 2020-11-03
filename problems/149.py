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
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort()
        slop_map = {}
        times = []
        new_points = []
        for p in points:
            if p in new_points:
                idx = new_points.index(p)
                times[idx] += 1
            else:
                new_points.append(p)
                times.append(1)
        if len(new_points) == 1:
            return times[0]
        for first in range(len(new_points)-1):
            p1 = new_points[first]
            for second in range(first+1, len(new_points)):
                p2 = new_points[second]
                slope= self.get_slope(p1, p2)
                # key = str(slope) + "_" + str(b)
                # if slope
                key = str(first) + "_" + str(slope)
                try:
                    slop_map[key].extend([second]*times[second])
                except:
                    slop_map[key] = [first] * times[first]
                    slop_map[key].extend([second]*times[second])
        # print(slop_map)
        res = 0
        for key, value in slop_map.items():
            if len(value) > res:
                res = len(value)
        return res
        # print(slop_map)

    def get_slope(self, p1, p2):
        import math
        # if p1[0] == p2[0] and p1[1] == p2[1]:
        #     return True, None, None
        denominator = p2[0] - p1[0]
        numerator = p2[1] - p1[1]
        if denominator == 0:
            return "inf"
        elif numerator == 0:
            return "0"
        else:
            num = math.gcd(denominator, numerator)
            return str(numerator/num) + "_" + str(denominator/num)

            # k = round(numerator/denominator, 10)
            # b = round(p2[1] - k*p2[0], 10)
            # k = numerator/denominator
            # b = p2[1] - k*p2[0]
            # return k, b

# new_points = [[560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],[-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],[-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],[-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],[7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],[350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],[-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],[-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],[0,2],[-41,6],[7,19],[30,250]]
# res = []
# for p in points:
#     if p in res:
#         print(p)
#     res.append(p)
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
res = Solution().maxPoints(points)
print(res)