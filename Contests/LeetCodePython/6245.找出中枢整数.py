#
# @lc app=leetcode.cn id=6245 lang=python3
#
# [6245] 找出中枢整数
#
# https://leetcode.cn/problems/find-the-pivot-integer/description/
#
# algorithms
# Easy (82.80%)
# Likes:    3
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 6.6K
# Testcase Example:  '8'
#
# 给你一个正整数 n ，找出满足下述条件的 中枢整数 x ：
# 
# 
# 1 和 x 之间的所有元素之和等于 x 和 n 之间所有元素之和。
# 
# 
# 返回中枢整数 x 。如果不存在中枢整数，则返回 -1 。题目保证对于给定的输入，至多存在一个中枢整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 8
# 输出：6
# 解释：6 是中枢整数，因为 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21 。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 解释：1 是中枢整数，因为 1 = 1 。
# 
# 
# 示例 3：
# 
# 
# 输入：n = 4
# 输出：-1
# 解释：可以证明不存在满足题目要求的整数。
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 1000
# 
# 
#
import math
# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        # def cal(l: int, r: int) -> int:
        #     return (l + r) * (r - l + 1) // 2
        # for i in range(n + 1):
        #     if cal(1, i) == cal(i, n):
        #         return i
        # return -1
        k = (n * n + n) // 2
        x = math.isqrt(k)
        if x * x == k:
            return x
        else:
            return -1
# @lc code=end

