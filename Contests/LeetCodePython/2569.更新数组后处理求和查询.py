#
# @lc app=leetcode.cn id=2569 lang=python3
#
# [2569] 更新数组后处理求和查询
#
# https://leetcode.cn/problems/handling-sum-queries-after-update/description/
#
# algorithms
# Hard (30.19%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 3.9K
# Testcase Example:  '[1,0,1]\n[0,0,0]\n[[1,1,1],[2,1,0],[3,0,0]]'
#
# 给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：
# 
# 
# 操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 或将 1 反转成
# 0 。l 和 r 下标都从 0 开始。
# 操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] +
# nums1[i] * p 。
# 操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
# 
# 
# 请你返回一个数组，包含所有第三种操作类型的答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
# 输出：[3]
# 解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3]
# 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
# 输出：[5]
# 解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length,nums2.length <= 10^5
# nums1.length = nums2.length
# 1 <= queries.length <= 10^5
# queries[i].length = 3
# 0 <= l <= r <= nums1.length - 1
# 0 <= p <= 10^6
# 0 <= nums1[i] <= 1
# 0 <= nums2[i] <= 10^9
# 
# 
#
from typing import List


# @lc code=start
class SegTree:
    def __init__(self, nums: list) -> None:
        n = len(nums)
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.build(nums, 1, 1, n)
        
    def build(self, nums: list, o: int, l: int, r: int) -> None:
        if l == r:
            self.tree[o] = nums[l - 1]
            return

        m = (l + r) >> 1
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
        self.pushUp(o)

    def xor(self, o: int, l: int, r: int) -> None:
        self.tree[o] = r - l + 1 - self.tree[o] # 异或反转
        self.lazy[o] ^= 1

    def pushUp(self, o: int) -> None:
        self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]

    def pushDown(self, o: int, l: int, r: int) -> None:
        m = (l + r) >> 1
        self.xor(o * 2, l, m)           # 调用相应的更新操作方法
        self.xor(o * 2 + 1, m + 1, r)
        self.lazy[o] = 0

    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:   # 当前区间已完全包含在更新区间，不需要继续往下更新，存在lazy
            self.xor(o, l, r)
            return

        if self.lazy[o]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o, l, r)

        m = (l + r) >> 1
        if m >= L:  # 左节点在更新区间
            self.update(o * 2, l, m, L, R, val)
        if m < R:   # 右节点在更新区间
            self.update(o * 2 + 1, m + 1, r, L, R, val)

        self.pushUp(o)  # 从左右节点更新当前节点值

    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if R < l or L > r:
            return 0

        if L <= l and r <= R:
            return self.tree[o]

        if self.lazy[o]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o, l, r)

        m = (l + r) >> 1
        res = 0
        if m >= L:  # 左节点在查询区间
            res += self.query(o * 2, l, m, L, R)
        if m < R:   # 右节点在查询区间
            res += self.query(o * 2 + 1, m + 1, r, L, R)

        return res
        
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        s = sum(nums2)
        st = SegTree(nums1)
        
        ans = []
        for op, l, r in queries:
            if op == 1:
                st.update(1, 1, n, l+1, r+1, 1)
            elif op == 2:
                s += l * st.query(1, 1, n, 1, n)
            else:
                ans.append(s)
        return ans
# @lc code=end

