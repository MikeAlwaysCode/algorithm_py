#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode.cn/problems/jump-game-ii/description/
#
# algorithms
# Medium (45.16%)
# Likes:    1862
# Dislikes: 0
# Total Accepted:    420.2K
# Total Submissions: 930.7K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 
# 假设你总是可以到达数组的最后一个位置。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [2,3,0,1,4]
# 输出: 2
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# 0 
# 
# 
#
import bisect
from typing import List


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        mxPos = end = step = 0
        for i in range(n - 1):
            if mxPos >= i:
                mxPos = max(mxPos, i + nums[i])
                if i == end:
                    end = mxPos
                    step += 1
        return step
        '''
        stk = [0]
        d = {0: 0}
        for i in range(n - 1):
            if i + nums[i] > stk[-1]:
                j = bisect.bisect_left(stk, i)
                stk.append(i + nums[i])
                d[i + nums[i]] = d[stk[j]] + 1
        j = bisect.bisect_left(stk, n - 1)
        return d[stk[j]]
        '''
# @lc code=end

