#
# @lc app=leetcode.cn id=1825 lang=python3
#
# [1825] 求出 MK 平均值
#
# https://leetcode.cn/problems/finding-mk-average/description/
#
# algorithms
# Hard (29.81%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 11.5K
# Testcase Example:  '["MKAverage","addElement","addElement","calculateMKAverage","addElement","calculateMKAverage","addElement","addElement","addElement","calculateMKAverage"]\n[[3,1],[3],[1],[],[10],[],[5],[5],[5],[]]'
#
# 给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。
# 
# MK 平均值 按照如下步骤计算：
# 
# 
# 如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。
# 从这个容器中删除最小的 k 个数和最大的 k 个数。
# 计算剩余元素的平均值，并 向下取整到最近的整数 。
# 
# 
# 请你实现 MKAverage 类：
# 
# 
# MKAverage(int m, int k) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。
# void addElement(int num) 往数据流中插入一个新的元素 num 。
# int calculateMKAverage() 对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement",
# "calculateMKAverage", "addElement", "addElement", "addElement",
# "calculateMKAverage"]
# [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
# 输出：
# [null, null, null, -1, null, 3, null, null, null, 5]
# 
# 解释：
# MKAverage obj = new MKAverage(3, 1); 
# obj.addElement(3);        // 当前元素为 [3]
# obj.addElement(1);        // 当前元素为 [3,1]
# obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
# obj.addElement(10);       // 当前元素为 [3,1,10]
# obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10]
# ⁠                         // 删除最小以及最大的 1 个元素后，容器为 [3]
# ⁠                         // [3] 的平均值等于 3/1 = 3 ，故返回 3
# obj.addElement(5);        // 当前元素为 [3,1,10,5]
# obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
# obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
# obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5]
# ⁠                         // 删除最小以及最大的 1 个元素后，容器为 [5]
# ⁠                         // [5] 的平均值等于 5/1 = 5 ，故返回 5
# 
# 
# 
# 
# 提示：
# 
# 
# 3 
# 1 
# 1 
# addElement 与 calculateMKAverage 总操作次数不超过 10^5 次。
# 
# 
#

# @lc code=start
from collections import deque
from sortedcontainers import SortedList


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.s = 0
        self.q = deque()
        self.lo = SortedList()
        self.mid = SortedList()
        self.hi = SortedList()

    def addElement(self, num: int) -> None:
        if not self.lo or num <= self.lo[-1]:
            self.lo.add(num)
        elif not self.hi or num >= self.hi[0]:
            self.hi.add(num)
        else:
            self.mid.add(num)
            self.s += num
        self.q.append(num)
        if len(self.q) > self.m:
            x = self.q.popleft()
            if x in self.lo:
                self.lo.remove(x)
            elif x in self.hi:
                self.hi.remove(x)
            else:
                self.mid.remove(x)
                self.s -= x
        while len(self.lo) > self.k:
            x = self.lo.pop()
            self.mid.add(x)
            self.s += x
        while len(self.hi) > self.k:
            x = self.hi.pop(0)
            self.mid.add(x)
            self.s += x
        while len(self.lo) < self.k and self.mid:
            x = self.mid.pop(0)
            self.lo.add(x)
            self.s -= x
        while len(self.hi) < self.k and self.mid:
            x = self.mid.pop()
            self.hi.add(x)
            self.s -= x

    def calculateMKAverage(self) -> int:
        return -1 if len(self.q) < self.m else self.s // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
# @lc code=end

