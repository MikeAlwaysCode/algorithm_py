#
# @lc app=leetcode.cn id=1253 lang=python3
#
# [1253] 重构 2 行二进制矩阵
#
# https://leetcode.cn/problems/reconstruct-a-2-row-binary-matrix/description/
#
# algorithms
# Medium (40.60%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 29.2K
# Testcase Example:  '2\n1\n[1,1,1]'
#
# 给你一个 2 行 n 列的二进制数组：
# 
# 
# 矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
# 第 0 行的元素之和为 upper。
# 第 1 行的元素之和为 lower。
# 第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。
# 
# 
# 你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。
# 
# 如果有多个不同的答案，那么任意一个都可以通过本题。
# 
# 如果不存在符合要求的答案，就请返回一个空的二维数组。
# 
# 
# 
# 示例 1：
# 
# 输入：upper = 2, lower = 1, colsum = [1,1,1]
# 输出：[[1,1,0],[0,0,1]]
# 解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。
# 
# 
# 示例 2：
# 
# 输入：upper = 2, lower = 3, colsum = [2,2,1,1]
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# 输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= colsum.length <= 10^5
# 0 <= upper, lower <= colsum.length
# 0 <= colsum[i] <= 2
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        s = two = 0
        for c in colsum:
            if c == 2:
                two += 1
            s += c
        if s != upper + lower or min(upper, lower) < two: return []
        upper -= two
        lower -= two
        ans = [[0] * n for _ in range(2)]
        for i in range(n):
            if colsum[i] == 2:
                ans[0][i] = ans[1][i] = 1
            elif colsum[i] == 1:
                if upper:
                    ans[0][i] = 1
                    upper -= 1
                else:
                    ans[1][i] = 1
        return ans
# @lc code=end

