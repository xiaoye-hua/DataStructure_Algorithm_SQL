#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        words.sort()
        for word in words:
            # new_words = words.copy()
            # new_words.remove(word)
            if self.wordBreak(word, words):
                res.append(word)
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approch one : dynamic programming
        :param s:
        :param wordDict:
        :return:
        """
        if len(s) == 0:
            return False
        dp = [False for _ in range(len(s))]
        for idx in range(len(s)):
            # res_lst = []
            for word in wordDict:
                res = None
                length = len(word)
                if idx == length-1 and s[:idx+1] == word:
                    if len(s) == len(word):
                        res = False
                    else:
                        res = True
                elif idx >length-1 and s[idx+1-length:idx+1] == word:
                    res = dp[idx-length]
                if res:
                    dp[idx] = res
                    break
        return dp[-1]
# class TestBreakable(object):
#     def __init__(self, wordDict):
#         self.wordDict = wordDict
#         return
#
#     def wordBreak(self, s):
#         table = [False] * (len(s))
#         for j in range(len(s)):
#             for i in range(j, -1, -1):
#                 word_so_far = s[i:j + 1]
#                 left_is_breakable = table[i - 1] if i > 0 else (True and j != len(s) - 1)
#                 if word_so_far in self.wordDict and left_is_breakable:
#                     table[j] = True
#                     break
#         return table[-1]
#
#
# class Solution(object):
#     def findAllConcatenatedWordsInADict(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         words_dict = set(words)
#         test_breakable = TestBreakable(words_dict)
#         results = []
#         for word in words:
#             if word and test_breakable.wordBreak(word):
#                 results.append(word)
#         return results

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
res = Solution().findAllConcatenatedWordsInADict(words)
print(res)