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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        First try: ETL
        Second try: Inspired from discussion https://leetcode.com/problems/insertion-sort-list/discuss/190913/Java-Python-with-Explanations
        :param head:
        :return:
        """
        dummy_head = ListNode(None)
        dummy_head.next = node_to_insert = head
        while head and head.next:
            if head.val>head.next.val:
                node_to_insert = head.next
                node_to_insert_pre = dummy_head
                while node_to_insert_pre.next.val < node_to_insert.val:
                    node_to_insert_pre = node_to_insert_pre.next
                head.next = node_to_insert.next
                node_to_insert.next = node_to_insert_pre.next
                node_to_insert_pre.next = node_to_insert
            else:
                head = head.next
        return dummy_head.next

        # if not head:
        #     return head
        # length = 0
        # dummy_head = ListNode(None)
        # dummy_head.next = head
        # head_copy = head
        # while head_copy:
        #     length += 1
        #     head_copy = head_copy.next
        #     # LinkedList.print_linkedlist(head_copy)
        # if length == 1:
        #     return head
        # length -= 1
        # while length != 0:
        #     step = length
        #     current_head = dummy_head
        #     previous = None
        #     while step != 0:
        #         previous = current_head
        #         current_head = current_head.next
        #         step -= 1
        #     while current_head.next and current_head.val > current_head.next.val:
        #         previous.next = current_head.next
        #         previous = current_head.next
        #
        #         current_head.next = current_head.next.next
        #         # current_head.next.next = current_head
        #         previous.next = current_head
        #     length -= 1
        # return dummy_head.next

head = LinkedList([4, 2, 1, 3]).head
res = Solution().insertionSortList(head)
# print(res)
LinkedList.print_linkedlist(res)