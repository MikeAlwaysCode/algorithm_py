#
# @lc app=leetcode.cn id=2427 lang=python3
#
# [2427] 公因子的数目
#
# https://leetcode.cn/problems/number-of-common-factors/description/
#
# algorithms
# Easy (81.19%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 19.2K
# Testcase Example:  '12\n6'
#
# 给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。
# 
# 如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。
# 
# 
# 
# 示例 1：
# 
# 输入：a = 12, b = 6
# 输出：4
# 解释：12 和 6 的公因子是 1、2、3、6 。
# 
# 
# 示例 2：
# 
# 输入：a = 25, b = 30
# 输出：2
# 解释：25 和 30 的公因子是 1、5 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= a, b <= 1000
# 
# 
#
import math


# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = math.gcd(a, b)
        ans = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                ans += 1
                if i * i != g:
                    ans += 1
            i += 1
        return ans
# @lc code=end

