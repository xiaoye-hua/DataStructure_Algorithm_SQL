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
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        """
        Approach one:  O(n**2)
        Approach two: O(n)
        :param N:
        :param trust:
        :return:
        """
        self.trust = trust
        # approach two
        begin_user = 1
        end_user = N
        candidate = begin_user
        for i in range(candidate+1, end_user+1):
            if self.check(i, candidate) and not self.check(candidate, i):
                continue
            else:
                candidate = i
        for  j in range(begin_user, candidate):
            if self.check(candidate, j) or not self.check(j, candidate):
                return -1
        return candidate



        # approach one
        # trusting = {key: [] for key in range(1, N+1)}
        # trusted = {key: [] for key in range(1, N+1)}
        # for lst in trust:
        #     u1, u2 = lst
        #     trusting[u1].append(u2)
        #     trusted[u2].append(u1)
        # res = -1
        # for user in range(1, N+1):
        #     if len(trusting[user]) == 0 and len(trusted[user])==N-1:
        #         return user
        # return res

    def check(self, i, j):
        return [i, j] in self.trust



# Input: N = 2, trust = [[1,2]]
# Output: 2
# Example 2:
#
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:
#
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# Example 4:
#
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1

N = 2
trust = [[1,2]]
res = Solution().findJudge(N, trust)
print(res)