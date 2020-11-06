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
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        stats = {}
        for w in words:
            try:
                stats[w] += 1
            except:
                stats[w] = 1
        res = []
        for lst in sorted(stats.items(), key=lambda x: [-x[1], x[0]])[:k]:
            # print(lst)
            res.append(lst[0])
        return res

# ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 1
res = Solution().topKFrequent(words, k)
print(res)