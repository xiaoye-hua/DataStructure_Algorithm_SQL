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
        Approch three : divide and conquer with memory:
        :param s:
        :param wordDict:
        :return:
        """
        self.wordDict = set(wordDict)
        self.mem = {}
        return self.divide_conquer(s)

    def divide_conquer(self, s):
        if s in self.mem:
            return self.mem[s]
        if s in self.wordDict:
            self.mem[s] = True
            return True
            # ans.append(s)
        for idx in range(1, len(s)):
            right = s[idx:]
            if right in self.wordDict and self.divide_conquer(s[:idx]):
                self.mem[s] = True
                return True
            # if self.divide_conquer(s[:idx]):
            #     self.mem[s[:idx]] = True
            #     return True
            # ans += [w + " " + right for w in self.divide_conquer(s[:idx])]
        self.mem[s] = False
        return False

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     """
    #     Approch one : dynamic programming
    #     :param s:
    #     :param wordDict:
    #     :return:
    #     """
    #     if len(s) == 0:
    #         return False
    #     dp = [False for _ in range(len(s))]
    #     for idx in range(len(s)):
    #         # res_lst = []
    #         for word in wordDict:
    #             res = None
    #             length = len(word)
    #             if idx == length-1 and s[:idx+1] == word:
    #                 if len(s) == len(word):
    #                     res = False
    #                 else:
    #                     res = True
    #             elif idx >length-1 and s[idx+1-length:idx+1] == word:
    #                 res = dp[idx-length]
    #             if res:
    #                 dp[idx] = res
    #                 break
    #     return dp[-1]

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
res = Solution().findAllConcatenatedWordsInADict(words)
print(res)