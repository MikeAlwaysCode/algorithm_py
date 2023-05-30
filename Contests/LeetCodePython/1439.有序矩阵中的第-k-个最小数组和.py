#
# @lc app=leetcode.cn id=1439 lang=python3
#
# [1439] 有序矩阵中的第 k 个最小数组和
#
# https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/description/
#
# algorithms
# Hard (60.21%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    8.8K
# Total Submissions: 14.7K
# Testcase Example:  '[[1,3,11],[2,4,6]]\n5'
#
# 给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。
# 
# 你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。
# 
# 
# 
# 示例 1：
# 
# 输入：mat = [[1,3,11],[2,4,6]], k = 5
# 输出：7
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。  
# 
# 示例 2：
# 
# 输入：mat = [[1,3,11],[2,4,6]], k = 9
# 输出：17
# 
# 
# 示例 3：
# 
# 输入：mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
# 输出：9
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9
# 。 
# 
# 
# 示例 4：
# 
# 输入：mat = [[1,1,10],[2,2,9]], k = 7
# 输出：12
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat.length[i]
# 1 <= m, n <= 40
# 1 <= k <= min(200, n ^ m)
# 1 <= mat[i][j] <= 5000
# mat[i] 是一个非递减数组
# 
# 
#
from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = []
        h = [(nums1[0] + nums2[0], 0, 0)]
        while h and len(ans) < k:
            _, i, j = heappop(h)
            ans.append(nums1[i] + nums2[j])  # 数对和
            if j == 0 and i + 1 < len(nums1):
                heappush(h, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        a = mat[0][:k]
        for row in mat[1:]:
            a = self.kSmallestPairs(row, a, k)
        return a[-1]
# @lc code=end

