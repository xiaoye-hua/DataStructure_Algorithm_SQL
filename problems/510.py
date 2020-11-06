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

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        root = node
        while root.parent:
            root = root.parent
        p = node
        self.value = []
        self.dfs(root)
        if self.value[-1].val == p.val:
            return None
        else:
            for idx in range(len(self.value)):
                if self.value[idx].val == p.val:
                    return self.value[idx + 1]

    def dfs(self, root):
        # print(root)
        if not root:
            return
        self.dfs(root.left)
        self.value.append(root)
        self.dfs(root.right)
