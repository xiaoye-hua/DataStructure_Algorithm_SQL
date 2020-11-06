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
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        str_log = []
        digit_log = []
        for ele in logs:
            try:
                int(ele.split(" ")[-1])
                digit_log.append(ele)
            except:
                str_log.append(
                    ele.split(" ")
                )
        str_log.sort(
            key=lambda x: x[1:]
        )
        str_log = [" ".join(ele) for ele in str_log]
        str_log.extend(digit_log)
        return str_log

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
# Output
# ["g1 act car","a2 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
# Expected
# ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

res = Solution().reorderLogFiles(logs)
print(res)