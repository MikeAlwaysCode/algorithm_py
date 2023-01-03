#
# @lc app=leetcode.cn id=6187 lang=python3
#
# [6187] 完成所有交易的初始最少钱数
#
# https://leetcode.cn/problems/minimum-money-required-before-transactions/description/
#
# algorithms
# Hard (36.52%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 3.4K
# Testcase Example:  '[[2,1],[5,0],[4,2]]'
#
# 给你一个下标从 0 开始的二维整数数组 transactions，其中transactions[i] = [costi, cashbacki] 。
# 
# 数组描述了若干笔交易。其中每笔交易必须以 某种顺序 恰好完成一次。在任意一个时刻，你有一定数目的钱 money ，为了完成交易 i ，money >=
# costi 这个条件必须为真。执行交易后，你的钱数 money 变成 money - costi + cashbacki 。
# 
# 请你返回 任意一种 交易顺序下，你都能完成所有交易的最少钱数 money 是多少。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：transactions = [[2,1],[5,0],[4,2]]
# 输出：10
# 解释：
# 刚开始 money = 10 ，交易可以以任意顺序进行。
# 可以证明如果 money < 10 ，那么某些交易无法进行。
# 
# 
# 示例 2：
# 
# 
# 输入：transactions = [[3,0],[0,3]]
# 输出：3
# 解释：
# - 如果交易执行的顺序是 [[3,0],[0,3]] ，完成所有交易需要的最少钱数是 3 。
# - 如果交易执行的顺序是 [[0,3],[3,0]] ，完成所有交易需要的最少钱数是 0 。
# 所以，刚开始钱数为 3 ，任意顺序下交易都可以全部完成。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= transactions.length <= 10^5
# transactions[i].length == 2
# 0 <= costi, cashbacki <= 10^9
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        tot = mx = 0
        for cost, cashback in transactions:
            tot += max(cost - cashback, 0)
            mx = max(mx, min(cost, cashback))
        return tot + mx
        '''
        n = len(transactions)
        cnt = [0] * n
        tot = 0
        for i in range(n):
            d = transactions[i][1] - transactions[i][0]
            if d <= 0:
                tot += d
            cnt[i] = d
        ans = 0
        for i in range(n):
            if cnt[i] <= 0:
                ans = max(ans, transactions[i][0] - tot + cnt[i])
            else:
                ans = max(ans, transactions[i][0] - tot)
        return ans
        '''
# @lc code=end

