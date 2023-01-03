#
# @lc app=leetcode.cn id=1012 lang=python3
#
# [1012] 至少有 1 位重复的数字
#
# https://leetcode.cn/problems/numbers-with-repeated-digits/description/
#
# algorithms
# Hard (37.86%)
# Likes:    113
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 11.8K
# Testcase Example:  '20'
#
# 给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 20
# 输出：1
# 解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 100
# 输出：10
# 解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。
# 
# 
# 示例 3：
# 
# 
# 输入：n = 1000
# 输出：262
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^9
# 
# 
#
from functools import cache
# @lc code=start
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        return n - self.countSpecialNumbers(n)
    def countSpecialNumbers(self, n: int) -> int:
        # 数位DP
        s = str(n)

        # i: 第几位
        # mask: 二进制位数为1则代表前面填了相应数字
        # isLimit：前面数字是n对应位上，或者第1位，则当前数字上限为s[i]，否则为9
        # isNum：前面是否有数字，有则当前可以填0，否则可以跳过当前位，或从1开始填
        @cache
        def f(i: int, mask: int, isLimit: bool, isNum: bool):
            if i == len(s):
                # 前面填了数字，当前为1个有效结果
                return int(isNum)
            res = 0
            if not isNum:
                # 可继续跳过
                res = f(i+1, mask, False, False)
            up = int(s[i]) if isLimit else 9
            for d in range(1-int(isNum), up+1):
                if not mask >> d & 1:   # mask前面没有d
                    res += f(i+1, mask|(1<<d), isLimit and d == up, True)
            return res
        return f(0, 0, True, False)
# @lc code=end

