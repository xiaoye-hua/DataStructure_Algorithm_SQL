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
    def numberToWords(self, num: int) -> str:
        """
        Inspired by leetcode 12: integer to Roman
        :param num:
        :return:
        """
        pass

num = 123
res = Solution().numberToWords(num)
print(res)