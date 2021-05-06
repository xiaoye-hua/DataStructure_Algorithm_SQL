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
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (days[-1] + 1)
        dp[0] = 0
        for day in range(1, days[-1] + 1):
            if day not in days:
                dp[day] = dp[day - 1]
            else:
                for day_range, cost in zip([1, 7, 30], costs):
                    # if day >= day_range:
                    dp[day] = min(dp[day], dp[max(day - day_range, 0)] + cost)
        # print(dp)
        return dp[day]
