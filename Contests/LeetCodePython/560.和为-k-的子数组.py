#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (45.42%)
# Likes:    1724
# Dislikes: 0
# Total Accepted:    277.7K
# Total Submissions: 611.5K
# Testcase Example:  '[1,1,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3], k = 3
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#
import collections
from typing import List
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = collections.defaultdict(int)
        s[0] = 1
        tot = ans = 0
        for num in nums:
            tot += num
            if tot - k in s:
                ans += s[tot - k]
            s[tot] += 1
        return ans
# @lc code=end

