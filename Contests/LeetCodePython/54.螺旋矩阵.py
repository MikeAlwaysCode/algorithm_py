#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (49.03%)
# Likes:    1171
# Dislikes: 0
# Total Accepted:    293.6K
# Total Submissions: 598.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]

        total = rows * columns
        ans = [0] * total

        r, c, dirIdx = 0, 0, 0

        for i in range(total):
            ans[i] = matrix[r][c]
            visited[r][c] = True

            nr = r + dirs[dirIdx][0]
            nc = c + dirs[dirIdx][1]

            if nr < 0 or nr >= rows or nc < 0 or nc >= columns or visited[nr][nc]:
                dirIdx = (dirIdx + 1) % 4
                nr = r + dirs[dirIdx][0]
                nc = c + dirs[dirIdx][1]
            
            r = nr
            c = nc
        
        return ans
# @lc code=end

