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
    def evaluate(self, expression: str) -> int:
        self.func_map = {
            "(mult" : self.mult,
            "(add": self.add,
            "(let": self.let
        }
        expre_lst = expression.split(" ")
        return self.evaluate_part(expre_lst)

    def evaluate_part(self, expre_lst, var_map={}):
        func = self.func_map[expre_lst[0]]
        if expre_lst[-1][-1] == ")":
            expre_lst[-1] = expre_lst[-1][:-1]
        lst = self.parse_single_part(expre_lst[1:])
        # if expre_lst[0] == "(let":
        # return func(lst)
        return func(lst, var_map)

    def mult(self, lst, var_map={}):
        if len(lst[0]) != 1:
            lst[0] = [self.evaluate_part(lst[0], var_map=var_map)]
        if len(lst[1]) != 1:
            lst[1] = [self.evaluate_part(lst[1], var_map=var_map)]
        return int(var_map.get(lst[0][0], lst[0][0])) * int(var_map.get(lst[1][0], lst[1][0]))

    def add(self, lst, var_map={}):
        if len(lst[0]) != 1:
            lst[0] = [self.evaluate_part(lst[0], var_map=var_map)]
        if len(lst[1]) != 1:
            lst[1] = [self.evaluate_part(lst[1], var_map=var_map)]
        return int(var_map.get(lst[0][0], lst[0][0])) + int(var_map.get(lst[1][0], lst[1][0]))

    def let(self, lst, var_map={}):
        # print(lst)
        import copy
        var_map =  copy.deepcopy(var_map)
        length = (len(lst) -1)//2
        for idx in range(length):
            if len(lst[idx*2+1]) != 1:
                lst[idx*2+1] = [self.evaluate_part(lst[idx*2+1], var_map=var_map)]
            var_map[lst[idx*2][0]] = var_map.get(lst[idx*2+1][0], lst[idx*2+1][0])
        # print(lst[-1])
        if len(lst[-1]) == 1:
            return int(var_map.get(lst[-1][0], lst[-1][0]))
        else:
            return self.evaluate_part(lst[-1], var_map=var_map)

    def parse_single_part(self, lst):
        res = []
        single_part = []
        mark_num = 0
        for ele in lst:
            for char in ele:
                if char == "(":
                    mark_num += 1
                if char == ")":
                    mark_num -= 1
            single_part.append(ele)
            if mark_num == 0:
                res.append(single_part)
                single_part = []
        return res




# expr = "(mult 3 (add 2 3))"
# # Output: 15
# expr = "(add 2 3)"
# expr = "(let a1 3 b2 (add a1 1) b2)"
# expr = "(let x 2 (add (let x 3 (let x 4 x)) x))"
# expr = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
# expr = "(let a -122 b 0 (add (add 1 -4) (mult a 66)))"
expr = "(let var 78 b 77 (let c 33 (add c (mult var 66))))"
res = Solution().evaluate(expr)
print(res)

# print(Solution().parse_single_part(["3", "(add", "2", "3)"]))