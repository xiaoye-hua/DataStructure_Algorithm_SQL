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


# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        First try: inspired from 997, ETL
        Second try; inspired from https://leetcode.com/problems/find-the-celebrity/discuss/240736/Python-solution
        :param n:
        :return:
        """
        # trust = []
        # for u1 in range(n-1):
        #     for u2 in range(u1+1, n):
        #         if knows(u1, u2):
        #             trust.append(
        #                 [u1+1, u2+1]
        #             )
        #         if knows(u2, u1):
        #             trust.append(
        #                 [u2+1, u1+1]
        #             )
        # # print(trust)
        # N = n
        # trusting = {key: [] for key in range(1, N+1)}
        # trusted = {key: [] for key in range(1, N+1)}
        # for lst in trust:
        #     u1, u2 = lst
        #     trusting[u1].append(u2)
        #     trusted[u2].append(u1)
        # res = -1
        # for user in range(1, N+1):
        #     if len(trusting[user]) == 0 and len(trusted[user])==N-1:
        #         return user-1
        # return res
        # approach two
        begin_user = 0
        end_user = n-1
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
        return knows(i, j)



# [[1,1,0],[0,1,0],[1,1,1]]