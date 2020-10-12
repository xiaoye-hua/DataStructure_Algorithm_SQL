#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        First try: DFS, ETL...  --> DP with DFS --> not finished
        Second try: DP with WFS (level order travesal of tree) inspired from discussion https://leetcode.com/problems/target-sum/discuss/97343/Python-DP
        :param nums:
        :param S:
        :return:
        """
        if not nums:
            return 0
        dic = {nums[0]:1, -nums[0]:1} if nums[0] != 0 else {nums[0]: 2}
        for idx in range(1, len(nums)):
            new_dic = {}
            for current_value in dic:
                new_dic[current_value + nums[idx]] = new_dic.get(current_value + nums[idx], 0) + dic.get(current_value, 0)
                new_dic[current_value - nums[idx]] = new_dic.get(current_value - nums[idx], 0) + dic.get(current_value, 0)
            dic = new_dic
        return dic.get(S, 0)

    #     # DP with DFS  --> failed
    #     self.res = 0
    #     self.target = S
    #     self.length = len(nums)
    #     self.nums = nums
    #     # self.cache = {}
    #     self.dfs(0, 0, S)
    #     return self.res
    #
    # def dfs(self, idx, current_sum):
    #     if idx == self.length:
    #         if current_sum == self.target:
    #             self.res += 1
    #     else:
    #         self.dfs(idx + 1, current_sum + self.nums[idx])
    #         self.dfs(idx + 1, current_sum - self.nums[idx])



nums = [1, 1, 1, 1, 1]
S = 3
res = Solution().findTargetSumWays(nums, S)
print(res)