#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#
# https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (22.19%)
# Likes:    487
# Dislikes: 0
# Total Accepted:    29.4K
# Total Submissions: 127.3K
# Testcase Example:  '[1]\n1'
#
# 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回
# -1 。
# 
# 子数组 是数组中 连续 的一部分。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1], k = 1
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2], k = 4
# 输出：-1
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [2,-1,2], k = 3
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 1 <= k <= 10^9
# 
# 
#
from bisect import bisect
from collections import deque
from itertools import accumulate
from typing import List
# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # preSumArr = [0]
        # for num in nums:
        #     preSumArr.append(preSumArr[-1] + num)
        preSumArr = list(accumulate(nums, initial=0))
        q = deque()
        res = len(nums) + 1
        for i, curSum in enumerate(preSumArr):
            while q and curSum - preSumArr[q[0]] >= k:
                res = min(res, i - q.popleft())
            while q and preSumArr[q[-1]] >= curSum:
                q.pop()
            q.append(i)
        return res if res < len(nums) + 1 else -1
        '''
        pres = 0
        d = {0:-1}
        q = [0]
        ans = len(nums) + 1
        for i, num in enumerate(nums):
            pres += num

            j = bisect.bisect(q, pres - k)
            if j == len(q):
                ans = min(ans, i - d[q[-1]])
            elif q[j] == pres - k:
                ans = min(ans, i - d[q[j]])
            elif j > 0:
                ans = min(ans, i - d[q[j-1]])

            d[pres] = i
            while q and q[-1] >= pres:
                q.pop()
            q.append(pres)

        return ans if ans <= len(nums) else -1
        '''
# @lc code=end

