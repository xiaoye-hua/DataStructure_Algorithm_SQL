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

import copy

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.matrix = {value: [] for value in range(n)}
        self.connection = connections
        self.n = n
        for lst in connections:
            a, b = lst
            self.matrix[a].append(b)
            self.matrix[b].append(a)
        res = []
        for lst in connections:
            if self.check_critical(lst):
                res.append(lst)
        return res

    def check_critical(self, lst):
        a, b = lst
        self.current_matrix = copy.deepcopy(self.matrix)
        self.current_matrix[a].remove(b)
        self.current_matrix[b].remove(a)
        self.visited = set()
        self.dfs(a)
        return len(self.visited)!=self.n

    def dfs(self, node):
        self.visited.add(node)
        for next_node in self.current_matrix[node]:
            if next_node not in self.visited:
                self.dfs(next_node)



# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
res = Solution().criticalConnections(n, connections)
print(res)