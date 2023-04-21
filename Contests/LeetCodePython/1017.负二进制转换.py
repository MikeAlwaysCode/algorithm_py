#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#
# https://leetcode.cn/problems/convert-to-base-2/description/
#
# algorithms
# Medium (57.19%)
# Likes:    82
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 12.5K
# Testcase Example:  '2'
#
# 给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。
# 
# 注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2
# 输出："110"
# 解释：(-2)^2 + (-2)^1 = 2
# 
# 
# 示例 2：
# 
# 
# 输入：n = 3
# 输出："111"
# 解释：(-2)^2 + (-2)^1 + (-2)^0 = 3
# 
# 
# 示例 3：
# 
# 
# 输入：n = 4
# 输出："100"
# 解释：(-2)^2 = 4
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0: return '0'
        if n == 1: return '1'
        if n & 1: return self.baseNeg2((n - 1) // -2) + '1'
        return self.baseNeg2(n // -2) + '0'
        # return str(n) if n in (0, 1) else self.baseNeg2((n - (n & 1)) // -2) + str(n & 1) 
# @lc code=end

