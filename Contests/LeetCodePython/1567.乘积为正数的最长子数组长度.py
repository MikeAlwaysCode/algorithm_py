#
# @lc app=leetcode.cn id=1567 lang=python3
#
# [1567] 乘积为正数的最长子数组长度
#
# https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/description/
#
# algorithms
# Medium (42.50%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    31.5K
# Total Submissions: 74.1K
# Testcase Example:  '[1,-2,-3,4]'
#
# 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。
# 
# 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
# 
# 请你返回乘积为正数的最长子数组长度。
# 
# 
# 
# 示例  1：
# 
# 
# 输入：nums = [1,-2,-3,4]
# 输出：4
# 解释：数组本身乘积就是正数，值为 24 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,1,-2,-3,-4]
# 输出：3
# 解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
# 注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
# 
# 示例 3：
# 
# 
# 输入：nums = [-1,-2,-3,0,1]
# 输出：2
# 解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = int(nums[0] > 0), int(nums[0] < 0)
        ans = pos

        for x in nums[1:]:
            if x > 0:
                pos += 1
                neg = neg + 1 if neg else 0
            elif x < 0:
                pos, neg = neg + 1 if neg else 0, pos + 1
            else:
                pos = neg = 0
            ans = max(ans, pos)
        
        return ans
# @lc code=end

