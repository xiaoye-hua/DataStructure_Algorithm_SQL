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
    def consecutiveNumbersSum(self, N: int) -> int:
        """
        First try: dynamic programing: ETL  failed
        Second try: math problem: k>=0 & 1<=i<=N
        :param N:
        :return:
        """
        k_lst = set()
        for i in range(1, N+1):
            subtract = N - i*(i-1)/2
            if int(subtract) != subtract or subtract<0:
                return len(k_lst)
            quotient = subtract/i
            if int(quotient) == quotient and quotient>0:
                k_lst.add(quotient)
                # print("*"*20)
                # print(quotient)
                # print(i)
        return len(k_lst)
        # res = 1
        # dp = [[0 for _ in range(N)] for _ in range(N)]
        # for idx in range(N):
        #     dp[idx][idx] = idx+1
        # for row in range(N):
        #     for col in range(row+1, N):
        #         dp[row][col] = dp[row][col-1] + dp[col][col]
        #         if dp[row][col] == N:
        #             res += 1
        # # print(dp)
        # return res

N = 5809342
res = Solution().consecutiveNumbersSum(N)
print(res)