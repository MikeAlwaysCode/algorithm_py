#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#
# https://leetcode.cn/problems/number-of-good-pairs/description/
#
# algorithms
# Easy (84.72%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    67.2K
# Total Submissions: 79.3K
# Testcase Example:  '[1,2,3,1,1,3]'
#
# 给你一个整数数组 nums 。
# 
# 如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
# 
# 返回好数对的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,3,1,1,3]
# 输出：4
# 解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
# 
# 
# 示例 2：
# 
# 输入：nums = [1,1,1,1]
# 输出：6
# 解释：数组中的每组数字都是好数对
# 
# 示例 3：
# 
# 输入：nums = [1,2,3]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 
# 
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        '''
        cnt = Counter()
        for x in nums:
            ans += cnt[x]
            cnt[x] += 1
        return ans
        '''
        cnt = Counter(nums)
        for v in cnt.values():
            ans += v * (v - 1) // 2
        return ans
# @lc code=end

