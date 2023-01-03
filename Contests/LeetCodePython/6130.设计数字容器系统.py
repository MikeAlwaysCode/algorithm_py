#
# @lc app=leetcode.cn id=6130 lang=python3
#
# [6130] 设计数字容器系统
#

# @lc code=start
from collections import defaultdict
# from unittest.util import sorted_list_difference
from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.nums = defaultdict(SortedList)
        self.id = dict()


    def change(self, index: int, number: int) -> None:
        if index in self.id:
            preNum = self.id[index]
            self.nums[preNum].remove(index)
        
        self.id[index] = number
        
        self.nums[number].add(index)
                

    def find(self, number: int) -> int:
        if self.nums[number]:
            return self.nums[number][0]
        else:
            return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end

