#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        for idx, g in enumerate(gas):
            c = cost[idx]
            if g>=c:
                previous = g - c
                begin_idx = idx + 1
                while begin_idx%length!=idx and previous>=0:
                    new_idx = begin_idx%length
                    previous = previous + gas[new_idx] - cost[new_idx]
                    begin_idx += 1
                if previous >= 0:
                    return idx
        return -1

# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
gas = [3,3,4]
cost = [3,4,4]
res = Solution().canCompleteCircuit(gas, cost)
print(res)