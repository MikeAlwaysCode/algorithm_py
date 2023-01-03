#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
# https://leetcode.cn/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (57.77%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    77.1K
# Total Submissions: 133.5K
# Testcase Example:  '[2,1,2]'
#
# 给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回
# 0。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,1,2]
# 输出：5
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^6
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0
# @lc code=end

