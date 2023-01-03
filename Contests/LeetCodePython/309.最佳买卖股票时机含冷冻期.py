#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (63.89%)
# Likes:    1375
# Dislikes: 0
# Total Accepted:    225.8K
# Total Submissions: 353.1K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: prices = [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 
# 示例 2:
# 
# 
# 输入: prices = [1]
# 输出: 0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp0: 没持有股票，并且没有冷冻期，转移自dp0 & dp2
        # dp1: 持有股票，转移自dp0 & dp1
        # dp2: 没持有股票，刚卖，还处于冷冻期，转移自dp1
        dp0, dp1, dp2 = 0, - prices[0], 0
        for i in range(1, n):
            dp0, dp1, dp2 = max(dp0, dp2), max(dp1, dp0 - prices[i]), dp1 + prices[i]
        return max(dp0, dp2)
# @lc code=end

