#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#
# https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/description/
#
# algorithms
# Easy (49.78%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    38.4K
# Total Submissions: 77.2K
# Testcase Example:  '3\n7'
#
# 给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：low = 3, high = 7
# 输出：3
# 解释：3 到 7 之间奇数数字为 [3,5,7] 。
# 
# 示例 2：
# 
# 输入：low = 8, high = 10
# 输出：1
# 解释：8 到 10 之间奇数数字为 [9] 。
# 
# 
# 
# 提示：
# 
# 
# 0 <= low <= high <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1 - (high & 1)) // 2 + (high & 1)
# @lc code=end

