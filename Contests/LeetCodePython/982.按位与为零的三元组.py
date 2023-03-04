#
# @lc app=leetcode.cn id=982 lang=python3
#
# [982] 按位与为零的三元组
#
# https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/description/
#
# algorithms
# Hard (57.66%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 13.1K
# Testcase Example:  '[2,1,3]'
#
# 给你一个整数数组 nums ，返回其中 按位与三元组 的数目。
# 
# 按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：
# 
# 
# 0 <= i < nums.length
# 0 <= j < nums.length
# 0 <= k < nums.length
# nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,1,3]
# 输出：12
# 解释：可以选出如下 i, j, k 三元组：
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,0,0]
# 输出：27
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] < 2^16
# 
# 
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = [0] * (1 << 16)
        cnt[0] = len(nums)
        for x in nums:
            x ^= (1 << 16) - 1
            s = x
            while s:
                cnt[s] += 1
                s = (s - 1) & x
        return sum(cnt[x & y] for x in nums for y in nums)
        '''
        cnt = Counter()
        for i in range(len(nums)):
            cnt[nums[i] & nums[i]] += 1
            for j in range(i + 1, len(nums)):
                cnt[nums[i] & nums[j]] += 2
        
        ans = 0
        for x in nums:
            x ^= (1 << 16) - 1
            s = x
            while True:
                ans += cnt[s]
                s = (s - 1) & x
                if s == x: break
        return ans
        '''
        '''
        for x in nums:
            for k, v in cnt.items():
                if k & x == 0:
                    ans += v
        return ans
        '''
# @lc code=end

