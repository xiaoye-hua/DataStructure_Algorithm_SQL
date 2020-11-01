#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/1 1:37 下午
# @Author  : guohua08
# @File    : SegmentTree.py
class SegmentTreeNode:
    def __init__(self, value=None, start=None, end=None, left=None, right=None):
        self.value = value
        self.start = start
        self.end = end
        self.left = left
        self.right = right


class SegmentTree:
    def __init__(self, start, end, lst):
        self.root = self.build_tree(start, end, lst)

    def build_tree(self, start, end, lst):
        if start == end:
            return SegmentTreeNode(
                value=lst[start]
                , start=start
                , end=end
            )
        mid = (start+end)//2
        left = right = None
        if mid >= start:
            left = self.build_tree(
                start=start
                , end = mid
                , lst=lst
            )
        if mid+1<=end:
            right = self.build_tree(
                start=mid+1
                , end=end
                , lst=lst
            )
        return SegmentTreeNode(
            value=left.value+right.value
            , start=start
            , end=end
            , left=left
            , right=right
        )

    def update_tree(self, index, value, root):
        if root.start == root.end == index:
            root.value = value
            return
        mid = (root.start + root.end) // 2
        if index <= mid:
            self.update_tree(
                index=index
                , value=value
                , root=root.left
            )
        else:
            self.update_tree(
                index=index
                , value=value
                , root=root.right
            )
        root.value = root.left.value + root.right.value

    def query(self, begin, end, root):
        if not root:
            return 0
        if root.start == begin and root.end == end:
            return root.value
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self.query(begin, end, root.left)
        elif begin > mid:
            return self.query(begin, end, root.right)
        else:
            return self.query(begin, mid, root.left) + self.query(mid+1, end, root.right)