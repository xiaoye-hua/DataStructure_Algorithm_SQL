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

import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """Second try:"""
        # if len(nums) == 1:
        #     return nums
        self.res = []
        self.remain_remove_idx = set([])
        self.small_half = [] # max heap
        self.large_half = [] # min heap
        self.nums = nums
        if k % 2 == 0:
            self.even = True
            large_half_len = k//2
        else:
            self.even = False
            large_half_len = k//2 + 1

        for idx, value in enumerate(nums[:k]):
            heapq.heappush(self.small_half, [-value, idx])
        for _ in range(large_half_len):
            self.move_root(self.small_half, self.large_half)
        self.res.append(self.get_median())
        for remove_idx in range(0, len(nums)-k):
            self.remain_remove_idx.add(remove_idx)
            add_value = nums[remove_idx+k]
            if add_value >= self.large_half[0][0]:
                heapq.heappush(self.large_half, [add_value, remove_idx + k])
                # ??
                if nums[remove_idx] <= self.large_half[0][0]:
                    # ?? how to ensure the first has not been removed
                    self.move_root(self.large_half, self.small_half)
            else:
                heapq.heappush(self.small_half, [-add_value, remove_idx + k])
                if nums[remove_idx] >= self.large_half[0][0]:
                    self.move_root(self.small_half, self.large_half)
            while self.large_half and self.large_half[0][1] in self.remain_remove_idx:
                idx = self.large_half[0][1]
                heapq.heappop(self.large_half)
                self.remain_remove_idx.remove(idx)
            while self.small_half and self.small_half[0][1] in self.remain_remove_idx:
                idx = self.small_half[0][1]
                heapq.heappop(self.small_half)
                self.remain_remove_idx.remove(idx)
            self.res.append(self.get_median())
            # print(f'small part {self.small_half}')
            # print(f'large part {self.large_half}')
            # print()
        return self.res

    def move_root(self, from_heap, to_heap):
        lst = heapq.heappop(from_heap)
        heapq.heappush(to_heap, [-lst[0], lst[1]])

    def get_median(self):
        if self.even:
            return (self.large_half[0][0] - self.small_half[0][0]) / 2
        else:
            return self.large_half[0][0]

    #
    #     """
    #     Approach two: with two heap
    #         time complicity: O(nlogk)
    #           ele value can not been used; alternative  use ele index
    #     """
    #     import heapq
    #     small_heap = []  # max heap
    #     large_heap = []  # min heap
    #     res = []
    #     visited = set([0])
    #     for i in range(k):
    #         heapq.heappush(small_heap, [-nums[i], i])
    #     if k % 2 == 0:
    #         large_len = k // 2
    #         self.k_even = True
    #     else:
    #         large_len = k // 2 + 1
    #         self.k_even = False
    #     for _ in range(large_len):
    #         self.move_root(small_heap, large_heap)
    #     res.append(self.get_median(small_heap, large_heap))
    #     for idx, ele in enumerate(nums[k:]):
    #         if ele >= large_heap[0][0]:
    #             heapq.heappush(large_heap, [ele, idx + k])
    #             # ??
    #             if nums[idx] <= large_heap[0][0]:
    #                 self.move_root(large_heap, small_heap)
    #         else:
    #             heapq.heappush(small_heap, [-ele, idx + k])
    #             if nums[idx] >= large_heap[0][0]:
    #                 self.move_root(small_heap, large_heap)
    #         # remove the visited index
    #         visited.add(idx)
    #         while large_heap and large_heap[0][1] in visited:
    #             heapq.heappop(large_heap)
    #         while small_heap and small_heap[0][1] in visited:
    #             heapq.heappop(small_heap)
    #         print(f'small part {small_heap}')
    #         print(f'large part {large_heap}')
    #         print()
    #         res.append(self.get_median(small_heap, large_heap))
    #     return res
    #
    # def move_root(self, heap1, heap2):
    #     root = heapq.heappop(heap1)
    #     heapq.heappush(heap2, [-root[0], root[1]])
    #
    # def get_median(self, small_heap, large_heap):
    #     if self.k_even:
    #         return (-small_heap[0][0] + large_heap[0][0]) / 2
    #     else:
    #         return large_heap[0][0]

#         """
#         Approch one:
#             time complicity O(nk)
#         """
#         res = []
#         i = 0
#         j = k - 1
#         if k % 2 == 0:
#             even = True
#         else:
#             even = False
#         current_windows = nums[i:j + 1]
#         current_windows.sort()
#         target_idx = (i + j) // 2
#         # print(target_idx)
#         if even:
#             median = (current_windows[target_idx] + current_windows[target_idx + 1]) / 2
#         else:
#             median = current_windows[target_idx]
#         res.append(median)

#         for j in range(k, len(nums)):
#             current_windows.remove(nums[i])
#             i += 1
#             idx = 0
#             while idx < len(current_windows) and nums[j] > current_windows[idx]:
#                 idx += 1
#             current_windows.insert(idx, nums[j])
#             if even:
#                 median = (current_windows[target_idx] + current_windows[target_idx + 1]) / 2
#             else:
#                 median = current_windows[target_idx]
#             res.append(median)
#         return res


nums = [1, 1, 1, 1]
k = 2

# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]

res = Solution().medianSlidingWindow(nums, k)
print(res)