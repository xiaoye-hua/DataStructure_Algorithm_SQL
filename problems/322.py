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
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount)]
        dp.insert(0, 0)
        for target_amount in range(1, amount+1):
            for c in coins:
                if target_amount>=c:
                    dp[target_amount] = min(
                        [
                            dp[target_amount]
                            , dp[target_amount-c] + 1
                        ]
                    )

        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]


s = "aaabb"
k = 3
coins = [1, 2, 5]
amount = 11
res = Solution().coinChange(coins, amount)
print(res)