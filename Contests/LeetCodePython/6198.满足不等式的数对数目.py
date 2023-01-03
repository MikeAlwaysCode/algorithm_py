#
# @lc app=leetcode.cn id=6198 lang=python3
#
# [6198] 满足不等式的数对数目
#
# https://leetcode.cn/problems/number-of-pairs-satisfying-inequality/description/
#
# algorithms
# Hard (34.93%)
# Likes:    0
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 3.5K
# Testcase Example:  '[3,2,5]\n[2,2,1]\n1'
#
# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两个数组的大小都为 n ，同时给你一个整数 diff ，统计满足以下条件的 数对 (i,
# j) ：
# 
# 
# 0 <= i < j <= n - 1 且
# nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
# 
# 
# 请你返回满足条件的 数对数目 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
# 输出：3
# 解释：
# 总共有 3 个满足条件的数对：
# 1. i = 0, j = 1：3 - 2 <= 2 - 2 + 1 。因为 i < j 且 1 <= 1 ，这个数对满足条件。
# 2. i = 0, j = 2：3 - 5 <= 2 - 1 + 1 。因为 i < j 且 -2 <= 2 ，这个数对满足条件。
# 3. i = 1, j = 2：2 - 5 <= 2 - 1 + 1 。因为 i < j 且 -3 <= 2 ，这个数对满足条件。
# 所以，我们返回 3 。
# 
# 
# 示例 2：
# 
# 输入：nums1 = [3,-1], nums2 = [-2,2], diff = -1
# 输出：0
# 解释：
# 没有满足条件的任何数对，所以我们返回 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length == nums2.length
# 2 <= n <= 10^5
# -10^4 <= nums1[i], nums2[i] <= 10^4
# -10^4 <= diff <= 10^4
# 
# 
#
from typing import List
from bisect import bisect_left, bisect_right
# @lc code=start
'''
from sortedcontainers import SortedSet, SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        ans = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff:
        #             ans += 1
        # return ans
        d = [0] * n
        for i in range(n):
            d[i] = nums1[i] - nums2[i]
        # d.sort()
        # cnt = [0] * n
        k = SortedList()
        cn = 0
        print(d)
        for i in range(n-1, -1, -1):
            if cn > 0:
                j = bisect_left(k, d[i]-diff)
                ans += cn - j
            k.add(d[i])
            cn += 1
            # print(k)
        return ans
'''
class Solution:
    def numberOfPairs(self, a: List[int], nums2: List[int], diff: int) -> int:
        for i, x in enumerate(nums2):
            a[i] -= x
        b = a.copy()
        b.sort()  # 配合下面的二分，离散化

        ans = 0
        t = BIT(len(a) + 1)
        for x in a:
            ans += t.query(bisect_right(b, x + diff))
            t.add(bisect_left(b, x) + 1)
        return ans

class BIT:
    def __init__(self, n):
        self.tree = [0] * n

    def add(self, x):
        while x < len(self.tree):
            self.tree[x] += 1
            x += x & -x

    def query(self, x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x &= x - 1
        return res
# @lc code=end

