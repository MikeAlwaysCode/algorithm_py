#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode.cn/problems/combination-sum-ii/description/
#
# algorithms
# Medium (60.30%)
# Likes:    1153
# Dislikes: 0
# Total Accepted:    366.4K
# Total Submissions: 607.6K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 
# 注意：解集不能包含重复的组合。 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 示例 2:
# 
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# 提示:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#
import collections
from typing import List
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combine = []
        freq = sorted(collections.Counter(candidates).items())
        n = len(freq)
        
        def dfs(target: int, idx: int) -> None:
            nonlocal combine

            if target == 0:
                ans.append(combine[:])
                return

            if idx == n or target < freq[idx][0]:
                return
            
            dfs(target, idx + 1)

            most = min(freq[idx][1], target // freq[idx][0])
            for i in range(1, most+1):
                combine.append(freq[idx][0])
                dfs(target - i * freq[idx][0], idx + 1)
            combine = combine[:-most]

        dfs(target, 0)
        return ans
# @lc code=end

