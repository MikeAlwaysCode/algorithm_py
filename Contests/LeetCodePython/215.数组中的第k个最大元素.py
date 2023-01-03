#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.55%)
# Likes:    1858
# Dislikes: 0
# Total Accepted:    730.1K
# Total Submissions: 1.1M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
# 
# 
# 
# 提示： 
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#
import random
from typing import List


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k);
    
    def quickSelect(self, nums: List[int], l: int, r: int, index: int) -> int:
        q = self.randomPartition(nums, l, r);
        if q == index:
            return nums[q]
        else:
            return self.quickSelect(nums, q + 1, r, index) if q < index else self.quickSelect(nums, l, q - 1, index)
    
    def randomPartition(self, nums: List[int], l: int, r: int) -> int:
        # int i = random.nextInt(r - l + 1) + l;
        # i = random.randrange(l, r)
        i = random.randint(l, r)
        self.swap(nums, i, r)
        return self.partition(nums, l, r)

    def partition(self, nums: List[int], l: int, r: int) -> int:
        x = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= x:
                i += 1
                self.swap(nums, i, j);
                
        self.swap(nums, i + 1, r);
        return i + 1
        
    def swap(self, nums: List[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]
# @lc code=end

