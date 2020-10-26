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


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.target = n
        self.row = {row: [0, 0] for row in range(self.target)}
        self.col = {col: [0, 0] for col in range(self.target)}
        self.diagonal = {1: [0, 0], -1: [0, 0]}
        self.board = [[0 for _ in range(self.target)] for _ in range(self.target)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if self.board[row][col] != 0:
            return
        else:
            self.board[row][col] = player
        # print(self.board)
        self.row[row][player - 1] += 1
        self.col[col][player - 1] += 1
        if row == col:
            self.diagonal[1][player - 1] += 1
        if self.target - 1 - row == col or self.target - 1 - col == row:
            self.diagonal[-1][player - 1] += 1
        # print(self.diagonal)
        for value in [self.row[row][player - 1], self.col[col][player - 1], self.diagonal[1][player - 1],
                      self.diagonal[-1][player - 1]]:
            if value == self.target:
                return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)