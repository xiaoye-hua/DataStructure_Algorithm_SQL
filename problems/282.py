#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:

    def addOperators(self, num: str, target: int) -> List[str]:
        """
        Inspired from discussion: https://leetcode.com/problems/expression-add-operators/discuss/310707/Clean-Python-DFS-solution
        :param num:
        :param target:
        :return:
        """
        self.length = len(num)
        self.res = []
        self.string = num
        self.target = target
        self.dfs(0, "", 0, None)
        return self.res

    def dfs(self, num_begin_idx, expression, current_sum, last_ele):
        if num_begin_idx>self.length:
            return
        elif num_begin_idx == self.length:
            if current_sum == self.target:
                    # and ("+" in expression or "-" in expression or "*" in expression):
                self.res.append(expression)
        else:
            for num_end_idx in range(num_begin_idx + 1, self.length + 1):
                num_str, num = self.string[num_begin_idx:num_end_idx], int(self.string[num_begin_idx:num_end_idx])
                if not (len(num_str)>1 and num_str[0] == "0"):
                    if last_ele is None:
                        self.dfs(num_end_idx, num_str, num, num)
                    else:
                        self.dfs(num_end_idx, expression+"*"+num_str, current_sum-last_ele+last_ele*num, last_ele*num)
                        self.dfs(num_end_idx, expression+"+"+num_str, current_sum+num, num)
                        self.dfs(num_end_idx, expression + "-" + num_str, current_sum-num, -num)



# num = "123"
# target = 6
num = "00"
target = 0
res = Solution().addOperators(num, target)
print(res)