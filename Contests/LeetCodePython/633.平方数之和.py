#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# https://leetcode.cn/problems/sum-of-square-numbers/description/
#
# algorithms
# Medium (38.56%)
# Likes:    403
# Dislikes: 0
# Total Accepted:    123.6K
# Total Submissions: 320.6K
# Testcase Example:  '5'
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
# 
# 
# 示例 2：
# 
# 
# 输入：c = 3
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= c <= 2^31 - 1
# 
# 
#
import math
# @lc code=start


class Solution:
    def judgeSquareSum(self, n: int) -> bool:
        if n % 4 == 3:
            return False

        l = 0
        r = math.isqrt(n)
        while l <= r:
            tot = l * l + r * r
            if tot == n:
                return True
            elif tot < n:
                l += 1
            else:
                r -= 1
        return False
# @lc code=end

