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
from src.MinHeap import MinHeap


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
# """
# approch 1: bubble sort
# """
# for idx in range(k):
#     for sec_idx in range(idx+1, len(nums)):
#         if nums[sec_idx] >nums[idx]:
#             tmp = nums[sec_idx]
#             nums[sec_idx] = nums[idx]
#             nums[idx] = tmp
# # print(nums)
# return nums[idx]
#         """
#         Approch 2:  min heap
#         """
#         import heapq
#
#         min_heap = []
#         for ele in nums:
#             if len(min_heap)>=k:
#                 heapq.heappushpop(min_heap, ele)
#             else:
#                 heapq.heappush(min_heap, ele)
#         return min_heap[0]


        # min_heap = []
        min_heap = MinHeap()
        for ele in nums:
            min_heap.push(ele)
            if min_heap.size>k:
                min_heap.pop()
        return min_heap.lst[1]



# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
nums = [3,2,1,5,6,4]
k = 2
result = Solution().findKthLargest(nums, k)
print(result)