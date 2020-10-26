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
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        cost = [float("inf") for _ in range(k)]
        profit = [0 for _ in range(k)]
        for p in prices:
            cost[0] = min(cost[0], p)
            profit[0] = max(profit[0], p - cost[0])
            for idx in range(1, k):
                cost[idx] = min(cost[idx], p-profit[idx-1])
                profit[idx] = max(profit[idx], p-cost[idx])
        return profit[-1]



        # hold, not_hold, not_hold_cooldown = -float("inf"), 0, -float("inf")
        # for p in prices:
        #     hold, not_hold, not_hold_cooldown = max(hold, not_hold-p), max(not_hold, not_hold_cooldown), hold+p
        # return max(not_hold_cooldown, not_hold)
        # length = len(prices)
        # if length <= 1:
        #     return 0
        # dp = [[0 for _ in range(length+1)] for _ in range(2)]
        # dp[1][1] = -prices[0]
        # for day in range(2, length+1):
        #     dp[0][day] = max(dp[0][day-1], dp[1][day-1]+prices[day-1])
        #     dp[1][day] = max(dp[1][day-1], dp[0][day-1]-prices[day-1])??
        # print(dp)
        # return max(dp[1][length], dp[0][length])


prices = [1,2,3,4,5]
res = Solution().maxProfit(prices)
print(res)