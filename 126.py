#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        First try: DFS --> ETL
        Second try: BFS --> ETL
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        if beginWord not in wordList:
            wordList.insert(0, beginWord)
        matrix = {key:[] for key in wordList}
        for begin_idx in range(len(wordList)):
            for end_idx in range(begin_idx+1, len(wordList)):
                if self.check_similar(wordList[begin_idx], wordList[end_idx]):
                    matrix[wordList[begin_idx]].append(wordList[end_idx])
                    matrix[wordList[end_idx]].append(wordList[begin_idx])
        # self.matrix = matrix
        # # print(self.matrix)
        # self.res = float("inf")
        # self.target = endWord
        queue = [beginWord]
        depth = 0
        visited = []
        found = False
        res = []
        while len(queue) != 0 and not found:
            depth += 1
            num = len(queue)
            for _ in range(num):
                node = queue.pop(0)
                if node == endWord:
                    found = True
                    return depth
                else:
                    if node not in visited:
                        queue += matrix[node]
                        visited.append(node)
        return res

    #     self.dfs(beginWord, 1, [])
    #     return 0 if self.res==float("inf") else self.res
    #
    # def dfs(self, node, depth, passed):
    #     new_passed = passed.copy()
    #     new_passed.append(node)
    #     for child in self.matrix[node]:
    #         if child not in new_passed:
    #             if child == self.target:
    #                 self.res = min(self.res, depth+1)
    #             else:
    #                 self.dfs(child, depth+1, new_passed)
    #
    def check_similar(self, a, b):
        diff_time = 0
        for idx in range(len(a)):
            if a[idx] != b[idx]:
                diff_time += 1
        # intersection = [ele for ele in a if ele in b]
        return diff_time == 1

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# beginWord = "leet"
# endWord = "code"
# wordList = ["lest","leet","lose","code","lode","robe","lost"]

# Output: 5
res = Solution().ladderLength(beginWord, endWord, wordList)
print(res)