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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        grid = board
        self.mark = "mart"
        count = 0
        if grid is None or grid == [[]] or grid == []:
            return count
        self.grid = grid
        self.y_dim = len(grid)
        self.x_dim = len(grid[0])
        self.change_edge("O", self.mark)
        for y in range(1, self.y_dim-1):
            for x in range(1, self.x_dim-1):
                # print(self.grid[y][x])
                if self.grid[y][x] == "O":
                    count += 1
                    # print(count)
                    # self.dfs(y, x)
                    self.dfs(y, x, "O", "X")
        self.change_edge(self.mark, "O")
        # return count

    def change_edge(self, origin_mark, target_mark):
        for y in range(self.y_dim):
            if self.grid[y][0] == origin_mark:
                self.dfs(y, 0, origin_mark, target_mark)
            if self.grid[y][self.x_dim-1] == origin_mark:
                self.dfs(y, self.x_dim - 1, origin_mark, target_mark)
        for x in range(self.x_dim):
            if self.grid[0][x] == origin_mark:
                self.dfs(0, x, origin_mark, target_mark)
            if self.grid[self.y_dim-1][x] == origin_mark:
                self.dfs(self.y_dim - 1, x, origin_mark, target_mark)

    def dfs(self, y, x, origin_mark, target_mark):
        if x < 0 or x >= self.x_dim or y < 0 or y >= self.y_dim or self.grid[y][x] != origin_mark:
            return
        self.grid[y][x] = target_mark
        self.dfs(y - 1, x, origin_mark, target_mark)
        self.dfs(y + 1, x, origin_mark, target_mark)
        self.dfs(y, x + 1, origin_mark, target_mark)
        self.dfs(y, x - 1, origin_mark, target_mark)

    # def dfs(self, y, x):
    #     if x < 0 or x >= self.x_dim or y < 0 or y >= self.y_dim or self.grid[y][x] == "X":
    #         return
    #     self.grid[y][x] = "X"
    #     self.dfs(y - 1, x)
    #     self.dfs(y + 1, x)
    #     self.dfs(y, x + 1)
    #     self.dfs(y, x - 1)

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
res = Solution().solve(board)
for lst in board:
    print(lst)
# print(res)