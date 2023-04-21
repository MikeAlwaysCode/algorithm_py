#
# @lc app=leetcode.cn id=1986 lang=python3
#
# [1986] 完成任务的最少工作时间段
#
# https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/
#
# algorithms
# Medium (31.83%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    6.2K
# Total Submissions: 19.4K
# Testcase Example:  '[1,2,3]\n3'
#
# 你被安排了 n 个任务。任务需要花费的时间用长度为 n 的整数数组 tasks 表示，第 i 个任务需要花费 tasks[i] 小时完成。一个 工作时间段
# 中，你可以 至多 连续工作 sessionTime 个小时，然后休息一会儿。
# 
# 你需要按照如下条件完成给定任务：
# 
# 
# 如果你在某一个时间段开始一个任务，你需要在 同一个 时间段完成它。
# 完成一个任务后，你可以 立马 开始一个新的任务。
# 你可以按 任意顺序 完成任务。
# 
# 
# 给你 tasks 和 sessionTime ，请你按照上述要求，返回完成所有任务所需要的 最少 数目的 工作时间段 。
# 
# 测试数据保证 sessionTime 大于等于 tasks[i] 中的 最大值 。
# 
# 
# 
# 示例 1：
# 
# 输入：tasks = [1,2,3], sessionTime = 3
# 输出：2
# 解释：你可以在两个工作时间段内完成所有任务。
# - 第一个工作时间段：完成第一和第二个任务，花费 1 + 2 = 3 小时。
# - 第二个工作时间段：完成第三个任务，花费 3 小时。
# 
# 
# 示例 2：
# 
# 输入：tasks = [3,1,3,1,1], sessionTime = 8
# 输出：2
# 解释：你可以在两个工作时间段内完成所有任务。
# - 第一个工作时间段：完成除了最后一个任务以外的所有任务，花费 3 + 1 + 3 + 1 = 8 小时。
# - 第二个工作时间段，完成最后一个任务，花费 1 小时。
# 
# 
# 示例 3：
# 
# 输入：tasks = [1,2,3,4,5], sessionTime = 15
# 输出：1
# 解释：你可以在一个工作时间段以内完成所有任务。
# 
# 
# 
# 
# 提示：
# 
# 
# n == tasks.length
# 1 <= n <= 14
# 1 <= tasks[i] <= 10
# max(tasks[i]) <= sessionTime <= 15
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        valid = [False] * (1 << n)
        for mask in range(1, 1 << n):
            needTime = 0
            for i in range(n):
                if mask & (1 << i):
                    needTime += tasks[i]
            if needTime <= sessionTime:
                valid[mask] = True

        f = [float("inf")] * (1 << n)
        f[0] = 0
        for mask in range(1, 1 << n):
            subset = mask
            while subset:
                if valid[subset]:
                    f[mask] = min(f[mask], f[mask ^ subset] + 1)
                subset = (subset - 1) & mask
        
        return f[(1 << n) - 1]
        '''
        n = len(tasks)
        f = [(float("inf"), float("inf"))] * (1 << n)
        f[0] = (1, 0)

        def add(o: Tuple[int, int], x: int) -> Tuple[int, int]:
            if o[1] + x <= sessionTime:
                return o[0], o[1] + x
            return o[0] + 1, x
        
        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    f[mask] = min(f[mask], add(f[mask ^ (1 << i)], tasks[i]))
        
        return f[(1 << n) - 1][0]
        '''
# @lc code=end

