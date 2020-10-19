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


# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        """
        Similar as 138
        """
        self.node_map = collections.defaultdict(lambda: NodeCopy(None, None, None, None))
        self.node_map[None] = None
        self.dfs(root)
        return self.node_map[root]

    def dfs(self, root):
        if not root:
            return
        self.node_map[root].val = root.val
        self.node_map[root].left = self.node_map[root.left]
        self.node_map[root].right = self.node_map[root.right]
        self.node_map[root].random = self.node_map[root.random]
        self.dfs(root.left)
        self.dfs(root.right)