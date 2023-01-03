#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#
# https://leetcode.cn/problems/advantage-shuffle/description/
#
# algorithms
# Medium (47.59%)
# Likes:    226
# Dislikes: 0
# Total Accepted:    32.3K
# Total Submissions: 66.8K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# 给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums 的优势可以用满足 nums1[i] > nums2[i] 的索引 i
# 的数目来描述。
# 
# 返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# 输出：[2,11,7,15]
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# 输出：[24,32,8,12]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length <= 10^5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 10^9
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        idx1 = list(range(n))
        idx2 = list(range(n))
        idx1.sort(key = lambda x: nums1[x])
        idx2.sort(key = lambda x: nums2[x])
        ans = [0] * n
        l, r = 0, n-1
        for i in range(n):
            if nums1[idx1[i]] > nums2[idx2[l]]:
                ans[idx2[l]] = nums1[idx1[i]]
                l += 1
            else:
                ans[idx2[r]] = nums1[idx1[i]]
                r -= 1
        return ans
# @lc code=end

