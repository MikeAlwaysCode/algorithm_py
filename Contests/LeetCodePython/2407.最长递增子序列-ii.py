#
# @lc app=leetcode.cn id=2407 lang=python3
#
# [2407] 最长递增子序列 II
#
# https://leetcode.cn/problems/longest-increasing-subsequence-ii/description/
#
# algorithms
# Hard (29.15%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 16.4K
# Testcase Example:  '[4,2,1,4,3,4,5,8,15]\n3'
#
# 给你一个整数数组 nums 和一个整数 k 。
# 
# 找到 nums 中满足以下要求的最长子序列：
# 
# 
# 子序列 严格递增
# 子序列中相邻元素的差值 不超过 k 。
# 
# 
# 请你返回满足上述要求的 最长子序列 的长度。
# 
# 子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [4,2,1,4,3,4,5,8,15], k = 3
# 输出：5
# 解释：
# 满足要求的最长子序列是 [1,3,4,5,8] 。
# 子序列长度为 5 ，所以我们返回 5 。
# 注意子序列 [1,3,4,5,8,15] 不满足要求，因为 15 - 8 = 7 大于 3 。
# 
# 
# 示例 2：
# 
# 输入：nums = [7,4,5,1,8,12,4,7], k = 5
# 输出：4
# 解释：
# 满足要求的最长子序列是 [4,5,8,12] 。
# 子序列长度为 4 ，所以我们返回 4 。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,5], k = 1
# 输出：1
# 解释：
# 满足要求的最长子序列是 [1] 。
# 子序列长度为 1 ，所以我们返回 1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i], k <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        u = max(nums)
        mx = [0] * (4 * u)

        def modify(o: int, l: int, r: int, i: int, val: int) -> None:
            if l == r:
                mx[o] = val
                return
            m = (l + r) // 2
            if i <= m: modify(o * 2, l, m, i, val)
            else: modify(o * 2 + 1, m + 1, r, i, val)
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])

        # 返回区间 [L,R] 内的最大值
        def query(o: int, l: int, r: int, L: int, R: int) -> int:  # L 和 R 在整个递归过程中均不变，将其大写，视作常量
            if L <= l and r <= R: return mx[o]
            res = 0
            m = (l + r) // 2
            if L <= m: res = query(o * 2, l, m, L, R)
            if R > m: res = max(res, query(o * 2 + 1, m + 1, r, L, R))
            return res

        for x in nums:
            if x == 1:
                modify(1, 1, u, 1, 1)
            else:
                res = 1 + query(1, 1, u, max(x - k, 1), x - 1)
                modify(1, 1, u, x, res)
        return mx[1]
# @lc code=end

