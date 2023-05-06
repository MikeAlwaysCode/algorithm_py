#
# @lc app=leetcode.cn id=2617 lang=python3
#
# [2617] 网格图中最少访问的格子数
#
# https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/description/
#
# algorithms
# Hard (33.27%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 9.6K
# Testcase Example:  '[[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]'
#
# 给你一个下标从 0 开始的 m x n 整数矩阵 grid 。你一开始的位置在 左上角 格子 (0, 0) 。
# 
# 当你在格子 (i, j) 的时候，你可以移动到以下格子之一：
# 
# 
# 满足 j < k <= grid[i][j] + j 的格子 (i, k) （向右移动），或者
# 满足 i < k <= grid[i][j] + i 的格子 (k, j) （向下移动）。
# 
# 
# 请你返回到达 右下角 格子 (m - 1, n - 1) 需要经过的最少移动格子数，如果无法到达右下角格子，请你返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
# 输出：4
# 解释：上图展示了到达右下角格子经过的 4 个格子。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
# 输出：3
# 解释：上图展示了到达右下角格子经过的 3 个格子。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：grid = [[2,1,0],[1,0,0]]
# 输出：-1
# 解释：无法到达右下角格子。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10^5
# 1 <= m * n <= 10^5
# 0 <= grid[i][j] < m * n
# grid[m - 1][n - 1] == 0
# 
# 
#
import heapq
from typing import List


# @lc code=start
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        dist[0][0] = 1
        row, col = [[] for _ in range(m)], [[] for _ in range(n)]

        def update(x: int, y: int) -> int:
            return y if x == -1 or x > y else x
        
        for i in range(m):
            for j in range(n):
                while row[i] and row[i][0][1] + grid[i][row[i][0][1]] < j:
                    heapq.heappop(row[i])
                if row[i]:
                    dist[i][j] = update(dist[i][j], dist[i][row[i][0][1]] + 1)

                while col[j] and col[j][0][1] + grid[col[j][0][1]][j] < i:
                    heapq.heappop(col[j])
                if col[j]:
                    dist[i][j] = update(dist[i][j], dist[col[j][0][1]][j] + 1)

                if dist[i][j] != -1:
                    heapq.heappush(row[i], (dist[i][j], j))
                    heapq.heappush(col[j], (dist[i][j], i))

        return dist[m - 1][n - 1]
# @lc code=end

