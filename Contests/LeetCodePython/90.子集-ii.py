#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode.cn/problems/subsets-ii/description/
#
# algorithms
# Medium (63.67%)
# Likes:    953
# Dislikes: 0
# Total Accepted:    254.1K
# Total Submissions: 399.1K
# Testcase Example:  '[1,2,2]'
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0]
# 输出：[[],[0]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# 
# 
# 
# 
#
import itertools
from typing import List
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        path = []
        def backtrack(nums, idx):
            ans.append(path[:])
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()
        backtrack(nums, 0)
        return ans
        '''
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n+1):
            for p in itertools.combinations(nums, i):
                ans.add(p)
        return list(ans)
        '''
# @lc code=end

