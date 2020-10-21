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
    def alienOrder(self, words: List[str]) -> str:
        """
        Inspired from discussion; https://leetcode.com/problems/alien-dictionary/discuss/208057/Python-solution
        :param words:
        :return:
        """
        self.adjacent_matrix = {}
        construct_True = self.construct_adjacent_matrix(words)
        if not construct_True:
            return ""
        # print(self.adjacent_matrix)
        # 0: unkonw; 1: visting; 2: visited
        self.status = {key: 0 for key in self.adjacent_matrix.keys()}
        self.res = ""
        for node in self.adjacent_matrix:
            if not self.dfs(node):
                return ""
        return self.res

    def construct_adjacent_matrix(self, words):
        length = len(words)
        if length == 0:
            return False
        node_lst = set()
        for string in words:
            node_lst.update(list(string))
        # set([list(string) for string in words])
        for key in node_lst:
            self.adjacent_matrix[key] = set()
        for idx in range(length-1):
            word_idx = 0
            first_word = words[idx]
            second_word = words[idx+1]
            if len(second_word) < len(first_word):
                if first_word[:len(second_word)] == second_word:
                    return False
            while word_idx<len(first_word) and word_idx < len(second_word):
                if first_word[word_idx] != second_word[word_idx]:
                    self.adjacent_matrix[first_word[word_idx]].update(second_word[word_idx])
                    break
                word_idx += 1
        return True

    def dfs(self, node):
        """
        if there is no cycle, return True
        else: return False
        """
        if self.status[node] == 1:
            return False
        if self.status[node] == 2:
            return True
        self.status[node] = 1
        for child in self.adjacent_matrix[node]:
            if not self.dfs(child):
                return False
        self.status[node] = 2
        self.res = node + self.res
        return True


words = ["ab", "abc"]
res = Solution().alienOrder(words)
print(f"[{res}]")