#
# @lc app=leetcode.cn id=6203 lang=python3
#
# [6203] 矩阵中和能被 K 整除的路径
#
# https://leetcode.cn/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description/
#
# algorithms
# Hard (45.15%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 5.5K
# Testcase Example:  '[[5,2,4],[3,0,5],[0,7,2]]\n3'
#
# 给你一个下标从 0 开始的 m x n 整数矩阵 grid 和一个整数 k 。你从起点 (0, 0) 出发，每一步只能往 下 或者往 右 ，你想要到达终点
# (m - 1, n - 1) 。
# 
# 请你返回路径和能被 k 整除的路径数目，由于答案可能很大，返回答案对 10^9 + 7 取余 的结果。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
# 输出：2
# 解释：有两条路径满足路径上元素的和能被 k 整除。
# 第一条路径为上图中用红色标注的路径，和为 5 + 2 + 4 + 5 + 2 = 18 ，能被 3 整除。
# 第二条路径为上图中用蓝色标注的路径，和为 5 + 3 + 0 + 5 + 2 = 15 ，能被 3 整除。
# 
# 
# 示例 2：
# 
# 输入：grid = [[0,0]], k = 5
# 输出：1
# 解释：红色标注的路径和为 0 + 0 = 0 ，能被 5 整除。
# 
# 
# 示例 3：
# 
# 输入：grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
# 输出：10
# 解释：每个数字都能被 1 整除，所以每一条路径的和都能被 k 整除。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 5 * 10^4
# 1 <= m * n <= 5 * 10^4
# 0 <= grid[i][j] <= 100
# 1 <= k <= 50
# 
# 
#
from functools import cache
from typing import List
# @lc code=start
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7

        n = len(grid)
        m = len(grid[0])

        '''
        @cache
        def dfs(i: int, j: int, v: int) -> int:
            if i < 0 or j < 0:
                return 0
            v = (v + grid[i][j]) % k
            if i == j == 0:
                return int(v == 0)
            return (dfs(i - 1, j, v) + dfs(i, j - 1, v)) % MOD
        
        ans = dfs(n - 1, m - 1, 0)
        dfs.cache_clear()
        return ans
        '''
        dp = [[[0] * k for _ in range(m + 1)] for _ in range(n + 1)]
        dp[1][1][grid[0][0]%k] = 1

        for i in range(n):
            for j in range(m):
                for l in range(k):
                    cur = (l + grid[i][j]) % k
                    dp[i+1][j+1][cur] += dp[i][j+1][l] + dp[i+1][j][l]
                    dp[i+1][j+1][cur] %= MOD
        # print(dp)
        return dp[n][m][0]
# @lc code=end

