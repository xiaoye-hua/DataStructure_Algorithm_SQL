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


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        '''
        hour size <= 3 (7)
        min size <= 5 (31)
        '''
        self.all_hour = [1, 2, 4, 8]
        self.all_min = [1, 2, 4, 8, 16, 32]
        self.hour_boundary = 11
        self.min_boundary = 59
        result = []
        for hour_len in range(0, min(3, turnedOn) + 1):
            min_len = turnedOn - hour_len
            if min_len > 5:
                continue
            self.hour_lst = []
            # print(self.all_hour)
            # print(hour_len)
            self.get_number(0, self.all_hour, hour_len, True)
            self.min_lst = []
            # self.get_min([], self.all_min, min_len)
            self.get_number(0, self.all_min, min_len, False)
            for hour in self.hour_lst:
                for minute in self.min_lst:
                    if len(minute) == 1:
                        minute = '0' + minute
                    result.append(
                        hour + ':' + minute
                    )
        return result

    def get_number(self, current_sum, remain_lst, left_len, hour):
        if left_len == 0:
            if current_sum != 0:
                if hour:
                    self.hour_lst.append(str(sum(current_sum)))
                else:
                    self.min_lst.append(str(sum(current_sum)))
            else:
                if hour:
                    self.hour_lst.append('0')
                else:
                    self.min_lst.append('00')
            return
            # print(remain_lst)
        for ele in remain_lst:
            if hour and current_sum+ele>self.hour_boundary:
                continue
            elif not hour and current_sum+ele>self.min_boundary:
                continue
            new_remain = copy.deepcopy(remain_lst)
            new_remain.remove(ele)
            # current_lst.appned(ele)
            self.get_number(current_sum + ele, new_remain, left_len - 1, hour)

