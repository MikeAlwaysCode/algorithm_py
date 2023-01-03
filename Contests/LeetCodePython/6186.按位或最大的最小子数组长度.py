#
# @lc app=leetcode.cn id=6186 lang=python3
#
# [6186] 按位或最大的最小子数组长度
#
# https://leetcode.cn/problems/smallest-subarrays-with-maximum-bitwise-or/description/
#
# algorithms
# Medium (28.87%)
# Likes:    2
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 6K
# Testcase Example:  '[1,0,2,1,3]'
#
# 给你一个长度为 n 下标从 0 开始的数组 nums ，数组中所有数字均为非负整数。对于 0 到 n - 1 之间的每一个下标 i ，你需要找出 nums
# 中一个 最小 非空子数组，它的起始位置为 i （包含这个位置），同时有 最大 的 按位或运算值 。
# 
# 
# 换言之，令 Bij 表示子数组 nums[i...j] 的按位或运算的结果，你需要找到一个起始位置为 i 的最小子数组，这个子数组的按位或运算的结果等于
# max(Bik) ，其中 i <= k <= n - 1 。
# 
# 
# 一个数组的按位或运算值是这个数组里所有数字按位或运算的结果。
# 
# 请你返回一个大小为 n 的整数数组 answer，其中 answer[i]是开始位置为 i ，按位或运算结果最大，且 最短 子数组的长度。
# 
# 子数组 是数组里一段连续非空元素组成的序列。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,0,2,1,3]
# 输出：[3,3,2,2,1]
# 解释：
# 任何位置开始，最大按位或运算的结果都是 3 。
# - 下标 0 处，能得到结果 3 的最短子数组是 [1,0,2] 。
# - 下标 1 处，能得到结果 3 的最短子数组是 [0,2,1] 。
# - 下标 2 处，能得到结果 3 的最短子数组是 [2,1] 。
# - 下标 3 处，能得到结果 3 的最短子数组是 [1,3] 。
# - 下标 4 处，能得到结果 3 的最短子数组是 [3] 。
# 所以我们返回 [3,3,2,2,1] 。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,2]
# 输出：[2,1]
# 解释：
# 下标 0 处，能得到最大按位或运算值的最短子数组长度为 2 。
# 下标 1 处，能得到最大按位或运算值的最短子数组长度为 1 。
# 所以我们返回 [2,1] 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= n <= 10^5
# 0 <= nums[i] <= 10^9
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ors = []  # 按位或的值 + 对应子数组的右端点的最小值
        for i in range(n - 1, -1, -1):
            num = nums[i]
            ors.append([0, i])
            k = 0
            for p in ors:
                p[0] |= num
                if ors[k][0] == p[0]:
                    ors[k][1] = p[1]  # 合并相同值，下标取最小的
                else:
                    k += 1
                    ors[k] = p
            del ors[k + 1:]
            # 本题只用到了 ors[0]，如果题目改成任意给定数值，可以在 ors 中查找
            ans[i] = ors[0][1] - i + 1
        return ans
        '''
        b = 0
        n = len(nums)
        cnt = [0] * 31
        j = n - 1
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            tmp = nums[i]
            cur = 0
            while tmp:
                if tmp & 1:
                    cnt[cur] += 1
                cur += 1
                tmp >>= 1
                
            b |= nums[i]
            while j > i:
                tmp = nums[j]
                cur = 0
                chk = True
                while tmp:
                    if tmp & 1 and cnt[cur] <= 1:
                        chk = False
                        break
                    cur += 1
                    tmp >>= 1
                if chk:
                    tmp = nums[j]
                    j -= 1
                    cur = 0
                    while tmp:
                        if tmp & 1:
                            cnt[cur] -= 1
                        cur += 1
                        tmp >>= 1
                else:
                    break
            
            ans[i] = j - i + 1
        return ans
        '''
# @lc code=end

