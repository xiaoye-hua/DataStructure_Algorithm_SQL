#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for ele in tokens:
            if ele not in operators:
                stack.append(int(ele))
            else:
                second_ele = stack.pop(-1)
                first_ele = stack.pop(-1)
                if ele == "+":
                    new_ele = first_ele + second_ele
                elif ele == "-":
                    new_ele = first_ele - second_ele
                elif ele == "*":
                    new_ele = first_ele * second_ele
                else:

                    new_ele = abs(first_ele) // abs(second_ele)
                    if first_ele * second_ele<0:
                        new_ele = -new_ele
                stack.append(new_ele)
            # print(ele)
            # print(stack)
            # print()
        return stack[0]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
res = Solution().evalRPN(tokens)
print(res)