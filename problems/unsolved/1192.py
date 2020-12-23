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

class GraphNode:
    def __init__(self, val=None, visited=False, parent=None, depth=float("inf"), lowest_depth=float("inf"), children=[]):
        self.val = val
        self.visited = visited
        self.parent = parent
        self.depth = depth
        self.lowest_depth = lowest_depth
        self.children = children

import collections
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Second try: object oriented  --> failed   为啥每次node_lst的所有ele会同时发生变化？？？  不懂，看答案 https://leetcode.com/problems/critical-connections-in-a-network/discuss/382440/Python-DFS-Tree-Solution-(O(V+E)-complexity)
        :param n:
        :param connections:
        :return:
        """
    #     node_lst = [GraphNode(val=i) for i in range(n)]
    #     for lst in connections:
    #         # ??? 为啥每次node_lst的所有ele会同时发生变化？？？
    #         a, b = lst
    #         node_lst[a].children.append(node_lst[b])
    #         node_lst[b].children.append(node_lst[a])
    #     self.res = []
    #     self.find(node_lst[0], 0)
    #     return self.res
    #
    # def find(self, node: GraphNode, depth):
    #     node.depth = depth
    #     node.visited = True
        self.depth = [0] * n
        self.visited = [False] * n
        self.min_depth = [float("inf")] * n
        self.parent = [None] * n
        self.res = []
        self.matrix = {value: [] for value in range(n)}
        for lst in connections:
            a, b = lst
            self.matrix[a].append(b)
            self.matrix[b].append(a)
        self.find(0, 0)
        return self.res

    def find(self, node, depth):
        self.depth[node] = depth
        self.min_depth[node] = depth
        self.visited[depth] = True
        depth += 1
        for child in self.matrix[node]:
            if not self.visited[child]:
                self.parent[child] = node
                self.find(child, depth)
                if self.min_depth[child] > self.depth[node]:
                    self.res.append([node, child])
            if self.parent[node] != child:
                self.min_depth[node] = min(self.min_depth[node], self.min_depth[child])







    #     #################
    #     First
    #     try:
    # #################
    #     self.matrix = {value: [] for value in range(n)}
    #     self.connection = connections
    #     self.n = n
    #     for lst in connections:
    #         a, b = lst
    #         self.matrix[a].append(b)
    #         self.matrix[b].append(a)
    #     res = []
    #     for lst in connections:
    #         if self.check_critical(lst):
    #             res.append(lst)
    #     return res
    #
    # def check_critical(self, lst):
    #     a, b = lst
    #     self.current_matrix = copy.deepcopy(self.matrix)
    #     self.current_matrix[a].remove(b)
    #     self.current_matrix[b].remove(a)
    #     self.visited = set()
    #     self.dfs(a)
    #     return len(self.visited)!=self.n
    #
    # def dfs(self, node):
    #     self.visited.add(node)
    #     for next_node in self.current_matrix[node]:
    #         if next_node not in self.visited:
    #             self.dfs(next_node)


    # def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    #
    #     dic = collections.defaultdict(list)
    #     for c in connections:
    #         u, v = c
    #         dic[u].append(v)
    #         dic[v].append(u)
    #
    #     timer = 0
    #
    #     depth, lowest, parent, visited = [float("inf")] * n, [float("inf")] * n, [float("inf")] * n, [False] * n
    #     res = []
    #
    #     def find(u):
    #
    #         nonlocal timer
    #
    #         visited[u] = True
    #         depth[u], lowest[u] = timer, timer
    #         timer += 1
    #
    #         for v in dic[u]:
    #
    #             if not visited[v]:
    #                 parent[v] = u
    #                 find(v)
    #                 if lowest[v] > depth[u]:
    #                     res.append([u, v])
    #
    #             if parent[u] != v:
    #                 lowest[u] = min(lowest[u], lowest[v])
    #
    #     find(0)
    #     return res



# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
res = Solution().criticalConnections(n, connections)
print(res)