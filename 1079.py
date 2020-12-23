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
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Inspired from 46
        :param tiles:
        :return:
        """
        self.res = set()
        for length in range(1, len(tiles)+1):
            self.backtrack(current_str="", remain_tiles=list(tiles), length_left=length)
        # print(self.res)
        # print(len(set(self.res)))
        return len(self.res)

    def backtrack(self, current_str, remain_tiles, length_left):
        if length_left == 0:
            # print(self.res)
            # print(current_str)
            self.res.add(current_str)
        else:
            length_left -= 1
            for tile in remain_tiles:
                new_remain = remain_tiles.copy()
                new_remain.remove(tile)
                self.backtrack(current_str+tile, new_remain, length_left)






# Example 1:
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:
#
# Input: tiles = "AAABBC"
# Output: 188
# Example 3:
#
# Input: tiles = "V"
# Output: 1

tiles = "AAB"
res = Solution().numTilePossibilities(tiles)
print(res)