#
# @lc app=leetcode.cn id=1353 lang=python3
#
# [1353] 最多可以参加的会议数目
#
# https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/description/
#
# algorithms
# Medium (29.50%)
# Likes:    244
# Dislikes: 0
# Total Accepted:    17.6K
# Total Submissions: 59.6K
# Testcase Example:  '[[1,2],[2,3],[3,4]]'
#
# 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于
# endDayi 。
# 
# 你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。注意，一天只能参加一个会议。
# 
# 请你返回你可以参加的 最大 会议数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：events = [[1,2],[2,3],[3,4]]
# 输出：3
# 解释：你可以参加所有的三个会议。
# 安排会议的一种方案如上图。
# 第 1 天参加第一个会议。
# 第 2 天参加第二个会议。
# 第 3 天参加第三个会议。
# 
# 
# 示例 2：
# 
# 
# 输入：events= [[1,2],[2,3],[3,4],[1,2]]
# 输出：4
# 
# 
# 
# 
# 提示：​​​​​​
# 
# 
# 1 <= events.length <= 10^5
# events[i].length == 2
# 1 <= startDayi <= endDayi <= 10^5
# 
# 
#
from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        h = []
        ans = curr = i = 0
        while i < len(events) or h:
            if h and (i >= len(events) or curr < events[i][0]):
                # 后续没有其他会议或者当前时间仍小于下一个会议的开始时间，则把之前入堆的会议出堆
                if heappop(h) >= curr:
                    # 结束时间大于等于当前时间
                    ans += 1
                    curr += 1
            elif i < len(events):
                # 下一个会议的结束时间入堆，当前时间设为下一个会议的开始时间
                heappush(h, events[i][1])
                curr = events[i][0]
                i += 1
        return ans
# @lc code=end

