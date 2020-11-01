#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 7:45 下午
# @Author  : guohua08
# @File    : playground.py
from typing import List

from src.linked_list.ListNode import ListNode
from src.linked_list.LinkedList import LinkedList

#
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        First try: Failed
        Second try: Inspired from discussion: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/719383/Python-O(n)-Sliding-window-Solution-based-on-template
        :param s:
        :param k:
        :return:
        """
        count = 0
        for unique_num in range(1, 27):
            count = max(count, self.helper(s, k, unique_num))
        return count

    def helper(self, s, k, unique_num):
        start = end = cur_unique_num = no_less_thanK_num = count = 0
        # a->z  : 97->122
        char_map = [0] * 128
        while end < len(s):
            if char_map[ord(s[end])] == 0:
                cur_unique_num += 1
            char_map[ord(s[end])] += 1
            if char_map[ord(s[end])] == k:
                no_less_thanK_num += 1
            end += 1

            while cur_unique_num > unique_num:
                if char_map[ord(s[start])] == k:
                    no_less_thanK_num -= 1
                char_map[ord(s[start])] -= 1
                if char_map[ord(s[start])] == 0:
                    cur_unique_num -= 1
                start += 1
            if cur_unique_num == no_less_thanK_num:
                count = max(count, end-start)
        return count

        # import collections
        # count = collections.Counter(s)
        # less_count = dict()
        # for key, value in count.items():
        #     if value<k:
        #         less_count[key] = value
        # for key, value in less_count.items():
        #     del count[key]
        # left, right = 0, len(s)-1
        # # print(right)
        # while len(less_count) != 0:
        #     # print(less_count)
        #     # for letter in [left_letter, right_letter]:
        #     while left<=right and s[left] in less_count:
        #         if less_count[s[left]] == 1:
        #             del less_count[s[left]]
        #         else:
        #             less_count[s[left]] -= 1
        #         left += 1
        #     while right>=left and s[right] in less_count:
        #         # print(right)
        #         if less_count[s[right]] == 1:
        #             del less_count[s[right]]
        #         else:
        #             less_count[s[right]] -= 1
        #         right -= 1
        #     if len(less_count) != 0:
        #         # print(less_count)
        #         left_letter = s[left]
        #         right_letter = s[right]
        #         if count[left_letter]>count[right_letter]:
        #             target_letter = left_letter
        #             left += 1
        #         else:
        #             target_letter = right_letter
        #             right -= 1
        #         if target_letter in less_count:
        #             if less_count[target_letter] == 1:
        #                 del less_count[target_letter]
        #             else:
        #                 less_count[target_letter] -= 1
        #         else:
        #             count[target_letter] -= 1
        #             if count[target_letter] < k:
        #                 if count[target_letter]>=1:
        #                     less_count[target_letter] = count[target_letter]
        #                 del count[target_letter]
        # print(right)
        # print(left)
        # return right-left+1

s = "bbaaacbd"
k = 3
res = Solution().longestSubstring(s, k)
print(res)

# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.