#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode.cn/problems/maximal-rectangle/description/
#
# algorithms
# Hard (54.34%)
# Likes:    1455
# Dislikes: 0
# Total Accepted:    163.3K
# Total Submissions: 300.4K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = []
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：matrix = [["1"]]
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：matrix = [["0","0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# rows == matrix.length
# cols == matrix[0].length
# 1 <= row, cols <= 200
# matrix[i][j] 为 '0' 或 '1'
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        left = [[0] * m for _ in range(n)]

        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == '0': continue
                if j == 0:
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j - 1] + 1

        ans = 0
        for j in range(m):
            up = [0] * n
            down = [n] * n
            stk = []
            for i in range(n):
                while stk and left[stk[-1]][j] >= left[i][j]:
                    down[stk[-1]] = i
                    stk.pop()
                up[i] = stk[-1] if stk else -1
                stk.append(i)
            ans = max(ans, max((down[i] - up[i] - 1) * left[i][j] for i in range(n)))
        '''
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == '0': continue
                w = left[i][j]
                ans = max(ans, w)
                for k in range(i - 1, -1, -1):
                    if left[k][j] == 0: break
                    w = min(w, left[k][j])
                    ans = max(ans, w * (i - k + 1))
        '''
        return ans
# @lc code=end

