#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode.cn/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (68.76%)
# Likes:    438
# Dislikes: 0
# Total Accepted:    236.4K
# Total Submissions: 343.9K
# Testcase Example:  '3'
#
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
# 
# 
# 示例 2:
# 
# 
# 输入: rowIndex = 0
# 输出: [1]
# 
# 
# 示例 3:
# 
# 
# 输入: rowIndex = 1
# 输出: [1,1]
# 
# 
# 
# 
# 提示:
# 
# 
# 0 
# 
# 
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(rowIndex) 空间复杂度吗？
# 
#
from typing import List
# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1], [1, 1]]
        if rowIndex <= 1: return res[rowIndex]
        for _ in range(1, rowIndex):
            temp, item = [1], res[-1]
            for i in range(0, len(item)):
                if i+1 < len(item): temp.append(item[i]+item[i+1])
            temp.append(1)
            res.append(temp[:])
        return res[-1]
# @lc code=end

