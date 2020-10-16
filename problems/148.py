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
    def sortList(self, head: ListNode) -> ListNode:
        # return head
        if not head or not head.next:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        # print(LinkedList.print_linkedlist(no))
        # LinkedList.print_linkedlist(head)
        first = self.sortList(head)
        second = self.sortList(second_half)
        return self.merge(first, second)

    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        if not head1:
            return head2
        if not head2:
            return head1
        dummy_head = ListNode(None)
        head = dummy_head
        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        if head1:
            head.next = head1
        if head2:
            head.next = head2
        return dummy_head.next


s = "aaabb"
k = 3
head = LinkedList([-1,5,3,4,0]).head
res = Solution().sortList(head)
LinkedList.print_linkedlist(res)