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
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group2item = {}
        item2group = {}
        max_group = max(group)
        for item, g in zip(range(n), group):
            if g == -1:
                group_num = max_group + 1
                max_group += 1
                group2item[group_num] = [item]
            else:
                group_num = g
                try:
                    group2item[group_num].append(item)
                except:
                    group2item[group_num] = [item]
            item2group[item] = group_num
        # before_item = [[] for _ in range(max_group+1)]
        # group_before_item = {key: [[] for _ in range(len(value))] for key, value in group2item.items()}
        group_adjacent_matrix = {key: [] for key in group2item.keys()}
        adjacent_matrix_dict = {key: {value: [] for value in item} for key, item in group2item.items()}
        for idx, ele in enumerate(beforeItems):
            # print(idx)
            # print(item2group)
            group1 = item2group[idx]
            for item in ele:
                group2 = item2group[item]
                if group2 != group1:
                    # before_item[group1].append(group2)
                    group_adjacent_matrix[group2].append(group1)

                else:
                    try:
                        adjacent_matrix_dict[group1][item].append(idx)
                    except:
                        adjacent_matrix_dict[group1][item] = [idx]
        res = []
        group_lst = self.top_sort(group_adjacent_matrix)
        if len(group_lst) == 0:
            return []
        for group in group_lst:
            single_group = self.top_sort(adjacent_matrix_dict[group])
            if len(single_group) == 0:
                return []
            res.extend(single_group)
        return res

    def top_sort(self, adjacent_matrix):
        self.adjacent_matrix  = adjacent_matrix
        self.status = {key:0 for key in self.adjacent_matrix.keys()}
        # for idx, item in enumerate(before_item):
        #     try:
        #         self.adjacenta_matrix[item].append(idx)
        #     except:
        #         self.adjacenta_matrix[item] = [idx]
        #     self.status[idx] = 0
        self.res = []
        for key in self.adjacent_matrix.keys():
            if not self.dfs(key):
                return []
        return self.res

    def dfs(self, node):
        if self.status[node] == 1:
            return False
        if self.status[node] == 2:
            return True
        self.status[node] = 1
        for child in self.adjacent_matrix[node]:
            if not self.dfs(child):
                return False
        self.status[node] = 2
        self.res.insert(0, node)
        return True


n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]


n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
# Output: [6,3,4,1,5,2,0,7]
res = Solution().sortItems(n, m, group, beforeItems)
print(res)