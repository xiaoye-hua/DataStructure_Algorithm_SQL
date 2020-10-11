#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList
import copy

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.res = []
        self.cache = {}
        self.search(num, target, "")
        return self.res

    def search(self, num, target, out_str):
        if len(num) == 0 and target == 0:
            self.res.append(out_str)
        if int(num) == target:
            self.res.append(num+out_str)
        if len(num) == 1 and int(num) != target:
            return
        new_str = copy.deepcopy(out_str)
        ???

s = "105"
target = 5
res = Solution().addOperators(s, target)
print(res)