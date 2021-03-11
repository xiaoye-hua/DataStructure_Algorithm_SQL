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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        if not matrix or not matrix[0]:
            return ans
        n = len(matrix[0])
        heights = [0 for _ in range(n+1)]
        for row in range(len(matrix)):
            for i in range(n):
                if matrix[row][i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            width_begin_idx = [-1]
            for i in range(n+1):
                while heights[i] < heights[width_begin_idx[-1]]:
                    h = heights[width_begin_idx.pop()]
                    w = i - width_begin_idx[-1] -1
                    ans = max(ans, h*w)
                width_begin_idx.append(i)
        return ans
