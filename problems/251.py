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


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.lst = []
        for lst in v:
            if isinstance(lst, list):
                self.lst.extend(lst)
            else:
                self.lst.append(lst)

    def next(self) -> int:
        return self.lst.pop(0)

    def hasNext(self) -> bool:
        return len(self.lst) != 0
