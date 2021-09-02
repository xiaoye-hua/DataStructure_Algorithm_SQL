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


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        dp[i][j] number of int need when the target is j and considering the ith int
        """
        if sum(nums) / 2 != sum(nums) // 2:
            return False
        amount = int(sum(nums) / 2)
        dp = [[-float('inf') for _ in range(amount + 1)] for _ in range(len(nums) + 1)]
        for idx in range(len(nums) + 1):
            dp[idx][0] = 0
        for coin_idx in range(1, len(nums) + 1):
            for a in range(1, amount + 1):
                for c in nums[:coin_idx]:
                    if c <= a:
                        dp[coin_idx][a] = max(dp[coin_idx][a], dp[coin_idx - 1][a - c] + 1)
            print("*" * 8)
            print(dp)
        # print(dp)
        res = max([dp[idx][amount] for idx in range(len(nums) + 1)])
        if res == -float("inf"):
            return False
        else:
            return True


nums = [1,5,11,5]

res = Solution().canPartition(nums=nums)

print(res)