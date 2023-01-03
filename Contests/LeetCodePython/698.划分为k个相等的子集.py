#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (41.37%)
# Likes:    681
# Dislikes: 0
# Total Accepted:    64.7K
# Total Submissions: 155.6K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 
# 
# 
# 示例 1：
# 
# 
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
# 
# 示例 2:
# 
# 
# 输入: nums = [1,2,3,4], k = 3
# 输出: false
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
# 每个元素的频率在 [1,4] 范围内
# 
# 
#
from functools import cache
from typing import List
# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot = sum(nums)
        if tot % k != 0:
            return False
        per = tot // k
        nums.sort()
        if nums[-1] > per:
            return False
        n = len(nums)

        dp = [False] * (1 << n)
        dp[0] = True
        cursum = [0] * (1 << n)
        for i in range(0, 1 << n):
            if not dp[i]:
                continue
            for j in range(n):
                if cursum[i] + nums[j] > per:
                    break
                if (i >> j & 1) == 0:
                    next = i | (1 << j)
                    if not dp[next]:
                        cursum[next] = (cursum[i] + nums[j]) % per
                        dp[next] = True
        return dp[(1 << n) - 1]
        '''
        @cache
        def dfs(s, p):
            if s == 0:
                return True
            for i in range(n):
                if nums[i] + p > per:
                    break
                if s >> i & 1 and dfs(s ^ (1 << i), (p + nums[i]) % per):  # p + nums[i] 等于 per 时置为 0
                    return True
            return False
        return dfs((1 << n) - 1, 0)
        '''
# @lc code=end

