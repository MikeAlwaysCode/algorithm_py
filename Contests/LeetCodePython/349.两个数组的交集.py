#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode.cn/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (74.35%)
# Likes:    591
# Dislikes: 0
# Total Accepted:    333.3K
# Total Submissions: 448.3K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 解释：[4,9] 也是可通过的
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1) & set(nums2))
        nums1.sort()
        nums2.sort()
        i = j = 0
        p = -1
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] != p:
                    p = nums1[i]
                    ans.append(p)
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans
# @lc code=end

