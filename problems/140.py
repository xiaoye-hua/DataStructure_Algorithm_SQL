#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Approach one: DFS without memory -> ETL
        Approach two: Divide and conquer with memory inspired from huahua tech road: https://zxi.mytechroad.com/blog/leetcode/leetcode-140-word-break-ii/
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
        ans = []
        if s in self.wordDict:
            ans.append(s)
        for idx in range(1, len(s)):
            right = s[idx:]
            if right not in self.wordDict:
                continue
            ans += [w + " " + right for w in self.divide_conquer(s[:idx])]
        self.mem[s] = ans
        return ans
    #     self.s = s
    #     self.s_len = len(s)
    #     self.wordDict = wordDict
    #     self.res = []
    #     for word in self.wordDict:
    #         self.dfs(0, [], word)
    #     return self.res
    #     #     if self.dfs(0, word):
    #     #         return True
    #     # return False
    #     # res = [self.dfs(0, word) for word in wordDict]
    #     # return sum(res) >0
    #
    # def dfs(self, begin_idx: int, lst: list, word: str):
    #     word_len = len(word)
    #     end_idx = begin_idx+word_len
    #     if end_idx > self.s_len:
    #         return
    #     else:
    #         if self.s[begin_idx:end_idx] == word:
    #             new_lst = lst.copy()
    #             new_lst.append(word)
    #             if end_idx == self.s_len:
    #                 self.res.append(" ".join(new_lst))
    #                 return
    #             else:
    #                 for word in self.wordDict:
    #                     self.dfs(end_idx, new_lst,word)



s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
res = Solution().wordBreak(s, wordDict)
print(res)