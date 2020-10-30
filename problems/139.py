#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList

#
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

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     """
    #     Approch one : dynamic programming: 28ms
    #     :param s:
    #     :param wordDict:
    #     :return:
    #     """
    #     dp = [False for _ in range(len(s))]
    #     for idx in range(len(s)):
    #         # res_lst = []
    #         for word in wordDict:
    #             res = None
    #             length = len(word)
    #             if idx == length-1 and s[:idx+1] == word:
    #                 res = True
    #             elif idx >length-1 and s[idx+1-length:idx+1] == word:
    #                 res = dp[idx-length]
    #             if res:
    #                 dp[idx] = res
    #                 break
    #     # print(dp)
    #     return dp[-1]
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
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         def canBreak(s, m, wordDict):
#             if s in m: return m[s]
#             if s in wordDict:
#                 m[s] = True
#                 return True
#
#             for i in range(1, len(s)):
#                 r = s[i:]
#                 if r in wordDict and canBreak(s[0:i], m, wordDict):
#                     m[s] = True
#                     return True
#
#             m[s] = False
#             return False
#
#         return canBreak(s, {}, set(wordDict))

# s = "dogs"
# wordDict = ["dog","s","gs"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
res = Solution().wordBreak(s, wordDict)
print(res)