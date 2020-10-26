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


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        self.row = len(matrix)
        self.col = len(matrix[0])
        if self.col == 0:
            return
        total = self.row*self.col
        self.matrix = matrix
        self.tree = FenwickTree(total)
        for row_idx in range(self.row):
            for col_idx in range(self.col):
                num = self.get_num(row_idx, col_idx)
                self.tree.update(num+1, self.matrix[row_idx][col_idx])

    def get_num(self, row_idx, col_idx):
        return row_idx * self.col + col_idx

    def update(self, row: int, col: int, val: int) -> None:
        num = self.get_num(row, col)
        self.tree.update(num+1, val-self.matrix[row][col])
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        # for col_idx in range(col1, col2+1):
        for row_idx in range(row1, row2+1):
            num1 = self.get_num(row_idx, col1)
            num2 = self.get_num(row_idx, col2)
            # print(num2)
            sum_value = self.tree.query(num2+1) - self.tree.query(num1)
            res += sum_value
        return res




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
# matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
matrix = [[[]]]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10


# ["NumMatrix","sumRegion","update","sumRegion"]
matrix = [[1]]
# ["NumMatrix","sumRegion","sumRegion","sumRegion","update","update","sumRegion"]
matrix = [[1],[2]]
 # [0,0,0,0],[1,0,1,0],[0,0,1,0],[0,0,3],[1,0,5],[0,0,1,0]]
 # [0,0,0,0],[0,0,-1],[0,0,0,0]]
num_matrix = NumMatrix(matrix)
# print(num_matrix.sumRegion(0, 0, 0, 0))
print(num_matrix.sumRegion(1, 0, 1, 0))

# num_matrix.update(0, 0, -1)
# print(num_matrix.sumRegion(0, 0, 0, 0))
