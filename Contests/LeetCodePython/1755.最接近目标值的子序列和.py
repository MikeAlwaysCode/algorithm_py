#
# @lc app=leetcode.cn id=1755 lang=python3
#
# [1755] 最接近目标值的子序列和
#
# https://leetcode.cn/problems/closest-subsequence-sum/description/
#
# algorithms
# Hard (44.87%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 13.3K
# Testcase Example:  '[5,-7,3,5]\n6'
#
# 给你一个整数数组 nums 和一个目标值 goal 。
# 
# 你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum -
# goal) 。
# 
# 返回 abs(sum - goal) 可能的 最小值 。
# 
# 注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,-7,3,5], goal = 6
# 输出：0
# 解释：选择整个数组作为选出的子序列，元素和为 6 。
# 子序列和与目标值相等，所以绝对差为 0 。
# 
# 
# 示例 2：
# 
# 输入：nums = [7,-9,15,-2], goal = -5
# 输出：1
# 解释：选出子序列 [7,-9,-2] ，元素和为 -4 。
# 绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,2,3], goal = -7
# 输出：7
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 40
# -10^7 <= nums[i] <= 10^7
# -10^9 <= goal <= 10^9
# 
# 
#
import bisect
import math
from typing import List


# @lc code=start
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums) // 2
        bit = {1<<i:nums[i] for i in range(n)}
        dp = [0] * (1 << n)
        for mask in range(1, 1 << n):
            # 从不包含lb元素的子集 + lb元素转移
            dp[mask] = dp[mask ^ mask & -mask] + bit[mask & -mask]
        res1 = sorted(list(set(dp)))

        m = len(nums) - n
        bit = {1<<i:nums[i + n] for i in range(m)}
        dp = [0] * (1 << m)
        for mask in range(1, 1 << m):
            dp[mask] = dp[mask ^ mask & -mask] + bit[mask & -mask]
        res2 = sorted(list(set(dp)), reverse = True)

        ans = math.inf

        for x in res1:
            ans = min(ans, abs(goal - x))
        for x in res2:
            ans = min(ans, abs(goal - x))

        i = j = 0
        while i < len(res1) and j < len(res2):
            ans = min(ans, abs(res1[i] + res2[j] - goal))
            if res1[i] + res2[j] > goal:
                j += 1
            elif res1[i] + res2[j] < goal:
                i += 1
            else:
                break
        return ans
# @lc code=end

