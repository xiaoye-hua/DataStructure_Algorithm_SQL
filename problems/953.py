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
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_rank = {char: idx for idx, char in enumerate(order)}
        for idx in range(len(words)-1):
            w1 = words[idx]
            w2 = words[idx+1]
            idx = 0
            found = False
            while idx < len(w1) and idx < len(w2) and not found:
                if w1[idx] != w2[idx]:
                    found = True
                    if char_rank[w1[idx]] > char_rank[w2[idx]]:
                        return False
                idx += 1
            if w1[idx-1] == w2[idx-1] and len(w1)>len(w2):
                return False
        return True


# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
words = ["kuvp","q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
res = Solution().isAlienSorted(words, order)
print(res)