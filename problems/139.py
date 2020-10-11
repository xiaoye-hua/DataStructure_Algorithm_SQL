#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     """
    #     Approach two: DFS -->  ETL
    #     :param s:
    #     :param wordDict:
    #     :return:
    #     """
    #     self.s = s
    #     self.s_len = len(s)
    #     self.wordDict = wordDict
    #     for word in self.wordDict:
    #         if self.dfs(0, word):
    #             return True
    #     return False
    #     # res = [self.dfs(0, word) for word in wordDict]
    #     # return sum(res) >0
    #
    # def dfs(self, begin_idx: int, word: str) -> bool:
    #     word_len = len(word)
    #     end_idx = begin_idx+word_len
    #     if end_idx > self.s_len:
    #         return False
    #     else:
    #         if self.s[begin_idx:end_idx] == word:
    #             if end_idx == self.s_len:
    #                 return True
    #             else:
    #                 for word in self.wordDict:
    #                     if self.dfs(end_idx, word):
    #                         return True
    #                 return False
    #         else:
    #             return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approch one : dynamic programming
        :param s:
        :param wordDict:
        :return:
        """
        dp = [False for _ in range(len(s))]
        for idx in range(len(s)):
            # res_lst = []
            for word in wordDict:
                res = None
                length = len(word)
                if idx == length-1 and s[:idx+1] == word:
                    res = True
                elif idx >length-1 and s[idx+1-length:idx+1] == word:
                    res = dp[idx-length]
                if res:
                    dp[idx] = res
                    break
        # print(dp)
        return dp[-1]


s = "dogs"
wordDict = ["dog","s","gs"]
res = Solution().wordBreak(s, wordDict)
print(res)