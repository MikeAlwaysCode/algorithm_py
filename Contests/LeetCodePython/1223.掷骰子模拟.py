#
# @lc app=leetcode.cn id=1223 lang=python3
#
# [1223] 掷骰子模拟
#
# https://leetcode.cn/problems/dice-roll-simulation/description/
#
# algorithms
# Hard (49.64%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    8.1K
# Total Submissions: 14K
# Testcase Example:  '2\n[1,1,2,2,2,3]'
#
# 有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。
# 
# 不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。
# 
# 现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。
# 
# 假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 2, rollMax = [1,1,2,2,2,3]
# 输出：34
# 解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2
# 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。
# 
# 
# 示例 2：
# 
# 输入：n = 2, rollMax = [1,1,1,1,1,1]
# 输出：30
# 
# 
# 示例 3：
# 
# 输入：n = 3, rollMax = [1,1,1,2,2,3]
# 输出：181
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 5000
# rollMax.length == 6
# 1 <= rollMax[i] <= 15
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        m = 6
        dp = [[0] * m for _ in range(n)]
        dp[0] = [1] * m
        s = [0] * n
        s[0] = m
        for i in range(1, n):
            for j, mx in enumerate(rollMax):
                res = s[i - 1]
                if i > mx:
                    res -= s[i - mx - 1] - dp[i - mx - 1][j]
                elif i == mx:
                    res -= 1
                dp[i][j] = res % MOD
            s[i] = sum(dp[i]) % MOD
        return s[-1]
# @lc code=end

