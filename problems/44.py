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


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         pass

class Solution(object):
    def isMatch(self, s, p):
        """
        Inspired from youtube video: regular expression dynamic programming
        :param s:
        :param p:
        :return:
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for col in range(1, len(p)+1):
            if p[col-1] == "*":
                dp[0][col] = dp[0][col-1]
        for row in range(1, len(s) + 1):
            for col in range(1, len(p) + 1):
                if p[col-1] == "*":
                    dp[row][col] = dp[row][col - 1] or dp[row-1][col]
                    # if dp[row][col-1]:
                    #     dp[row][col] = dp[row][col-1]
                    # else:
                    #     row_idx = row - 1
                    #     while row_idx >= 0 and not dp[row][col]:
                    #         if dp[row_idx][col]:
                    #             dp[row][col] = dp[row_idx][col]
                    #         row_idx -= 1
                if s[row-1] == p[col-1] or p[col-1] == "?":
                    dp[row][col] = dp[row-1][col-1]
        # for idx, lst in enumerate(dp):
        #     print(idx)
        #     print(lst)
        return dp[-1][-1]


s = "bbabbaabbbabaaaabbbbabbaabbaaabbbbabbbaaaaaaaaaababbbabaabaabbbabbbaaabaababbbbababaaaaabaaaabbbbabbaaabbaaabbaabbbbababaaaaabbbbaaabababbbaabbbbaabbaabbabbbaabbababaaabbabbbaababbbbaaaabbababbbbabaaa"
p = "**baab*a*bb*bbbbba********b***a******b*b*aaabbb*b*ba*a*b*a****b*babbba*aa*ababa*bb***babb*ab*b*abab*aa"
res = Solution().isMatch(s, p)
print(res)