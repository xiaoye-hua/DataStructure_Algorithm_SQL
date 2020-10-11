#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:40 下午
# @Author  : guohua08
# @File    : LinkedList.py
from typing import List

from src.linked_list.ListNode import ListNode


class LinkedList:
    def __init__(self, lst: List[int]) -> None:
        dummy_head = ListNode(None)
        head = dummy_head
        for val in lst:
            node = ListNode(val=val)
            head.next = node
            head = head.next
        self.head = dummy_head.next

    @staticmethod
    def print_linkedlist(node: ListNode):
        while node:
            print(node.val)
            node = node.next
