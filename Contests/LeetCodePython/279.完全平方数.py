#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode.cn/problems/perfect-squares/description/
#
# algorithms
# Medium (65.55%)
# Likes:    1481
# Dislikes: 0
# Total Accepted:    331.3K
# Total Submissions: 505.3K
# Testcase Example:  '12'
#
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11
# 不是。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4
# 
# 示例 2：
# 
# 
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^4
# 
# 
#
from math import sqrt
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        if (self.isPerfectSquare(n)):
            return 1
        
        if (self.checkAnswer4(n)):
            return 4
        
        for i in range(1, int(sqrt(n))+1):
            j = n - i * i
            if (self.isPerfectSquare(j)):
                return 2
        
        return 3

    def isPerfectSquare(self, x: int) -> bool:
        y = int(sqrt(x))
        return y * y == x
        
    # 是否能表示为 4^k*(8m+7)
    def checkAnswer4(self, x: int) -> bool:
        while x % 4 == 0:
            x /= 4
        return x % 8 == 7
# @lc code=end

