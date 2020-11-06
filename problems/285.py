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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        self.value = []
        self.dfs(root)
        if self.value[-1].val == p.val:
            return None
        else:
            for idx in range(len(self.value)):
                if self.value[idx].val == p.val:
                    return self.value[idx+1]

    def dfs(self, root):
        # print(root)
        if not root:
            return
        self.dfs(root.left)
        self.value.append(root)
        self.dfs(root.right)


root2 = TreeNode(2)
root1 = TreeNode(1)
root3 = TreeNode(3)
root2.left = root1
root2.right = root3

res = Solution().inorderSuccessor(root2, root1)
print(res)
# k = 3
# res = Solution().longestSubstring(s, k)
# print(res)