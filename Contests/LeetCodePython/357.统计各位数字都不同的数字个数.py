#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 统计各位数字都不同的数字个数
#
# https://leetcode.cn/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (60.45%)
# Likes:    330
# Dislikes: 0
# Total Accepted:    68.6K
# Total Submissions: 113.4K
# Testcase Example:  '2'
#
# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10^n^ 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2
# 输出：91
# 解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。 
# 
# 
# 示例 2：
# 
# 
# 输入：n = 0
# 输出：1
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        ans, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            ans += cur
        return ans
# @lc code=end

