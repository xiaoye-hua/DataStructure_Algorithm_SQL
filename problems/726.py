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
    def countOfAtoms(self, formula: str) -> str:
        if not formula:
            return formula
        self.formula = formula
        stack = []
        idx = 0
        while idx < len(formula):
            ele = formula[idx]
            if ele == "(":
                stack.append(ele)
            elif ele == ")":
                current_stack = []
                time, idx= self.get_num(idx+1)
                lst = stack.pop()
                while lst != "(":
                    atom, num = lst
                    lst = stack.pop()
                    current_stack.append(
                        [atom, num*time]
                    )
                stack.extend(current_stack)
            else:
                lst, idx = self.get_lst(idx)
                stack.append(lst)
            idx += 1
        res_dict = {}
        for lst in stack:
            atom, num = lst
            try:
                res_dict[atom] += num
            except:
                res_dict[atom] = num
        res_lst = [[key, value] for key, value in res_dict.items()]
        res_lst.sort()
        res = "".join([str(key)+str(value) if value!=1 else key for key, value in res_lst])
        return res

    def get_num(self, idx):
        res = ""
        while idx< len(self.formula) and self.formula[idx].isdigit():
            res = res + self.formula[idx]
            idx += 1
        try:
            return int(res), idx-1
        except:
            return 1, idx-1

    def get_atom(self, idx):
        res = self.formula[idx]
        idx += 1
        while idx< len(self.formula) and self.formula[idx].islower():
            res += self.formula[idx]
            idx += 1
        return res, idx-1

    def get_lst(self, idx):
        atom, idx = self.get_atom(idx)
        num, idx = self.get_num(idx+1)
        return [atom, num], idx







formula = "H20"
# Output: "K4N2O14S4"

res = Solution().countOfAtoms(formula)
print(res)