#
# @lc app=leetcode.cn id=1577 lang=python3
#
# [1577] 数的平方等于两数乘积的方法数
#
# https://leetcode.cn/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/description/
#
# algorithms
# Medium (34.16%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 18.9K
# Testcase Example:  '[7,4]\n[5,2,8,9]'
#
# 给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：
# 
# 
# 类型 1：三元组 (i, j, k) ，如果 nums1[i]^2 == nums2[j] * nums2[k] 其中 0 <= i <
# nums1.length 且 0 <= j < k < nums2.length
# 类型 2：三元组 (i, j, k) ，如果 nums2[i]^2 == nums1[j] * nums1[k] 其中 0 <= i <
# nums2.length 且 0 <= j < k < nums1.length
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [7,4], nums2 = [5,2,8,9]
# 输出：1
# 解释：类型 1：(1,1,2), nums1[1]^2 = nums2[1] * nums2[2] (4^2 = 2 * 8)
# 
# 示例 2：
# 
# 输入：nums1 = [1,1], nums2 = [1,1,1]
# 输出：9
# 解释：所有三元组都符合题目要求，因为 1^2 = 1 * 1
# 类型 1：(0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2), nums1[i]^2 =
# nums2[j] * nums2[k]
# 类型 2：(0,0,1), (1,0,1), (2,0,1), nums2[i]^2 = nums1[j] * nums1[k]
# 
# 
# 示例 3：
# 
# 输入：nums1 = [7,7,8,3], nums2 = [1,2,9,7]
# 输出：2
# 解释：有两个符合题目要求的三元组
# 类型 1：(3,0,2), nums1[3]^2 = nums2[0] * nums2[2]
# 类型 2：(3,0,1), nums2[3]^2 = nums1[0] * nums1[1]
# 
# 
# 示例 4：
# 
# 输入：nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
# 输出：0
# 解释：不存在符合题目要求的三元组
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 1 <= nums1[i], nums2[i] <= 10^5
# 
# 
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def getTriplets(map1: Counter, map2: Counter):
            triplets = 0
            for num1, count1 in map1.items():
                square = num1 * num1
                for num2, count2 in map2.items():
                    if square % num2 == 0:
                        num3 = square // num2
                        if num2 == num3:
                            curTriplets = count1 * count2 * (count2 - 1) // 2
                            triplets += curTriplets
                        elif num2 < num3 and num3 in map2:
                            count3 = map2[num3]
                            curTriplets = count1 * count2 * count3
                            triplets += curTriplets
            return triplets

        map1 = Counter(nums1)
        map2 = Counter(nums2)
        return getTriplets(map1, map2) + getTriplets(map2, map1)
# @lc code=end

