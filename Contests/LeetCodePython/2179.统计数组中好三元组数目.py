#
# @lc app=leetcode.cn id=2179 lang=python3
#
# [2179] 统计数组中好三元组数目
#
# https://leetcode.cn/problems/count-good-triplets-in-an-array/description/
#
# algorithms
# Hard (37.08%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 9K
# Testcase Example:  '[2,0,1,3]\n[0,1,2,3]'
#
# 给你两个下标从 0 开始且长度为 n 的整数数组 nums1 和 nums2 ，两者都是 [0, 1, ..., n - 1] 的 排列 。
# 
# 好三元组 指的是 3 个 互不相同 的值，且它们在数组 nums1 和 nums2 中出现顺序保持一致。换句话说，如果我们将 pos1v 记为值 v 在
# nums1 中出现的位置，pos2v 为值 v 在 nums2 中的位置，那么一个好三元组定义为 0 <= x, y, z <= n - 1 ，且
# pos1x < pos1y < pos1z 和 pos2x < pos2y < pos2z 都成立的 (x, y, z) 。
# 
# 请你返回好三元组的 总数目 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [2,0,1,3], nums2 = [0,1,2,3]
# 输出：1
# 解释：
# 总共有 4 个三元组 (x,y,z) 满足 pos1x < pos1y < pos1z ，分别是 (2,0,1) ，(2,0,3) ，(2,1,3) 和
# (0,1,3) 。
# 这些三元组中，只有 (0,1,3) 满足 pos2x < pos2y < pos2z 。所以只有 1 个好三元组。
# 
# 
# 示例 2：
# 
# 输入：nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
# 输出：4
# 解释：总共有 4 个好三元组 (4,0,3) ，(4,0,2) ，(4,1,3) 和 (4,1,2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length == nums2.length
# 3 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= n - 1
# nums1 和 nums2 是 [0, 1, ..., n - 1] 的排列。
# 
# 
#
from typing import List


# @lc code=start
class BIT:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)
        self.n = n
        self.BITree = [0] * (self.n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = 0
        while x:
            ans += self.BITree[x]
            x -= self.lowbit(x)
        return ans

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += self.lowbit(x)

    def update(self, x: int, val: int) -> None:
        self.add(x + 1, val - self.nums[x])
        self.nums[x] = val

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        d = {v:i for i, v in enumerate(nums2)}
        ans = 0
        bit = BIT(n)
        for i, v in enumerate(nums1):
            j = d[v]
            less = bit.query(j)
            large = n - 1 - i - (j - less)
            ans += less * large
            bit.update(j, 1)
        return ans
        '''
        bit1 = BIT(n)
        bit2 = BIT(n)
        for v in nums1:
            i = d[v]
            ans += bit2.query(i)
            bit2.add(i + 1, bit1.query(i))
            bit1.update(i, 1)
        return ans
        '''
# @lc code=end

