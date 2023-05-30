#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#
# https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (40.70%)
# Likes:    472
# Dislikes: 0
# Total Accepted:    58.5K
# Total Submissions: 143.7K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# 给定两个以 升序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。
# 
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
# 
# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
# ⁠    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# 
# 示例 2:
# 
# 
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# 
# 示例 3:
# 
# 
# 输入: nums1 = [1,2], nums2 = [3], k = 3 
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums1.length, nums2.length <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 和 nums2 均为升序排列
# 1 <= k <= 1000
# 
# 
#
from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        h = [(nums1[0] + nums2[0], 0, 0)]
        while h and len(ans) < k:
            _, i, j = heappop(h)
            ans.append((nums1[i], nums2[j]))  # 数对
            if j == 0 and i + 1 < len(nums1):
                heappush(h, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
# @lc code=end

