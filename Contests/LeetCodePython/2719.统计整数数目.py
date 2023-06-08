#
# @lc app=leetcode.cn id=2719 lang=python3
#
# [2719] 统计整数数目
#
# https://leetcode.cn/problems/count-of-integers/description/
#
# algorithms
# Hard (45.75%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 4.4K
# Testcase Example:  '"1"\n"12"\n1\n8'
#
# 给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x
# 满足以下条件，我们称它是一个好整数：
# 
# 
# num1 <= x <= num2
# min_sum <= digit_sum(x) <= max_sum.
# 
# 
# 请你返回好整数的数目。答案可能很大，请返回答案对 10^9 + 7 取余后的结果。
# 
# 注意，digit_sum(x) 表示 x 各位数字之和。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num1 = "1", num2 = "12", min_num = 1, max_num = 8
# 输出：11
# 解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11 。
# 
# 
# 示例 2：
# 
# 
# 输入：num1 = "1", num2 = "5", min_num = 1, max_num = 5
# 输出：5
# 解释：数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num1 <= num2 <= 10^22
# 1 <= min_sum <= max_sum <= 400
# 
# 
#
from functools import cache


# @lc code=start
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(num2)
        if len(num1) < n:
            num1 = "0" * (n - len(num1)) + num1
            
        @cache
        def f(i: int, s: int, isUpLimit: bool, isDownLimit: bool):
            if i == n:
                return int(min_sum <= s <= max_sum)
            if s > max_sum: return 0

            res = 0
            up = int(num2[i]) if isUpLimit else 9
            down = int(num1[i]) if isDownLimit else 0
            for d in range(down, up + 1):
                res = (res + f(i + 1, s + d, isUpLimit and d == up, isDownLimit and d == down)) % MOD

            return res
        
        return f(0, 0, True, True) % MOD
# @lc code=end

