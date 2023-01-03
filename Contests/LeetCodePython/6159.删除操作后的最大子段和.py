#
# @lc app=leetcode.cn id=6159 lang=python3
#
# [6159] 删除操作后的最大子段和
#
# https://leetcode.cn/problems/maximum-segment-sum-after-removals/description/
#
# algorithms
# Hard (47.00%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 3.7K
# Testcase Example:  '[1,2,5,6,1]\n[0,3,2,4,1]'
#
# 给你两个下标从 0 开始的整数数组 nums 和 removeQueries ，两者长度都为 n 。对于第 i 个查询，nums 中位于下标
# removeQueries[i] 处的元素被删除，将 nums 分割成更小的子段。
# 
# 一个 子段 是 nums 中连续 正 整数形成的序列。子段和 是子段中所有元素的和。
# 
# 请你返回一个长度为 n 的整数数组 answer ，其中 answer[i]是第 i 次删除操作以后的 最大 子段和。
# 
# 注意：一个下标至多只会被删除一次。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
# 输出：[14,7,2,2,0]
# 解释：用 0 表示被删除的元素，答案如下所示：
# 查询 1 ：删除第 0 个元素，nums 变成 [0,2,5,6,1] ，最大子段和为子段 [2,5,6,1] 的和 14 。
# 查询 2 ：删除第 3 个元素，nums 变成 [0,2,5,0,1] ，最大子段和为子段 [2,5] 的和 7 。
# 查询 3 ：删除第 2 个元素，nums 变成 [0,2,0,0,1] ，最大子段和为子段 [2] 的和 2 。
# 查询 4 ：删除第 4 个元素，nums 变成 [0,2,0,0,0] ，最大子段和为子段 [2] 的和 2 。
# 查询 5 ：删除第 1 个元素，nums 变成 [0,0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
# 所以，我们返回 [14,7,2,2,0] 。
# 
# 示例 2：
# 
# 输入：nums = [3,2,11,1], removeQueries = [3,2,1,0]
# 输出：[16,5,3,0]
# 解释：用 0 表示被删除的元素，答案如下所示：
# 查询 1 ：删除第 3 个元素，nums 变成 [3,2,11,0] ，最大子段和为子段 [3,2,11] 的和 16 。
# 查询 2 ：删除第 2 个元素，nums 变成 [3,2,0,0] ，最大子段和为子段 [3,2] 的和 5 。
# 查询 3 ：删除第 1 个元素，nums 变成 [3,0,0,0] ，最大子段和为子段 [3] 的和 3 。
# 查询 5 ：删除第 0 个元素，nums 变成 [0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
# 所以，我们返回 [16,5,3,0] 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length == removeQueries.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= removeQueries[i] < n
# removeQueries 中所有数字 互不相同 。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        fa = list(range(n + 1))
        s = [0] * (n + 1)
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        
        ans = [0] * n
        for i in range(n - 1, 0, -1):
            x = removeQueries[i]
            to = find(x + 1)
            fa[x] = to
            s[to] += s[x] + nums[x]
            ans[i-1] = max(ans[i], s[to])
        return ans
# @lc code=end

