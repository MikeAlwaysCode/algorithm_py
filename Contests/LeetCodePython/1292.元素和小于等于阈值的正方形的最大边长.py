#
# @lc app=leetcode.cn id=1292 lang=python3
#
# [1292] 元素和小于等于阈值的正方形的最大边长
#
# https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/
#
# algorithms
# Medium (49.69%)
# Likes:    105
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 20.3K
# Testcase Example:  '[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]\n4'
#
# 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
# 
# 请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# 输出：2
# 解释：总和小于或等于 4 的正方形的最大边长为 2，如图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
# threshold = 1
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 10^4
# 0 <= threshold <= 10^5^ 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]
        
        def getRect(x1, y1, x2, y2) -> int:
            return prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]

        mx = min(n, m)
        ans = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for c in range(ans + 1, mx + 1):
                    if i + c - 1 <= n and j + c - 1 <= m and getRect(i, j, i + c - 1, j + c - 1) <= threshold:
                        ans = max(ans, c)
                        # ans += 1
                    else:
                        break
        return ans
# @lc code=end

