#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode.cn/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (43.03%)
# Likes:    900
# Dislikes: 0
# Total Accepted:    73.4K
# Total Submissions: 170.4K
# Testcase Example:  '[5,2,6,1]'
#
# 给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0] 
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [-1]
# 输出：[0]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [-1,-1]
# 输出：[0,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#
from typing import List
# @lc code=start
class Solution:
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

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.nums = nums
        n = len(nums)

        discretization = {v:i for i, v in enumerate(sorted(set(nums)))}

        self.n = len(discretization)
        self.BITree = [0] * (self.n + 1)
        
        res = [0] * n
        for i in range(n - 1, -1, -1):
            idx = discretization[nums[i]]
            res[i] = self.query(idx)
            self.add(idx+1, 1)

        return res
# @lc code=end

