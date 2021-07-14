#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 8:12 上午
# @Author  : guohua08
# @File    : MinHeap.py


class MinHeap:
    def __init__(self, list_input=False):
        """
        heap property:
            1. structure property:
                complete tree, 2p and 2p+1 between parent and children
            2. order property:
                parent is smaller that children

        list_input: whether the input value is a list, if True, the first element of the list will be the key
        """
        self.lst = [0]
        self.size = 0  # size of heap
        self.list_input = list_input

    def push(self, value):
        self.lst.append(value)
        self.size += 1
        self.prec_up(self.size)

    def pop(self):
        min_value = self.lst.pop(1)
        self.size -= 1
        self.lst.insert(1, self.lst.pop())
        self.prec_down(1)
        return min_value

    def build_heap(self, lst):
        """
        Two methods to build from a entire list:
            1. iterate and insert one by one：　O(nlogn)
            2. start with the entire list: O(n)
        """
        i = len(lst) // 2
        self.lst = [0] + lst[:]
        self.size = len(lst)
        while i >= 0:
            self.prec_down(i)
            i -= 1

    def prec_up(self, i):
        if self.list_input:
            while i//2>0:
                idx = i//2
                if self.lst[idx][0] >= self.lst[i][0]:
                    self.lst[idx], self.lst[i] = self.lst[i], self.lst[idx]
                else:
                    return
                i = idx
        else:
            while i//2>0:
                idx = i//2
                if self.lst[idx] >= self.lst[i]:
                    self.lst[idx], self.lst[i] = self.lst[i], self.lst[idx]
                else:
                    return
                i = idx

    def prec_down(self, i):
        if self.list_input:
            while 2 * i <= self.size:
                idx = self.min_child(i)
                if self.lst[idx][0] <= self.lst[i][0]:
                    self.lst[idx], self.lst[i] = self.lst[i], self.lst[idx]
                    i = idx
                else:
                    return
        else:
            while 2*i <= self.size:
                idx = self.min_child(i)
                if self.lst[idx] <= self.lst[i]:
                    self.lst[idx], self.lst[i] = self.lst[i], self.lst[idx]
                    i = idx
                else:
                    return

    def min_child(self, i):
        if 2*i+1 > self.size:
            return 2*i
        if self.list_input:
            if self.lst[2 * i][0] < self.lst[2 * i + 1][0]:
                return 2 * i
            else:
                return 2 * i + 1
        else:
            if self.lst[2*i] < self.lst[2*i+1]:
                return 2*i
            else:
                return 2*i + 1