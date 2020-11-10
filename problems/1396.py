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


class UndergroundSystem:

    def __init__(self):
        self.average_time = {}
        self.current_id = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.current_id[id] = {
            "begin_station": stationName
            , "begin_time": t
        }

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        routine = self.current_id[id]["begin_station"] + "_" + stationName
        current_duration = t - self.current_id[id]["begin_time"]
        try:
            self.average_time[routine]
        except:
            self.average_time[routine] = {
                "averate": 0
                , "times": 0
                , "total": 0
            }
        self.average_time[routine]["total"] += current_duration
        self.average_time[routine]["times"] += 1
        self.average_time[routine]["averate"] = self.average_time[routine]["total"]/self.average_time[routine]["times"]
        del self.current_id[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        routine = startStation + "_" + endStation
        return self.average_time[routine]["averate"]


# ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
# [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
# Output
# [null,null,null,null,null,null,null,14.00000,12.00000,null,12.00000,null,12.00000]
# Expected
# [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


#
# s = "aaabb"
# k = 3
# res = Solution().longestSubstring(s, k)
# print(res)
#
#
#
# Input
# ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
# [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
#
# Output
# [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
#
# Explanation
# UndergroundSystem undergroundSystem = new UndergroundSystem();
# undergroundSystem.checkIn(45, "Leyton", 3);
# undergroundSystem.checkIn(32, "Paradise", 8);
# undergroundSystem.checkIn(27, "Leyton", 10);
# undergroundSystem.checkOut(45, "Waterloo", 15);
# undergroundSystem.checkOut(27, "Waterloo", 20);
# undergroundSystem.checkOut(32, "Cambridge", 22);
# undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
# undergroundSystem.checkIn(10, "Leyton", 24);
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000
# undergroundSystem.checkOut(10, "Waterloo", 38);
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.00000