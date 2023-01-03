#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#
# https://leetcode.cn/problems/maximum-sum-circular-subarray/description/
#
# algorithms
# Medium (37.47%)
# Likes:    435
# Dislikes: 0
# Total Accepted:    48.9K
# Total Submissions: 130.6K
# Testcase Example:  '[1,-2,3,-2]'
#
# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
# 
# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i]
# 的前一个元素是 nums[(i - 1 + n) % n] 。
# 
# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j]
# ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= n <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4​​​​​​​
# 
# 
#
import math
from typing import List
# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 最大子数组和
        def kadaneMax(gen):
            # Maximum non-empty subarray sum
            ans = cur = - math.inf
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans
            
        # 最小子数组和
        def kadaneMin(gen):
            # Maximum non-empty subarray sum
            ans = cur = math.inf
            for x in gen:
                cur = x + min(cur, 0)
                ans = min(ans, cur)
            return ans

        # 最大子序和
        ans1 = kadaneMax(nums)
        S = sum(nums)
        ans2 = S - kadaneMin(nums[1:])
        ans3 = S - kadaneMin(nums[:-1])
        return max(ans1, ans2, ans3)
# @lc code=end

