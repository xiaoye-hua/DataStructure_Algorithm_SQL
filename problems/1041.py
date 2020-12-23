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
    def isRobotBounded(self, instructions: str) -> bool:
        """
        triky part: valid if not face north or back to the start point
        inspired from discussion: https://leetcode.com/problems/robot-bounded-in-circle/discuss/374510/Readable-Python-3-solution-(easy)
        :param instructions:
        :return:
        """
        # N 0; W 1; S 2; E 3
        direction = 0
        x, y = 0, 0
        for ele in instructions:
            if ele == "G":
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x -= 1
                elif direction == 2:
                    y -= 1
                else:
                    x += 1
            elif ele == "L":
                direction += 1
            else:
                direction -= 1
            if direction == 4:
                direction = 0
            if direction == -1:
                direction = 3
        return (x==0 and y==0) or direction!=0

# Input: "GGLLGG"
# Output: true
# Explanation:
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:
#
# Input: "GG"
# Output: false
# Explanation:
# The robot moves north indefinitely.

instructions = "GG"
res = Solution().isRobotBounded(instructions)
print(res)