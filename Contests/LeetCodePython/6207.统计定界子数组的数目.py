#
# @lc app=leetcode.cn id=6207 lang=python3
#
# [6207] 统计定界子数组的数目
#
# https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/description/
#
# algorithms
# Hard (29.16%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 8.2K
# Testcase Example:  '[1,3,5,2,7,5]\n1\n5'
#
# 给你一个整数数组 nums 和两个整数 minK 以及 maxK 。
# 
# nums 的定界子数组是满足下述条件的一个子数组：
# 
# 
# 子数组中的 最小值 等于 minK 。
# 子数组中的 最大值 等于 maxK 。
# 
# 
# 返回定界子数组的数目。
# 
# 子数组是数组中的一个连续部分。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# 输出：2
# 解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,1,1,1], minK = 1, maxK = 1
# 输出：10
# 解释：nums 的每个子数组都是一个定界子数组。共有 10 个子数组。
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 10^5
# 1 <= nums[i], minK, maxK <= 10^6
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mnPos = mxPos = -1
        left = 0
        ans = 0
        for right, a in enumerate(nums):
            if a == minK:
                mnPos = right
            if a == maxK:
                mxPos = right
            if a < minK or a > maxK:
                left = right + 1
            # ans += max(0, min(mnPos, mxPos) - left + 1)
            m = mnPos if mnPos < mxPos else mxPos
            if m >= left:
                ans += m - left + 1
        return ans
        '''
        n = len(nums)
        dp = [0] * (n + 1)
        cnt = [0] * (n + 1)
        idx = -1
        mn, mx = 10 ** 7, 0
        for i, a in enumerate(nums, 1):
            if minK <= a <= maxK:
                mn = min(mn, a)
                mx = max(mx, a)
                
                if idx == -1:
                    idx = i - 1
                    
                if dp[i-1]:
                    dp[i] = dp[i-1]
                elif mn == minK and mx == maxK:
                    dp[i] = 1
                
                if a == minK or a == maxK:
                    cmn, cmx = 10 ** 7, 0
                    mj = idx
                    for j in range(i-1, idx, -1):
                        if nums[j] < minK or nums[j] > maxK:
                            break
                        # idx = j
                        cmn = min(cmn, nums[j])
                        cmx = max(cmx, nums[j])
                        if cmn == minK and cmx == maxK:
                            if mj == idx:
                                mj = j
                            # dp[i] += 1
                    # print(minK, maxK, cmn, cmx, i, mj)
                    dp[i] += mj - idx
                    idx = mj
            else:
                mn, mx = 10 ** 7, 0
                idx = -1
                
            cnt[i] = cnt[i-1] + dp[i]
        # print(dp)
        return cnt[n]
        '''
# @lc code=end

