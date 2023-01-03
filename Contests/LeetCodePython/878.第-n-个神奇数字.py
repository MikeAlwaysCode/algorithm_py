#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#
# https://leetcode.cn/problems/nth-magical-number/description/
#
# algorithms
# Hard (34.03%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 24.7K
# Testcase Example:  '1\n2\n3'
#
# 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
# 
# 给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 10^9 + 7 取模 后的值。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 1, a = 2, b = 3
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：n = 4, a = 2, b = 3
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^9
# 2 <= a, b <= 4 * 10^4
# 
# 
# 
# 
#
import math


# @lc code=start
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        if a == b:
            return (a * n) % MOD
        
        c = math.lcm(a, b)
        l, r = min(a, b), n * min(a, b)
        while l < r:
            mid = l + r >> 1
            cnt = mid // a + mid // b - mid // c
            if cnt >= n:
                r = mid
            else:
                l = mid + 1
        return r % MOD
        # while l <= r:
        #     mid = l + r + 1 >> 1
        #     cnt = mid // a + mid // b - mid // c
        #     if cnt >= n:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return l % MOD
# @lc code=end

