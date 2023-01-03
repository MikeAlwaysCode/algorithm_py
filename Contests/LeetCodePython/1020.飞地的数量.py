#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#
# https://leetcode.cn/problems/number-of-enclaves/description/
#
# algorithms
# Medium (62.11%)
# Likes:    189
# Dislikes: 0
# Total Accepted:    52.6K
# Total Submissions: 84.6K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
# 
# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
# 
# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 的值为 0 或 1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        for dr, dc in self.DIR:
            self.dfs(grid, i + dr, j + dc) 

    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            if grid[i][0] == 1:
                self.dfs(grid, i, 0)
            if grid[i][m-1] == 1:
                self.dfs(grid, i, m-1)
        for j in range(m):
            if grid[0][j] == 1:
                self.dfs(grid, 0, j)
            if grid[n-1][j] == 1:
                self.dfs(grid, n-1, j)
        # ans = 0
        # for i in range(1, n-1):
        #     for j in range(1, m-1):
        #         if grid[i][j] == 1:
        #             ans += 1
        # return ans
        return sum(grid[i][j] for i in range(1, n-1) for j in range(1, m-1))
# @lc code=end

