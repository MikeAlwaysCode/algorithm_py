#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
# https://leetcode.cn/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (51.09%)
# Likes:    825
# Dislikes: 0
# Total Accepted:    183.7K
# Total Submissions: 359.6K
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
#
# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回
# 需要移除区间的最小数量，使剩余区间互不重叠 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 
# 
# 示例 2:
# 
# 
# 输入: intervals = [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 
# 
# 示例 3:
# 
# 
# 输入: intervals = [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
        
        return n - ans
        '''
        if not intervals:
            return 0
        
        intervals.sort()
        n = len(intervals)
        f = [1]

        for i in range(1, n):
            f.append(max((f[j] for j in range(i) if intervals[j][1] <= intervals[i][0]), default=0) + 1)

        return n - max(f)
        '''
# @lc code=end

