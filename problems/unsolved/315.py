#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None, value=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, tree_node: TreeNode):
        if not self.root:
            self.root = tree_node
        else:
            root = self.root
            left_child = None
            parent = None
            while root:
                parent = root
                if root.key<tree_node.key:

                    # tree_node.value[1] = tree_node.value[1] + root.value[1] + root.value[0]
                    left_child = False
                    root = root.right
                elif root.key == tree_node.key:
                    left_child = None
                    # root.value[0] += 1
                    break
                else:
                    # root.value[1] += 1
                    left_child = True
                    root = root.left
            if left_child is None:
                root.value[0] += 1
                return
            elif left_child:
                parent.value[1] += 1
                parent.left = tree_node
                tree_node.parent = parent
            else:
                tree_node.value[1] = tree_node.value[1] + parent.value[1] + parent.value[0]
                parent.right = tree_node
                tree_node.parent = parent
        # return smaller count
        return tree_node.value[1]

    def get_value(self, key):
        root = self.root
        while root:
            if key == root.key:
                return root.value
            elif key > root.key:
                root = root.right
            else:
                root = root.left


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        second try: binary search tree
        :param nums:
        :return:
        """
        res = [0 for _ in range(len(nums))]
        bst = BinarySearchTree()
        for idx in range(len(nums)-1, -1, -1):
            tree_node = TreeNode(key=nums[idx], value=[1, 0])
            target = bst.insert(tree_node)
            res[idx] = target
        # res = []
        # for n in nums:
        #     value = bst.get_value(n)
        #     res.append(value[1])
        return res

        # """
        # first try: max heap --> ETL ??
        #     time complexity: 0(n**2)
        # :param nums:
        # :return:
        # """
        # import heapq
        # max_heap = []
        # for n in nums:
        #     heapq.heappush(max_heap, -n)
        # previous_item = float("inf")
        # left_lst = []
        # res = []
        # for item in nums:
        #     first_present = True
        #     if item <= previous_item:
        #         while len(max_heap)>0 and item <= -max_heap[0]:
        #             max_item = -heapq.heappop(max_heap)
        #             if first_present and max_item == item:
        #                 first_present = False
        #             else:
        #                 left_lst.append(max_item)
        #     else:
        #         idx = len(left_lst)-1
        #         while first_present and idx>=0 and left_lst[idx]<=item:
        #             new_item = left_lst[idx]
        #             if first_present and new_item == item:
        #                 first_present = False
        #             else:
        #                 heapq.heappush(max_heap, -new_item)
        #             left_lst.pop(-1)
        #             idx -= 1
        #     print(f"item: {item}")
        #     print(f"max_heap: {max_heap}")
        #     print(f"left_lst: {left_lst}")
        #     res.append(len(max_heap))
        #     print(f"res: {res}")
        #     previous_item = item
        # return res

nums = [5, 2, 6, 1]
res = Solution().countSmaller(nums)
print(res)