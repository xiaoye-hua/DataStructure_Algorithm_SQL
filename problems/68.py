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
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.res = []
        self.maxWidth = maxWidth
        self.words = words
        self.length = len(self.words)
        self.justifySinle(0)
        return self.res

    def justifySinle(self, begin_idx):
        if begin_idx >= self.length:
            return
        elif begin_idx == self.length-1:
            res = self.words[-1] + " "*(self.maxWidth-len(self.words[-1]))
            self.res.append(res)
        else:
            current_word = self.words[begin_idx]
            current_length = len(current_word)
            idx = begin_idx+1
            words = [current_word]
            while idx < self.length and current_length+len(self.words[idx])+1<=self.maxWidth:
                words.append(self.words[idx])
                current_length += len(self.words[idx]) + 1
                idx += 1
            if len(words) == 1 or idx>=self.length:
                res = " ".join(words) + " " * (self.maxWidth - (sum([len(w) for w in words]) + len(words)-1))
                self.res.append(res)
            else:
                left = self.maxWidth - sum([len(w) for w in words])
                quotient, remainder = divmod(left, len(words)-1)
                # seq = " "*quotient
                seq1 = " "*(quotient+1)
                seq2 = " "*quotient
                first_half = seq1.join(words[:remainder+1])
                second_half = seq2.join(words[remainder+1:])
                self.res.append(
                    first_half + seq2 + second_half
                )
            # print(self.res)
            self.justifySinle(idx)


# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:
#
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be",
#              because the last line must be left-justified instead of fully-justified.
#              Note that the second line is also left-justified becase it contains only one word.

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
res = Solution().fullJustify(words, maxWidth)
print(res)
# Wrong Answer
# Details
# Input
# ["What","must","be","acknowledgment","shall","be"]
# 16
# Output
# ["What   must   be","acknowledgment  ","shall be         "]
# Expected
# ["What   must   be","acknowledgment  ","shall be        "]