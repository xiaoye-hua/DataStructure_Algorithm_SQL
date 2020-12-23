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


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        approach 1: brute force sort:  304ms
        approach 2: heap ： 316ms 没啥大提升
        :param lo:
        :param hi:
        :param k:
        :return:
        """
        import heapq
        max_heap = []
        self.cache = {
            1:0
        }
        for key in range(lo, hi+1):
            value = self.get_power(key)
            if len(max_heap)<k:
                heapq.heappush(max_heap, [-value, -key])
            else:
                if value < -max_heap[0][0] or (value == -max_heap[0][0] and key<-max_heap[0][1]):
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, [-value, -key])
        return -max_heap[0][1]

    # [[8, 3], [10, 6], [11, 14], [7, 16], [9, 19]]

    # def getKth(self, lo: int, hi: int, k: int) -> int:
    #     """
    #     approach 1: brute force sort:  304ms
    #     approach 2: heap
    #     :param lo:
    #     :param hi:
    #     :param k:
    #     :return:
    #     """
    #     import heapq
    #     max_heap = []
    #     self.cache = {
    #         1: 0
    #     }
    #     result = []
    #     for key in range(lo, hi + 1):
    #         value = self.get_power(key)
    #         result.append(
    #             [key, value]
    #         )
    #     result = sorted(result, key=lambda x: [x[1], x[0]])
    #     print(result)
    #     return result[k-1][0]

    def get_power(self, num):
        try:
            return self.cache[num]
        except:
            if num%2 == 0:
                 self.cache[num] = 1 + self.get_power(num/2)
            else:
                self.cache[num] = 1 + self.get_power(3*num+1)
            return self.cache[num]

# Input: lo = 12, hi = 15, k = 2
# Output: 13
# Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
# The power of 13 is 9
# The power of 14 is 17
# The power of 15 is 17
# The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
# Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.


# lo = 12
# hi = 15
# k = 2
lo = 7
hi = 11
k = 4
res = Solution().getKth(lo, hi, k)
# print(Solution().get_power(3))
print(res)

