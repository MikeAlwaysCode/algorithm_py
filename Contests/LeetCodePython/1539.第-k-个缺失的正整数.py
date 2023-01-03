#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#
# https://leetcode.cn/problems/kth-missing-positive-number/description/
#
# algorithms
# Easy (53.87%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    35.2K
# Total Submissions: 65.4K
# Testcase Example:  '[2,3,4,7,11]\n5'
#
# 给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
# 
# 请你找到这个数组里第 k 个缺失的正整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [2,3,4,7,11], k = 5
# 输出：9
# 解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [1,2,3,4], k = 2
# 输出：6
# 解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# 对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j] 
# 
# 
# 
# 
# 进阶：
# 
# 你可以设计一个时间复杂度小于 O(n) 的算法解决此问题吗？
# 
#
import bisect
from typing import List


# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) >> 1
            x = arr[mid] if mid < len(arr) else 10**9
            if x - mid - 1 >= k:
                r = mid
            else:
                l = mid + 1

        return k - (arr[l - 1] - (l - 1) - 1) + arr[l - 1]
        '''
        for a in arr:
            if a <= k:
                k += 1
        return k
        '''
        '''
        n = len(arr)
        miss = [0] * n
        for i, a in enumerate(arr):
            miss[i] = a - i - 1
        
        j = bisect.bisect_left(miss, k)
        if j >= n or miss[j] > k:
            return k if j == 0 else k + j
        # elif miss[j] == k:
        else:
            return arr[j] - 1
        '''
# @lc code=end

