#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


import copy
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        first try: copy from word search I: ETL
        :param board:
        :param words:
        :return:
        """
        self.res = set()
        self.row_num = len(board)
        self.col_num = len(board[0])
        self.board = board
        self.words = words
        # if len(word) > self.row_num * self.col_num:
        #     return False
        for row in range(self.row_num):
            for col in range(self.col_num):
                self.backtrack(row, col, idx=0, words=self.words, passed=[])
        return list(self.res)

    def backtrack(self, x, y, idx, words, passed=[]):
        if len(words) == 0:
            return
        if [x, y] in passed:
            return
        new_words = []
        # print(words)
        for word in words:
            if len(word)>idx and self.board[x][y] == word[idx]:
                if len(word) == idx + 1:
                    if word not in self.res:
                        self.res.update([word])
                        self.words.remove(word)
                    # try:
                else:
                    new_words.append(word)

        passed.append([x, y])
        self.backtrack(max(x - 1, 0), y, idx+1, new_words, passed.copy())
        self.backtrack(min(x + 1, self.row_num - 1), y, idx+1, new_words, passed.copy())
        self.backtrack(x, max(y - 1, 0), idx+1, new_words, passed.copy())
        self.backtrack(x, min(y + 1, self.col_num - 1), idx+1, new_words, passed.copy())

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
res = Solution().findWords(board, words)
print(res)