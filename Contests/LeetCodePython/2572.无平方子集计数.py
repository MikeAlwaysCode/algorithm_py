#
# @lc app=leetcode.cn id=2572 lang=python3
#
# [2572] 无平方子集计数
#
# https://leetcode.cn/problems/count-the-number-of-square-free-subsets/description/
#
# algorithms
# Medium (23.13%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 7.6K
# Testcase Example:  '[3,4,4,5]'
#
# 给你一个正整数数组 nums 。
# 
# 如果数组 nums 的子集中的元素乘积是一个 无平方因子数 ，则认为该子集是一个 无平方 子集。
# 
# 无平方因子数 是无法被除 1 之外任何平方数整除的数字。
# 
# 返回数组 nums 中 无平方 且 非空 的子集数目。因为答案可能很大，返回对 10^9 + 7 取余的结果。
# 
# nums 的 非空子集 是可以由删除 nums
# 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,4,4,5]
# 输出：3
# 解释：示例中有 3 个无平方子集：
# - 由第 0 个元素 [3] 组成的子集。其元素的乘积是 3 ，这是一个无平方因子数。
# - 由第 3 个元素 [5] 组成的子集。其元素的乘积是 5 ，这是一个无平方因子数。
# - 由第 0 个和第 3 个元素 [3,5] 组成的子集。其元素的乘积是 15 ，这是一个无平方因子数。
# 可以证明给定数组中不存在超过 3 个无平方子集。
# 
# 示例 2：
# 
# 
# 输入：nums = [1]
# 输出：1
# 解释：示例中有 1 个无平方子集：
# - 由第 0 个元素 [1] 组成的子集。其元素的乘积是 1 ，这是一个无平方因子数。
# 可以证明给定数组中不存在超过 1 个无平方子集。
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 30
# 
# 
#
from collections import Counter
from typing import List

# @lc code=start
MOD = 10 ** 9 + 7
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
M = 1 << len(PRIMES)
NSQ_TO_MASK = [0] * 31
for i in range(2, 31):
    for j, p in enumerate(PRIMES):
        if i % p == 0:
            if i % (p * p) == 0:
                NSQ_TO_MASK[i] = -1
                break
            NSQ_TO_MASK[i] |= 1 << j

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        dp = [0] * M
        dp[0] = 1
        cnt = Counter(nums)
        for x, c in cnt.items():
            mask = NSQ_TO_MASK[x]
            if mask <= 0: continue
            other = (M - 1) ^ mask
            j = other
            while True:
                dp[j | mask] = (dp[j | mask] + dp[j] * c) % MOD
                j = (j - 1) & other
                if j == other: break
        return (sum(dp) * pow(2, cnt[1], MOD) - 1) % MOD
        '''
        # 01背包
        dp = [0] * M
        dp[0] = 1
        for x in nums:
            mask = NSQ_TO_MASK[x]
            if mask == -1: continue
            for j in range(M - 1, mask - 1, -1):
                if (j | mask) == j:
                    dp[j] = (dp[j] + dp[j ^ mask]) % MOD  # 不选 mask + 选 mask
        return (sum(dp) - 1) % MOD
        '''
# @lc code=end

