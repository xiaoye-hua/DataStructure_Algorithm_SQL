#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        First try: dynamic programmin --> ETL
        Second try: inspired from problem 53 --> failed
        Third try: change code of problem 53
        :param nums:
        :return:
        """
        dp = [1 for _ in range(len(nums)+1)]
        dp_min = [1 for _ in range(len(nums)+1)]
        res = -float("inf")
        for idx in range(1, len(nums)+1):
            dp[idx] = max(nums[idx-1], nums[idx-1]*dp[idx-1], nums[idx-1]*dp_min[idx-1])
            dp_min[idx] = min(nums[idx-1], nums[idx-1]*dp_min[idx-1], nums[idx-1]*dp[idx-1])
            res = max(res, dp[idx])
        # print(dp)
        # print(dp_min)
        return res

        # dp = [[0]*len(nums) for _ in range(len(nums))]
        # for idx in range(len(nums)):
        #     dp[idx][idx] =  nums[idx]
        # for begin_idx in range(len(nums)):
        #     for end_idx in range(begin_idx+1, len(nums)):
        #         dp[begin_idx][end_idx] = dp[begin_idx][end_idx-1] * dp[end_idx][end_idx]
        # # print(dp)
        # return max([max(lst) for lst in dp])

# nums = [-2, 3, -4]
nums = [2,3,-2,4]
res = Solution().maxProduct(nums)
print(res)