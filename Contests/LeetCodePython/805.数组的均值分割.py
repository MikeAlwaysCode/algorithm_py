#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#
# https://leetcode.cn/problems/split-array-with-same-average/description/
#
# algorithms
# Hard (30.17%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 19.3K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# 给定你一个整数数组 nums
# 
# 我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) ==
# average(B) 。
# 
# 如果可以完成则返回true ， 否则返回 false  。
# 
# 注意：对于数组 arr ,  average(arr) 是 arr 的所有元素除以 arr 长度的和。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,2,3,4,5,6,7,8]
# 输出: true
# 解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [3,1]
# 输出: false
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 30
# 0 <= nums[i] <= 10^4
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        m = n // 2
        s = sum(nums)
        if all(s * i % n for i in range(1, m + 1)):
            return False

        dp = [set() for _ in range(m + 1)]
        dp[0].add(0)
        for num in nums:
            for i in range(m, 0, -1):
                for x in dp[i - 1]:
                    curr = x + num
                    if curr * n == s * i:
                        return True
                    dp[i].add(curr)
        return False
        '''
        s = sum(nums)
        for i in range(n):
            nums[i] = nums[i] * n - s

        m = n // 2
        left = set()
        for i in range(1, 1<<m):
            tot = sum(x for j, x in enumerate(nums[:m]) if i >> j & 1)
            if tot == 0:
                return True
            left.add(tot)
        rsum = sum(nums[m:])
        for i in range(1, 1 << (n - m)):
            tot = sum(x for j, x in enumerate(nums[m:]) if i >> j & 1)
            if tot == 0 or rsum != tot and -tot in left:
                return True
        return False
        '''
# @lc code=end

