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
    def maxArea(self, height: List[int]) -> int:
        """
        为啥非得移动短的那个？？ 为啥第二种方法不对？？
        """
        res = 0
        begin_idx = 0
        end_idx = len(height) - 1
        while end_idx != begin_idx:
            # if heght[begin_idx]<height[]
            res = max(res, (end_idx - begin_idx) * min(height[end_idx], height[begin_idx]))
            if height[begin_idx] < height[end_idx]:
                begin_idx += 1
            else:
                end_idx -= 1
        return res


#         res = 0
#         begin_idx = 0
#         end_idx = len(height)-1
#         while end_idx != begin_idx:
#             # if heght[begin_idx]<height[]

#             res = max(res, (end_idx-begin_idx)*min(height[end_idx], height[begin_idx]))
#             if height[begin_idx]<height[end_idx]:
#                 if height[begin_idx+1] >= height[begin_idx]:
#                     begin_idx += 1
#                 else:
#                     if height[begin_idx+1] > height[end_idx-1]:
#                         begin_idx += 1
#                     else:
#                         end_idx -= 1
#             else:
#                 if height[end_idx-1] >= height[end_idx]:
#                     end_idx -= 1
#                 else:
#                     if height[end_idx-1] > height[begin_idx+1]:
#                         end_idx -= 1
#                     else:
#                         begin_idx += 1
#         return res

#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


height = [1,8,6,2,5,4,8,3,7]
res = Solution().maxArea(height)
print(res)