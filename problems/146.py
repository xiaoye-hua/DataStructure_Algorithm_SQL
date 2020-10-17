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


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent_key = None
        self.current_num = 0
        self.dict = dict()
        self.used_seq = []

    def get(self, key: int) -> int:
        try:
            value = self.dict[key]
            if key in self.used_seq:
                self.used_seq.remove(key)
            self.used_seq.append(key)
            return value
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key == 4:
        #     print(self.current_num)
        #     print(self.dict)
        if self.current_num == self.capacity and key not in self.dict:
            target_key = self.used_seq.pop(0)
            del self.dict[target_key]
            self.current_num -= 1
        if key in self.used_seq:
            self.used_seq.remove(key)
        self.used_seq.append(key)
        if key not in self.dict:
            self.current_num += 1
        self.dict[key] = value
        self.recent_key = key

        # print('8'*20)
        # print(f"{key}:{value}")
        # print(self.used_seq)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
for a, b, c in zip(["LRUCache","put","put","get","put","get","put","get","get","get"], [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]], ['null','null','null',1,'null',-1,'null',-1,3,4]):
    print("*" * 30)
    print(a)
    print(b)
    print(c)