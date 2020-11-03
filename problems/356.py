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


import math
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        length = len(points)
        if length in [0, 1]:
            return True
        new_points = []
        for p in points:
            if p not in new_points:
                new_points.append(p)
        points = new_points
        length = len(points)
        points.sort(key=lambda x: x[0])
        begin = 0
        end = length - 1
        mid = (begin+end) // 2+1
        last_half = points[mid:]
        last_half.sort(key=lambda x:[x[0], -x[1]])
        points[mid:] = last_half[:]
        mid_x = self.get_mid_x(points[begin][0]+points[end][0], 2)
        while end - begin>=1:
            p1 = points[begin]
            p2 = points[end]
            if self.x2str(p1[0])!=mid_x or self.x2str(p2[0])!=mid_x:
                current_midx_x = self.get_mid_x(p1[0]+p2[0], 2)
                if current_midx_x != mid_x or p1[1] != p2[1]:
                    return False
            begin += 1
            end -= 1
        if begin == end:
            x, y = points[begin]
            current_midx_x = self.x2str(x)
            if  current_midx_x != mid_x:
                return False
        return True

    def x2str(self, x):
        denominator = 1
        while x != int(x):
            x *= 10
            denominator *= 10
        current_midx_x = self.get_mid_x(x, denominator)
        return current_midx_x

    def get_mid_x(self, numerator, denominator):
        total = int(numerator)
        sign = "" if total>=0 else "-"
        total = abs(total)
        common_d = math.gcd(total, denominator)
        mid_x = sign +  str(total / common_d) + "_" + str(denominator/ common_d)
        return mid_x






points = [[0,0],[0,-1]]
res = Solution().isReflected(points)
print(res)