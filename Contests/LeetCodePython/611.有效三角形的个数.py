#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#
# https://leetcode.cn/problems/valid-triangle-number/description/
#
# algorithms
# Medium (53.76%)
# Likes:    449
# Dislikes: 0
# Total Accepted:    80.5K
# Total Submissions: 149.7K
# Testcase Example:  '[2,2,3,4]'
#
# 给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [2,2,3,4]
# 输出: 3
# 解释:有效的组合是: 
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [4,2,3,4]
# 输出: 4
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            k = i
            for j in range(i + 1, n):
                while k + 1 < n and nums[k + 1] < nums[i] + nums[j]:
                    k += 1
                ans += max(k - j, 0)
        return ans
        '''
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += k - j
        return ans
        '''
# @lc code=end

