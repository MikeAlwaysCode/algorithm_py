#
# @lc app=leetcode.cn id=1187 lang=python3
#
# [1187] 使数组严格递增
#
# https://leetcode.cn/problems/make-array-strictly-increasing/description/
#
# algorithms
# Hard (47.99%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 9.3K
# Testcase Example:  '[1,5,3,6,7]\n[1,3,2,4]'
#
# 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
# 
# 每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j
# < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
# 
# 如果无法让 arr1 严格递增，请返回 -1。
# 
# 
# 
# 示例 1：
# 
# 输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# 输出：1
# 解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
# 
# 
# 示例 2：
# 
# 输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# 输出：2
# 解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
# 
# 
# 示例 3：
# 
# 输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# 输出：-1
# 解释：无法使 arr1 严格递增。
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10^9
# 
# 
# 
# 
#
import math
from bisect import bisect_left
from typing import List


# @lc code=start
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        a = arr1 + [math.inf]
        b = sorted(set(arr2))
        n = len(a)
        f = [0] * n
        for i, x in enumerate(a):
            k = bisect_left(b, x)
            res = 0 if k >= i else -math.inf
            if i and a[i - 1] < x:
                res = max(res, f[i - 1])
            for j in range(i - 2, max(i - k - 2, -1), -1):
                if b[k - (i - j - 1)] > a[j]:
                    res = max(res, f[j])
            f[i] = res + 1
        return -1 if f[-1] < 0 else n - f[-1]
# @lc code=end

