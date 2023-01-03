#
# @lc app=leetcode.cn id=6206 lang=python3
#
# [6206] 最长递增子序列 II
#
# https://leetcode.cn/problems/longest-increasing-subsequence-ii/description/
#
# algorithms
# Hard (17.32%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 9.3K
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
from typing import List
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
    '''
        tmp = SegmentTree([0] * (10 ** 5 + 1))
        for x in nums:
            note = tmp.query(max(0, x-k), x-1)
            tmp.update(x, note + 1)
        return tmp.query(0, 10 ** 5)
        
class SegmentTree:
    def __init__(self, data, merge=max): 
        self.data = data
        self.n = len(data)
        self.tree = [None] * (4 * self.n)
        self._merge = merge
        if self.n:
            self._build(0, 0, self.n-1)


    def query(self, ql, qr):
        return self._query(0, 0, self.n-1, ql, qr)

    def update(self, index, value):
        self.data[index] = value
        self._update(0, 0, self.n-1, index)

    def _build(self, tree_index, l, r):
        if l == r:
            self.tree[tree_index] = self.data[l]
            return
        mid = (l+r) // 2
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        self._build(left, l, mid)
        self._build(right, mid+1, r)
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])

    def _query(self, tree_index, l, r, ql, qr):
        if l == ql and r == qr:
            return self.tree[tree_index]

        mid = (l+r) // 2
        left, right = tree_index * 2 + 1, tree_index * 2 + 2
        if qr <= mid:
            return self._query(left, l, mid, ql, qr)
        elif ql > mid:
            return self._query(right, mid+1, r, ql, qr)

        return self._merge(self._query(left, l, mid, ql, mid), 
                          self._query(right, mid+1, r, mid+1, qr))

    def _update(self, tree_index, l, r, index):
        if l == r == index:
            self.tree[tree_index] = self.data[index]
            return
        mid = (l+r)//2
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        if index > mid:
            self._update(right, mid+1, r, index)
        else:
            self._update(left, l, mid, index)
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])
    '''
# @lc code=end

