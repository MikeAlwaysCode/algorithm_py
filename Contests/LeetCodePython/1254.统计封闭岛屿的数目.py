#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#
# https://leetcode.cn/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (62.23%)
# Likes:    167
# Dislikes: 0
# Total Accepted:    36.8K
# Total Submissions: 59.2K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。
# 
# 请返回 封闭岛屿 的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
# 
# 示例 2：
# 
# 
# 
# 
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：grid = [[1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# ⁠            [1,1,1,1,1,1,1]]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
    
    def dfs(self, grid, i, j) -> bool:
        if (i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1) and grid[i][j] == 0:
            return False
        if grid[i][j] == 1:
            return True
        grid[i][j] = 1
        # return all(self.dfs(grid, i + dr, j + dc) for dr, dc in self.DIR) # 短路AND
        chk = True
        for dr, dc in self.DIR:
            chk = self.dfs(grid, i + dr, j + dc) and chk
        return chk

    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0:
                    ans += self.dfs(grid, i, j)
        return ans
# @lc code=end

