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

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
res = Solution().findAllConcatenatedWordsInADict(words)
print(res)