#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#
# https://leetcode.cn/problems/shortest-bridge/description/
#
# algorithms
# Medium (48.03%)
# Likes:    307
# Dislikes: 0
# Total Accepted:    42.1K
# Total Submissions: 85.7K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 给你一个大小为 n x n 的二元矩阵 grid ，其中 1 表示陆地，0 表示水域。
# 
# 岛 是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。grid 中 恰好存在两座岛 。
# 
# 
# 
# 你可以将任意数量的 0 变为 1 ，以使两座岛连接起来，变成 一座岛 。
# 
# 返回必须翻转的 0 的最小数目。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[0,1],[1,0]]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
# 
# 
# 示例 3：
# 
# 
# 输入：grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] 为 0 或 1
# grid 中恰有两个岛
# 
# 
#
from collections import deque
from typing import List
# @lc code=start
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v != 1:
                    continue
                island = []
                grid[i][j] = -1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    island.append((x, y))
                    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = -1
                            q.append((nx, ny))

                step = 0
                q = island
                while True:
                    tmp = q
                    q = []
                    for x, y in tmp:
                        for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                            if 0 <= nx < n and 0 <= ny < n:
                                if grid[nx][ny] == 1:
                                    return step
                                if grid[nx][ny] == 0:
                                    grid[nx][ny] = -1
                                    q.append((nx, ny))
                    step += 1
# @lc code=end

