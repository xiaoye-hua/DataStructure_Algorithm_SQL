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
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        import copy
        self.board_copy = copy.deepcopy(board)
        self.row_num = len(board)
        self.col_num = len(board[0])
        for row in range(self.row_num):
            for col in range(self.col_num):
                self.update(row, col, board)

    def update(self, row, col, board):
        res = []
        if row > 0:
            res.append(self.board_copy[row-1][col])
            if col > 0:
                res.append(self.board_copy[row-1][col-1])
        if row < self.row_num-1:
            res.append(self.board_copy[row+1][col])
            if col < self.col_num-1:
                res.append(self.board_copy[row+1][col+1])
        if col > 0:
            res.append(self.board_copy[row][col-1])
            if row < self.row_num-1:
                res.append(self.board_copy[row+1][col-1])
        if col < self.col_num-1:
            res.append(self.board_copy[row][col+1])
            if row > 0:
                res.append(self.board_copy[row-1][col+1])
        sum_num = sum(res)
        if self.board_copy[row][col] == 0:
            if sum_num == 3:
                board[row][col] = 1
        else:
            if sum_num > 3:
                board[row][col] = 0
            elif sum_num < 2:
                board[row][col] = 0



board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
res = Solution().gameOfLife(board)
print(board)