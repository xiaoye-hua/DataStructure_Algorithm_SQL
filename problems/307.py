#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.SegmentTree import SegmentTree


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
    """
    Approach one: Fenwick tree  inspired from huahua leetcode 307
    Approach two: Segment tree   inspired from huahua leetcode segment tree explain
    """

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.segment_tree = SegmentTree(start=0, end=len(nums) - 1, lst=nums)

    def update(self, i: int, val: int) -> None:
        self.segment_tree.update_tree(i, val, self.segment_tree.root)

    def sumRange(self, i: int, j: int) -> int:
        return self.segment_tree.query(begin=i, end=j, root=self.segment_tree.root)

    # approach one:
    # def __init__(self, nums: List[int]):
    #     self.nums = nums
    #     self.tree = FenwickTree(len(nums))
    #     for idx, value in enumerate(nums):
    #         self.tree.update(idx+1, value)
    #
    # def update(self, i: int, val: int) -> None:
    #     self.tree.update(i+1, val-self.nums[i])
    #     self.nums[i] = val
    #
    # def sumRange(self, i: int, j: int) -> int:
    #     return self.tree.query(j+1) - self.tree.query(i)



# nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8

# ["NumArray","update","sumRange","sumRange","update","sumRange"]
# [[[9,-8]],[0,3],[1,1],[0,1],[1,-3],[0,1]]
["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
[[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]

nums = [0,9,5,7,3]
num_array = NumArray(nums)
# print(num_array.sumRange(0, 3))
# print(num_array.update(0, 3))
print(num_array.sumRange(4, 4))
print(num_array.sumRange(2, 4))
print(num_array.sumRange(3, 3))

# print(num_array.update(1, -3))
# print(num_array.sumRange(0, 1))