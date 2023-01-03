#
# @lc app=leetcode.cn id=6190 lang=python3
#
# [6190] 找到所有好下标
#
# https://leetcode.cn/problems/find-all-good-indices/description/
#
# algorithms
# Medium (22.54%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 15.2K
# Testcase Example:  '[2,1,1,1,3,4,1]\n2'
#
# 给你一个大小为 n 下标从 0 开始的整数数组 nums 和一个正整数 k 。
# 
# 对于 k <= i < n - k 之间的一个下标 i ，如果它满足以下条件，我们就称它为一个 好 下标：
# 
# 
# 下标 i 之前 的 k 个元素是 非递增的 。
# 下标 i 之后 的 k 个元素是 非递减的 。
# 
# 
# 按 升序 返回所有好下标。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,1,1,1,3,4,1], k = 2
# 输出：[2,3]
# 解释：数组中有两个好下标：
# - 下标 2 。子数组 [2,1] 是非递增的，子数组 [1,3] 是非递减的。
# - 下标 3 。子数组 [1,1] 是非递增的，子数组 [3,4] 是非递减的。
# 注意，下标 4 不是好下标，因为 [4,1] 不是非递减的。
# 
# 示例 2：
# 
# 
# 输入：nums = [2,1,1,2], k = 2
# 输出：[]
# 解释：数组中没有好下标。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 3 <= n <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= k <= n / 2
# 
# 
#
from collections import deque
from itertools import accumulate, pairwise
from typing import List
# @lc code=start
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        lt = list(accumulate((x < y for x, y in pairwise(nums)), initial=0))
        gt = list(accumulate((x > y for x, y in pairwise(nums)), initial=0))
        return [i for i in range(k, len(nums) - k) if lt[i - 1] == lt[i - k] and gt[i + 1] == gt[i + k]]
        '''
        q = deque()
        n = len(nums)
        suf = [0] * n
        for i in range(n-1, -1, -1):
            if not q or nums[i] <= q[-1]:
                q.append(nums[i])
            else:
                q.clear()
                q.append(nums[i])
            suf[i] = len(q)
        # print(suf)
        q.clear()
        ans = []
        for i in range(n-k-1):
            if not q or nums[i] <= q[-1]:
                q.append(nums[i])
            else:
                q.clear()
                q.append(nums[i])
            if len(q) >= k and suf[i+2] >= k:
                ans.append(i+1)
        return ans
        '''
# @lc code=end

