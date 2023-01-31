#
# @lc app=leetcode.cn id=2319 lang=python3
#
# [2319] 判断矩阵是否是一个 X 矩阵
#
# https://leetcode.cn/problems/check-if-matrix-is-x-matrix/description/
#
# algorithms
# Easy (73.26%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    15.7K
# Total Submissions: 20.7K
# Testcase Example:  '[[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]'
#
# 如果一个正方形矩阵满足下述 全部 条件，则称之为一个 X 矩阵 ：
# 
# 
# 矩阵对角线上的所有元素都 不是 0
# 矩阵中所有其他元素都是 0
# 
# 
# 给你一个大小为 n x n 的二维整数数组 grid ，表示一个正方形矩阵。如果 grid 是一个 X 矩阵 ，返回 true ；否则，返回 false
# 。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
# 输出：true
# 解释：矩阵如上图所示。
# X 矩阵应该满足：绿色元素（对角线上）都不是 0 ，红色元素都是 0 。
# 因此，grid 是一个 X 矩阵。
# 
# 
# 示例 2：
# 
# 输入：grid = [[5,7,0],[0,3,1],[0,5,0]]
# 输出：false
# 解释：矩阵如上图所示。
# X 矩阵应该满足：绿色元素（对角线上）都不是 0 ，红色元素都是 0 。
# 因此，grid 不是一个 X 矩阵。
# 
# 
# 
# 
# 提示：
# 
# 
# n == grid.length == grid[i].length
# 3 <= n <= 100
# 0 <= grid[i][j] <= 10^5
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i, row in enumerate(grid):
            for j, d in enumerate(row):
                # if (i == j or i == n - 1 - j or n - 1 - i == j or n - 1 - i == n - 1 - j) != (d > 0):
                if (i == j or i + j == n - 1) != (d > 0):
                    return False
        return True
# @lc code=end

