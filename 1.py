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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value2index = {}
        for idx, value in enumerate(nums):
            try:
                idx1 = value2index[target - value]
                return [idx1, idx]
            except:
                value2index[value] = idx
