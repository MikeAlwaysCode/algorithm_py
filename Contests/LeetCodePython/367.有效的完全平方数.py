#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode.cn/problems/valid-perfect-square/description/
#
# algorithms
# Easy (44.85%)
# Likes:    420
# Dislikes: 0
# Total Accepted:    173.9K
# Total Submissions: 387.8K
# Testcase Example:  '16'
#
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 
# 进阶：不要 使用任何内置的库函数，如  sqrt 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = 16
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：num = 14
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r, ans = 0, num, False
        while l <= r:
            mid = (l + r) // 2
            x = mid * mid
            if x == num:
                ans = True
                break
            elif x > num:
                r = mid - 1
            else:
                l = mid + 1
        return ans
# @lc code=end

