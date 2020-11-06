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
    def partitionLabels(self, S: str) -> List[int]:
        if len(S) == 0:
            return []
        self.ele_range = {}
        for idx, ele in enumerate(S):
            self.ele_range[ele] = idx
        self.res = []
        self.partition(S, 0)
        return self.res

    def partition(self, s, idx):
        if len(s)-1 < idx:
            return
        max_idx = self.ele_range[s[idx]]
        new_idx = idx
        while new_idx != max_idx:
            new_idx += 1
            if self.ele_range[s[new_idx]] > max_idx:
                max_idx = self.ele_range[s[new_idx]]
        self.res.append(new_idx-idx+1)
        self.partition(s, new_idx+1)



# Input: \
S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
res = Solution().partitionLabels(S)
print(res)