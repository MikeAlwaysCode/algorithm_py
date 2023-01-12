#
# @lc app=leetcode.cn id=1314 lang=python3
#
# [1314] 矩阵区域和
#
# https://leetcode.cn/problems/matrix-block-sum/description/
#
# algorithms
# Medium (75.65%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    21.8K
# Total Submissions: 28.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素
# mat[r][c] 的和： 
# 
# 
# i - k 
# j - k  且
# (r, c) 在矩阵内。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
# 
# 
# 示例 2：
# 
# 
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 
# 1 
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]
        
        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return P[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + k + 1, j + k + 1) - get(i - k, j + k + 1) - get(i + k + 1, j - k) + get(i - k, j - k);

        return ans
# @lc code=end

