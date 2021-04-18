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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        str_len = len(s)
        word_num = len(wordDict)
        dp = [False] * str_len
        dp.insert(0, True)
        for idx, string in enumerate(s):
            word_idx = 0
            cur_idx = idx + 1
            while not dp[cur_idx] and word_idx<word_num:
                ele = wordDict[word_idx]
                word_len = len(ele)
                if cur_idx >= word_len and s[cur_idx-word_len: cur_idx] == ele:
                    dp[cur_idx] = dp[cur_idx-word_len]
                word_idx += 1
        return dp[-1]


s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

res = Solution().wordBreak(s, wordDict)
print(res)
