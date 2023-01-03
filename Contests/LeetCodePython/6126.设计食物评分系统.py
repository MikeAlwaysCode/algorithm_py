#
# @lc app=leetcode.cn id=6126 lang=python3
#
# [6126] 设计食物评分系统
#

from typing import *
# @lc code=start
from collections import defaultdict
# from sortedcontainers import SortedList
from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # self.cuisine = defaultdict(SortedList)
        # self.cuisine = dict()
        # self.food = dict()
        self.food = {}
        self.cuisine = defaultdict(SortedSet)
        # n = len(foods)
        # for i in range(n):
            # self.food[foods[i]] = (cuisines[i], ratings[i])

            # if not cuisines[i] in self.cuisine:
            #     self.cuisine[cuisines[i]] = SortedList(key = lambda x:(-x[0],x[1]))

            # self.cuisine[cuisines[i]].add((ratings[i], foods[i]))
        for f, c, r in zip(foods, cuisines, ratings):
            self.food[f] = [r, c]
            self.cuisine[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        # self.cuisine[self.food[food][0]].remove((self.food[food][1], food))
        # self.cuisine[self.food[food][0]].add((newRating, food))
        # self.food[food] = (self.food[food][0], newRating)
        r, c = self.food[food]
        s = self.cuisine[c]
        s.remove((-r, food))  # 移除旧数据
        s.add((-newRating, food))  # 添加新数据
        self.food[food][0] = newRating

    def highestRated(self, cuisine: str) -> str:
        # print(self.food)
        # print(self.cuisine)
        # return self.cuisine[cuisine][0][1]
        return self.cuisine[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @lc code=end

