#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#
# https://leetcode.cn/problems/count-sub-islands/description/
#
# algorithms
# Medium (66.88%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    20.7K
# Total Submissions: 31K
# Testcase Example:  '[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]'
#
# 给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向
# （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。
# 
# 如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1
# 中同一个岛屿完全包含，那么我们称 grid2 中的这个岛屿为 子岛屿 。
# 
# 请你返回 grid2 中 子岛屿 的 数目 。
# 
# 
# 
# 示例 1：
# 
# 输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# 输出：3
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
# 
# 
# 示例 2：
# 
# 输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# 输出：2 
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] 和 grid2[i][j] 都要么是 0 要么是 1 。
# 
# 
#
from collections import deque
from typing import List
# @lc code=start
class Solution:
    DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
    
    def dfs(self, grid1, grid2, i, j) -> bool:
        if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
            return True
            
        grid2[i][j] = 0
        
        chk = True
        if grid1[i][j] == 0:
            chk = False
        for dr, dc in self.DIR:
            chk = self.dfs(grid1, grid2, i + dr, j + dc) and chk
        return chk

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def bfs(sx: int, sy: int) -> int:
            q = deque([(sx, sy)])
            grid2[sx][sy] = 0
            # 判断岛屿包含的每一个格子是否都在 grid1 中出现了
            check = (grid1[sx][sy] == 1)
            while q:
                x, y = q.popleft()
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                        q.append((nx, ny))
                        grid2[nx][ny] = 0
                        if grid1[nx][ny] != 1:
                            check = False
            
            return int(check)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    ans += bfs(i, j)
        return ans
        '''
        n, m = len(grid2), len(grid2[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    ans += self.dfs(grid1, grid2, i, j)
        return ans
        '''
# @lc code=end

