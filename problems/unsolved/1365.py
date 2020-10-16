#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        first try: max heap --> ETL ??
            time complexity: 0(n**2)
        :param nums:
        :return:
        """
        import heapq
        max_heap = []

        for n in nums:
            heapq.heappush(max_heap, -n)
        previous_item = float("inf")
        left_lst = []
        res = []
        for item in nums:
            first_present = True
            heapq.heappush(max_heap, -previous_item)
            if item <= previous_item:
                while len(max_heap)>0 and item <= -max_heap[0]:
                    max_item = -heapq.heappop(max_heap)
                    if first_present and max_item == item:
                        first_present = False
                    else:
                        left_lst.append(max_item)
            else:
                idx = len(left_lst)-1
                while first_present and idx>=0 and left_lst[idx]<=item:
                    new_item = left_lst[idx]
                    if first_present and new_item == item:
                        first_present = False
                    else:
                        heapq.heappush(max_heap, -new_item)
                    left_lst.pop(-1)
                    idx -= 1
            # print(f"item: {item}")
            # print(f"max_heap: {max_heap}")
            # print(f"left_lst: {left_lst}")
            res.append(len(max_heap))
            # print(f"res: {res}")
            previous_item = item
        return res

nums = [8,1,2,2,3]
res = Solution().smallerNumbersThanCurrent(nums)
print(res)