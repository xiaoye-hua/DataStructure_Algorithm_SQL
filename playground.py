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

import copy
import bisect


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.res = max(self.res, self.parser_one_side(root, 0))
        return self.res

    self.parse_one_side(self, root: Optional[TreeNode], depth: int) -> int:
    if root is None:
        return depth
    l = self.parse_one_side(root.left, 0)
    r = self.parse_one_size(root.right, 0)
    self.res = max(self.res, l + r)
    return max(l, r)


res = Solution().longestObstacleCourseAtEachPosition([3,1,5,6,4,2])
print(res)
