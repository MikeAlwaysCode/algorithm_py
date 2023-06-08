#
# @lc app=leetcode.cn id=2563 lang=python3
#
# [2563] 统计公平数对的数目
#
# https://leetcode.cn/problems/count-the-number-of-fair-pairs/description/
#
# algorithms
# Medium (33.43%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 19.9K
# Testcase Example:  '[0,1,7,4,4,5]\n3\n6'
#
# 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。
# 
# 如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：
# 
# 
# 0 <= i < j < n，且
# lower <= nums[i] + nums[j] <= upper
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6
# 输出：6
# 解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,7,9,2,5], lower = 11, upper = 11
# 输出：1
# 解释：只有单个公平数对：(2,3) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# nums.length == n
# -10^9 <= nums[i] <= 10^9
# -10^9 <= lower <= upper <= 10^9
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        rl, ru = n - 1, n - 1
        ans = 0
        for l in range(n):
            rl = max(rl, l + 1)
            while rl - 1 > l and nums[l] + nums[rl - 1] >= lower:
                rl -= 1
            while ru > l and nums[l] + nums[ru] > upper:
                ru -= 1
            if ru <= l: break
            if nums[l] + nums[rl] < lower: continue
            if ru >= rl: ans += ru - rl + 1
        return ans
# @lc code=end

