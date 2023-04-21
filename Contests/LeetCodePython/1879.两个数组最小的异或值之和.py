#
# @lc app=leetcode.cn id=1879 lang=python3
#
# [1879] 两个数组最小的异或值之和
#
# https://leetcode.cn/problems/minimum-xor-sum-of-two-arrays/description/
#
# algorithms
# Hard (48.06%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 7.3K
# Testcase Example:  '[1,2]\n[2,3]'
#
# 给你两个整数数组 nums1 和 nums2 ，它们长度都为 n 。
# 
# 两个数组的 异或值之和 为 (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... +
# (nums1[n - 1] XOR nums2[n - 1]) （下标从 0 开始）。
# 
# 
# 比方说，[1,2,3] 和 [3,2,1] 的 异或值之和 等于 (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 +
# 2 = 4 。
# 
# 
# 请你将 nums2 中的元素重新排列，使得 异或值之和 最小 。
# 
# 请你返回重新排列之后的 异或值之和 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2], nums2 = [2,3]
# 输出：2
# 解释：将 nums2 重新排列得到 [3,2] 。
# 异或值之和为 (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2 。
# 
# 示例 2：
# 
# 输入：nums1 = [1,0,3], nums2 = [5,3,4]
# 输出：8
# 解释：将 nums2 重新排列得到 [5,4,3] 。
# 异或值之和为 (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length
# n == nums2.length
# 1 <= n <= 14
# 0 <= nums1[i], nums2[i] <= 10^7
# 
# 
#
import math
from typing import List


# @lc code=start
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        f = [math.inf] * (1 << n)
        f[0] = 0

        for mask in range(1, 1 << n):
            c = mask.bit_count()
            for i in range(n):
                if (mask >> i) & 1:
                    f[mask] = min(f[mask], f[mask ^ (1 << i)] + (nums1[c - 1] ^ nums2[i]))
        
        return f[(1 << n) - 1]
# @lc code=end

