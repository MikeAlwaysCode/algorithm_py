#
# @lc app=leetcode.cn id=6151 lang=python3
#
# [6151] 统计特殊整数
#
# https://leetcode.cn/problems/count-special-integers/description/
#
# algorithms
# Hard (37.40%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 7.1K
# Testcase Example:  '20'
#
# 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。
# 
# 给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 5
# 输出：5
# 解释：1 到 5 所有整数都是特殊整数。
# 
# 
# 示例 3：
# 
# 
# 输入：n = 135
# 输出：110
# 解释：从 1 到 135 总共有 110 个整数是特殊整数。
# 不特殊的部分数字为：22 ，114 和 131 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 2 * 10^9
# 
# 
#
from functools import cache
# @lc code=start
class Solution:
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

