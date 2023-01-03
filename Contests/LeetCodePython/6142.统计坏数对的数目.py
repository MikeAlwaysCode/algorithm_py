#
# @lc app=leetcode.cn id=6142 lang=python3
#
# [6142] 统计坏数对的数目
#
# https://leetcode.cn/problems/count-number-of-bad-pairs/description/
#
# algorithms
# Medium (36.51%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 8.9K
# Testcase Example:  '[4,1,3,3]'
#
# 给你一个下标从 0 开始的整数数组 nums 。如果 i < j 且 j - i != nums[j] - nums[i] ，那么我们称 (i, j)
# 是一个 坏数对 。
# 
# 请你返回 nums 中 坏数对 的总数目。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [4,1,3,3]
# 输出：5
# 解释：数对 (0, 1) 是坏数对，因为 1 - 0 != 1 - 4 。
# 数对 (0, 2) 是坏数对，因为 2 - 0 != 3 - 4, 2 != -1 。
# 数对 (0, 3) 是坏数对，因为 3 - 0 != 3 - 4, 3 != -1 。
# 数对 (1, 2) 是坏数对，因为 2 - 1 != 3 - 1, 1 != 2 。
# 数对 (2, 3) 是坏数对，因为 3 - 2 != 3 - 3, 1 != 0 。
# 总共有 5 个坏数对，所以我们返回 5 。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,2,3,4,5]
# 输出：0
# 解释：没有坏数对。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 
# 
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        '''
        count = len(nums)
        d = dict()
        for i, n in enumerate(nums):
            t = n - i
            if t not in d:
                d[t] = 1
            else:
                d[t] += 1
        
        ans = 0
        for k, v in d.items():
            if v >= 2:
                ans += v * (v - 1) / 2
        return int(count * (count - 1) / 2 - ans)
        '''
        n = len(nums)
        ans = n * (n - 1) // 2
        cnt = Counter([x - i for i, x in enumerate(nums)])
        for v in cnt.values():
            ans -= v * (v - 1) // 2
        return ans
# @lc code=end

