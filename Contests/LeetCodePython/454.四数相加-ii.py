#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# https://leetcode.cn/problems/4sum-ii/description/
#
# algorithms
# Medium (63.37%)
# Likes:    629
# Dislikes: 0
# Total Accepted:    140.2K
# Total Submissions: 221.3K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l)
# 能满足：
# 
# 
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 解释：
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
# 
# 
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        countAB = Counter(a + b for a in nums1 for b in nums2)
        ans = 0
        for c in nums3:
            for d in nums4:
                if -c-d in countAB:
                    ans += countAB[-c-d]
        return ans
# @lc code=end

