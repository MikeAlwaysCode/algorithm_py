#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# https://leetcode.cn/problems/number-of-digit-one/description/
#
# algorithms
# Hard (49.03%)
# Likes:    523
# Dislikes: 0
# Total Accepted:    55.7K
# Total Submissions: 113.4K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 13
# 输出：6
# 
# 
# 示例 2：
# 
# 
# 输入：n = 0
# 输出：0
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
from functools import cache


# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i: int, cnt: int, isLimit: bool):
            if i == len(s):
                return cnt
            res = 0
            up = int(s[i]) if isLimit else 9
            for d in range(up+1):
                res += f(i+1, cnt + (d == 1), isLimit and d == up)
            return res
        return f(0, 0, True)
# @lc code=end

