#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List
import collections

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        First try: BFS --> don't know how to store the path
        Second try: BFS+DFS --> BFS for the length; DFS for all sequence  --> ETL
        Third try: BFS: inspried from https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
                    Explaination: layer:{endword: BFS path to endwords}
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        wordList = set(wordList)
        layer = {}
        layer[beginWord] = [[beginWord]]
        res = []
        while layer:
            new_layer = {}
            for w in layer:
                if w == endWord:
                    res.extend(layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                try:
                                    new_layer[neww] += [lst + [neww] for lst in layer[w]]
                                except:
                                    new_layer[neww] = [lst + [neww] for lst in layer[w]]
            wordList -= set(new_layer.keys())
            layer = new_layer
            # print(layer)

        return res
#         if beginWord not in wordList:
#             wordList.insert(0, beginWord)
#         matrix = {key:[] for key in wordList}
#         for begin_idx in range(len(wordList)):
#             for end_idx in range(begin_idx+1, len(wordList)):
#                 if self.check_similar(wordList[begin_idx], wordList[end_idx]):
#                     matrix[wordList[begin_idx]].append(wordList[end_idx])
#                     matrix[wordList[end_idx]].append(wordList[begin_idx])
#
#         self.matrix = matrix
#         self.res = []
#         self.target = endWord
#         self.length = self.bfs(beginWord, endWord, wordList)
#         # return self.length
#         if self.length == 0:
#             return self.res
#         else:
#             self.dfs(beginWord, 1, [], [])
#             return self.res
#
#     def bfs(self, beginWord, endWord, wordList):
#         import collections
#         import string
#         # wordList.add(endWord)
#
#         wordList = set(wordList)
#         queue = collections.deque([[beginWord, 1]])
#         while queue:
#             word, length = queue.popleft()
#             if word == endWord:
#                 return length
#             for i in range(len(word)):
#                 for c in 'abcdefghijklmnopqrstuvwxyz':
#                     next_word = word[:i] + c + word[i + 1:]
#                     if next_word in wordList:
#                         wordList.remove(next_word)
#                         queue.append([next_word, length + 1])
#         return 0
#
#     def dfs(self, node, depth, passed, path):
#         new_passed = passed.copy()
#         new_passed.append(node)
#         new_path = path.copy()
#         new_path.append(node)
#         if depth > self.length:
#             return
#         elif depth == self.length:
#             if node == self.target:
#                 self.res.append(new_path)
#         else:
#             for child in self.matrix[node]:
#                 if child not in new_passed:
#                     self.dfs(child, depth+1, new_passed, new_path)
#     #
#     def check_similar(self, a, b):
#         diff_time = 0
#         for idx in range(len(a)):
#             if a[idx] != b[idx]:
#                 diff_time += 1
#         # intersection = [ele for ele in a if ele in b]
#         return diff_time == 1



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# beginWord = "leet"
# endWord = "code"
# wordList = ["lest","leet","lose","code","lode","robe","lost"]

# Output: 5
res = Solution().findLadders(beginWord, endWord, wordList)
print(res)