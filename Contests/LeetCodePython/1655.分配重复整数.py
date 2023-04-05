#
# @lc app=leetcode.cn id=1655 lang=python3
#
# [1655] 分配重复整数
#
# https://leetcode.cn/problems/distribute-repeating-integers/description/
#
# algorithms
# Hard (39.57%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 9.5K
# Testcase Example:  '[1,2,3,4]\n[2]'
#
# 给你一个长度为 n 的整数数组 nums ，这个数组中至多有 50 个不同的值。同时你有 m 个顾客的订单 quantity ，其中，整数
# quantity[i] 是第 i 位顾客订单的数目。请你判断是否能将 nums 中的整数分配给这些顾客，且满足：
# 
# 
# 第 i 位顾客 恰好 有 quantity[i] 个整数。
# 第 i 位顾客拿到的整数都是 相同的 。
# 每位顾客都满足上述两个要求。
# 
# 
# 如果你可以分配 nums 中的整数满足上面的要求，那么请返回 true ，否则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,4], quantity = [2]
# 输出：false
# 解释：第 0 位顾客没办法得到两个相同的整数。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,3], quantity = [2]
# 输出：true
# 解释：第 0 位顾客得到 [3,3] 。整数 [1,2] 都没有被使用。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,1,2,2], quantity = [2,2]
# 输出：true
# 解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [2,2] 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= 1000
# m == quantity.length
# 1 <= m <= 10
# 1 <= quantity[i] <= 10^5
# nums 中至多有 50 个不同的数字。
# 
# 
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        cnt = Counter(nums)
        n = len(quantity)

        need = [0] * (1 << n)
        # for mask in range(1, 1 << n):
        #     for j in range(n):
        #         if (mask >> j) & 1:
        #             need[mask] += quantity[j]
        for j in range(n):
            bit = 1 << j
            for mask in range(bit):
                need[mask|bit] = need[mask] + quantity[j]

        dp = [False] * (1 << n)
        dp[0] = True
        for v in cnt.values():
            tmp = dp.copy()
            for mask in range(1, 1 << n):
                if tmp[mask]: continue
                sub = mask
                while True:
                    if need[sub] <= v and dp[mask ^ sub]:
                        tmp[mask] = True
                        break
                    sub = (sub - 1) & mask
                    if sub == mask: break
            if tmp[(1 << n) - 1]: return True
            dp = tmp
        return False
# @lc code=end

