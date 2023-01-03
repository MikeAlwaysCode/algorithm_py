#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#
# https://leetcode.cn/problems/count-negative-numbers-in-a-sorted-matrix/description/
#
# algorithms
# Easy (74.53%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    45.8K
# Total Submissions: 61.4K
# Testcase Example:  '[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]'
#
# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 请你统计并返回 grid 中 负数 的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# 输出：8
# 解释：矩阵中共有 8 个负数。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[3,2],[1,0]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
# 
# 
# 
# 
# 进阶：你可以设计一个时间复杂度为 O(n + m) 的解决方案吗？
# 
#
from typing import List
# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        end = m
        for i in range(n):
            while end > 0 and grid[i][end-1] < 0:
                end -= 1
            ans += m - end
        '''
        for i in range(n):
            l, r = 0, end
            while l < r:
                mid = l + r >> 1
                if grid[i][mid] >= 0:
                    l = mid + 1
                else:
                    r = mid
            end = r
            # print(l, r)
            ans += m - end
        '''
        return ans
# @lc code=end

