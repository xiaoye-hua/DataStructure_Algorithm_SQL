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
        Approach one: ETL
        :param s:
        :param wordDict:
        :return:
        """
        self.s = s
        self.s_len = len(s)
        self.wordDict = wordDict
        self.res = []
        for word in self.wordDict:
            self.dfs(0, [], word)
        return self.res
        #     if self.dfs(0, word):
        #         return True
        # return False
        # res = [self.dfs(0, word) for word in wordDict]
        # return sum(res) >0

    def dfs(self, begin_idx: int, lst: list, word: str):
        word_len = len(word)
        end_idx = begin_idx+word_len
        if end_idx > self.s_len:
            return
        else:
            if self.s[begin_idx:end_idx] == word:
                new_lst = lst.copy()
                new_lst.append(word)
                if end_idx == self.s_len:
                    self.res.append(" ".join(new_lst))
                    return
                else:
                    for word in self.wordDict:
                        self.dfs(end_idx, new_lst,word)



s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
res = Solution().wordBreak(s, wordDict)
print(res)