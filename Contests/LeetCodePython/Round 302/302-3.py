#
# @lc app=leetcode.cn id=6130 lang=python3
#
# [6130] 设计数字容器系统
#

from typing import *
# @lc code=start
from collections import defaultdict
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # self.cuisine = defaultdict(SortedList)
        self.cuisine = dict()
        self.food = dict()
        n= len(foods)
        for i in range(n):
            self.food[foods[i]] = (cuisines[i], ratings[i])

            if not cuisines[i] in self.cuisine:
                self.cuisine[cuisines[i]] = SortedList(key = lambda x:(-x[0],x[1]))

            self.cuisine[cuisines[i]].add((ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.cuisine[self.food[food][0]].remove((self.food[food][1], food))
        self.cuisine[self.food[food][0]].add((newRating, food))
        self.food[food] = (self.food[food][0], newRating)


    def highestRated(self, cuisine: str) -> str:
        # print(self.food)
        # print(self.cuisine)
        return self.cuisine[cuisine][0][1]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end

# ["FoodRatings","changeRating","highestRated","highestRated","highestRated"]
# [[["cpctxzh","bryvgjqmj","wedqhqrmyc","ee","lafzximxh","lojzxfel","flhs"],
# ["wbhdgqphq","wbhdgqphq","mxxajogm","wbhdgqphq","wbhdgqphq","mxxajogm","mxxajogm"],
# [15,5,7,16,16,10,13]],
# ["lojzxfel",1],["mxxajogm"],["wbhdgqphq"],["mxxajogm"]]
foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]
sol = FoodRatings(foods,cuisines,ratings)
# sol.__init__(foods,cuisines,ratings)
print(sol.highestRated("korean"))
print(sol.highestRated("japanese"))
sol.changeRating("sushi", 16)
print(sol.highestRated("japanese"))
sol.changeRating("ramen", 16)
print(sol.highestRated("japanese"))
