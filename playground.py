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

import copy
import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, A):
        mono, res = [], []
        for a in A:
            i = bisect.bisect(mono, a)
            res.append(i + 1)
            if i == len(mono):
                mono.append(0)
            mono[i] = a
        return res


res = Solution().longestObstacleCourseAtEachPosition([3,1,5,6,4,2])
print(res)
