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

test = {"headers": ["id", "company", "salary"], "values": [[169, "Apple", 58032], [864, "Apple", 57868], [995, "Dropbox", 61412], [1018, "Facebook", 54162], [610, "Facebook", 53971], [119, "Google", 56281], [1008, "Snapchat", 56604], [106, "Wechat", 52150]]}


gd = {"headers":["id","company","salary"],"values":[[348,"Amazon",54836],[780,"Amazon",54861],[864,"Apple",57868],[169,"Apple",58032],[1938,"Baidu",49984],[1445,"Baidu",50677],[995,"Dropbox",61412],[610,"Facebook",53971],[1018,"Facebook",54162],[119,"Google",56281],[1804,"Linked",59707],[1131,"Linked",59887],[745,"Pinterest",53822],[843,"Pinterest",54620],[1008,"Snapchat",56604],[106,"Wechat",52150]]}


import pandas as pd

test_df = pd.DataFrame(test['values'])
gd_df = pd.DataFrame(gd['values'])

print(test_df.sort_values(by=[1, 2]))
print(gd_df.sort_values(by=[1, 2]))

print()