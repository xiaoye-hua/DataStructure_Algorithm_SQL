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


class TrieNode:
    def __init__(self):
        self.is_end_word = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for w in word:
            index = ord(w) - ord("a")
            if not p.children[index]:
                p.children[index] = TrieNode()
            p = p.children[index]
        p.is_end_word = True

    def search(self, word):
        node = self.find(word)
        if node is None:
            return False
        elif node.is_end_word:
            return True
        else:
            return False

    def startsWith(self, word):
        node = self.find(word)
        return node is not None

    def find(self, word):
        p = self.root
        for w in word:
            index = ord(w) - ord("a")
            if not p.children[index]:
                return None
            p = p.children[index]
        return p

trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))

print(trie.search("app"))
print(trie.startsWith("app"))





# class TrieNode(object):
#     def __init__(self):
#         self.is_word = False
#         self.children = [None] * 26
#
#
# class Trie(object):
#
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         p = self.root
#         for c in word:
#             index = ord(c) - ord('a')
#             if not p.children[index]:
#                 p.children[index] = Trie.TrieNode()
#             p = p.children[index]
#         p.is_word = True
#
#     def search(self, word):
#         node = self.find(word)
#         return node is not None and node.is_word
#
#     def startsWith(self, prefix):
#         return self.find(prefix) is not None
#
#     def find(self, prefix):
#         p = self.root
#         for c in prefix:
#             index = ord(c) - ord('a')
#             if not p.children[index]: return None
#             p = p.children[index]
#         return p
#
#
# # ["Trie","insert","search","search","startsWith","insert","search"]
# # [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]