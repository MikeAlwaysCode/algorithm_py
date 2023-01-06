#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (62.28%)
# Likes:    4018
# Dislikes: 0
# Total Accepted:    618.7K
# Total Submissions: 992.9K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 
# 
# 示例 2：
# 
# 
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        ans = 0
        i, j = 0, len(height) - 1
        pre = suf = 0
        while i <= j:
            pre = max(pre, height[i])
            suf = max(suf, height[j])
            if pre <= suf:
                ans += pre - height[i]
                i += 1
            else:
                ans += suf - height[j]
                j -= 1
        '''
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n
        suf_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h
        '''
        return ans
# @lc code=end

