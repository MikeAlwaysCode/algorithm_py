#
# @lc app=leetcode.cn id=1886 lang=python3
#
# [1886] 判断矩阵经轮转后是否一致
#
# https://leetcode.cn/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/
#
# algorithms
# Easy (59.08%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    9.8K
# Total Submissions: 16.5K
# Testcase Example:  '[[0,1],[1,0]]\n[[1,0],[0,1]]'
#
# 给你两个大小为 n x n 的二进制矩阵 mat 和 target 。现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，如果能够使 mat 与
# target 一致，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# 输出：true
# 解释：顺时针轮转 90 度一次可以使 mat 和 target 一致。
# 
# 
# 示例 2：
# 
# 
# 输入：mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# 输出：false
# 解释：无法通过轮转矩阵中的元素使 equal 与 target 一致。
# 
# 
# 示例 3：
# 
# 
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# 输出：true
# 解释：顺时针轮转 90 度两次可以使 mat 和 target 一致。
# 
# 
# 
# 
# 提示：
# 
# 
# n == mat.length == target.length
# n == mat[i].length == target[i].length
# 1 
# mat[i][j] 和 target[i][j] 不是 0 就是 1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        chk = [True] * 4
        for i in range(n):
            for j in range(n):
                ni, nj = i, j
                for k in range(4):
                    if chk[k] and mat[i][j] != target[ni][nj]:
                        chk[k] = False
                    ni, nj = nj, n - 1 - ni
                if not any(chk): break
        return any(chk)
# @lc code=end

