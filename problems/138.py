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
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        First try: failed
        Second try: inspired by hints  ??? Why my solution failed
        Thirde try: inspried from discussion: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution
        """
        map_new = collections.defaultdict(
            lambda: Node(0, None, None)
        )
        map_new[
            None] = None  # if a node's next or random is None, their value will be None but not a new Node, doing so removes the if-else check in the while loop

        nd_old = head
        while nd_old:
            map_new[nd_old].val = nd_old.val
            map_new[nd_old].next = map_new[nd_old.next]
            map_new[nd_old].random = map_new[nd_old.random]
            nd_old = nd_old.next
        return map_new[head]

#         if not head:
#             return head
#         dummy_head = Node(9999999999)
#         dummy_head.next = head
#         while head:
#             new_node = Node(head.val)
#             new_node.next = head.next
#             head.next = new_node
#             head = head.next.next
#         slow = dummy_head.next
#         fast = slow.next
#         while slow.next.next:
#             random = slow.random
#             if not random:
#                 fast.random = None
#             else:
#                 fast.random = random.next
#             slow = slow.next.next
#             fast = fast.next.next
#         result_dummy = Node(9999999999)
#         # fast = dummy_head.next.next
#         while dummy_head.next and dummy_head.next.next:
#             result_dummy.next = dummy_head.next.next
#             dummy_head = dummy_head.next.next
#         return result_dummy.next
# #         if not head:
#             return head
#         dummy_head = Node(9999999999)
#         dummy_head.next = head

#         node_lst = []
#         val_lst = []
#         while head:
#             node = Node(x=head.val)
#             val_lst.append(head.val)
#             node_lst.append(node)
#             head = head.next
#         for idx in range(len(node_lst)-1):
#             node_lst[idx].next = node_lst[idx+1]
#         head = dummy_head.next
#         idx = 0
#         while head:
#             random = head.random
#             if not random:
#                 node_lst[idx].random = None
#             else:
#                 # random_value = head.random.val
#                 # random_idx = val_lst.index(random_value)
#                 node_lst[idx].random = node_lst[random_idx]
#             idx += 1
#             head = head.next
#         return node_lst[0]

