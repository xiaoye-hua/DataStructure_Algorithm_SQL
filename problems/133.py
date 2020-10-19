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
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.node_map = collections.defaultdict(lambda: Node(None, []))
        self.node_map[None] = None
        self.visited = []
        self.dfs(node)
        return self.node_map[node]

    def dfs(self, node):
        if not node or node.val in self.visited:
            return
        self.node_map[node].val = node.val
        for n in node.neighbors:
            self.node_map[node].neighbors.append(
                self.node_map[n]
            )
        self.visited.append(node.val)
        for n in node.neighbors:
            self.dfs(n)