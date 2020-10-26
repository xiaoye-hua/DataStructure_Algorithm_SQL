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


class FenwickTree:
    def __init__(self, n):
        self._sums = [0 for _ in range(n + 1)]

    def update(self, i, delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & -i
        return s

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = FenwickTree(len(nums))
        for idx, value in enumerate(nums):
            self.tree.update(idx+1, value)

    def update(self, i: int, val: int) -> None:
        self.tree.update(i+1, val-self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.query(j+1) - self.tree.query(i)





# class NumArray:
#
#     def __init__(self, nums):
#         self._nums = nums
#         self._tree = FenwickTree(len(nums))
#         for i in range(len(nums)):
#             self._tree.update(i + 1, nums[i])
#
#     def update(self, i, val):
#         self._tree.update(i + 1, val - self._nums[i])
#         self._nums[i] = val
#
#     def sumRange(self, i, j):
#         return self._tree.query(j + 1) - self._tree.query(i)



nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8

num_array = NumArray(nums)
print(num_array.sumRange(0, 2))
num_array.update(1, 2)
print(num_array.sumRange(0, 2))