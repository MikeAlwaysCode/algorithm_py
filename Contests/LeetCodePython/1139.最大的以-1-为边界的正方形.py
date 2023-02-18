#
# @lc app=leetcode.cn id=1139 lang=python3
#
# [1139] 最大的以 1 为边界的正方形
#
# https://leetcode.cn/problems/largest-1-bordered-square/description/
#
# algorithms
# Medium (49.52%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    14.6K
# Total Submissions: 28.7K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回
# 0。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
# 
# 
# 示例 2：
# 
# 输入：grid = [[1,1,0,0]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] 为 0 或 1
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        left = [[0] * (m + 1) for _ in range(n + 1)]
        up = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    left[i + 1][j + 1] = left[i + 1][j] + 1
                    up[i + 1][j + 1] = up[i][j + 1] + 1

                    l = min(left[i + 1][j + 1], up[i + 1][j + 1])
                    while left[i - l + 2][j + 1] < l or up[i + 1][j - l + 2] < l:
                        l -= 1
                    ans = max(ans, l)
        return ans ** 2
# @lc code=end

