#
# @lc app=leetcode.cn id=6143 lang=python3
#
# [6143] 预算内的最多机器人数目
#
# https://leetcode.cn/problems/maximum-number-of-robots-within-budget/description/
#
# algorithms
# Hard (22.33%)
# Likes:    0
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 4.8K
# Testcase Example:  '[3,6,1,3,4]\n[2,1,3,4,5]\n25'
#
# 你有 n 个机器人，给你两个下标从 0 开始的整数数组 chargeTimes 和 runningCosts ，两者长度都为 n 。第 i
# 个机器人充电时间为 chargeTimes[i] 单位时间，花费 runningCosts[i] 单位时间运行。再给你一个整数 budget 。
# 
# 运行 k 个机器人 总开销 是 max(chargeTimes) + k * sum(runningCosts) ，其中 max(chargeTimes)
# 是这 k 个机器人中最大充电时间，sum(runningCosts) 是这 k 个机器人的运行时间之和。
# 
# 请你返回在 不超过 budget 的前提下，你 最多 可以 连续 运行的机器人数目为多少。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
# 输出：3
# 解释：
# 可以在 budget 以内运行所有单个机器人或者连续运行 2 个机器人。
# 选择前 3 个机器人，可以得到答案最大值 3 。总开销是 max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 ，小于
# 25 。
# 可以看出无法在 budget 以内连续运行超过 3 个机器人，所以我们返回 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
# 输出：0
# 解释：即使运行任何一个单个机器人，还是会超出 budget，所以我们返回 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# chargeTimes.length == runningCosts.length == n
# 1 <= n <= 5 * 10^4
# 1 <= chargeTimes[i], runningCosts[i] <= 10^5
# 1 <= budget <= 10^15
# 
# 
#
from collections import deque
from typing import List
# @lc code=start
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        q = deque()
        ans = totCost = left = 0

        for right in range(n):
            if not q:
                left = right
            # 单调递减队列，队头即为最大值，进队前把前面小于等于当前值的都弹出
            while q and q[-1][0] <= chargeTimes[right]:
                q.pop()
            q.append((chargeTimes[right], right))
            totCost += runningCosts[right]

            while q and q[0][0] + (right - left + 1) * totCost > budget:
                if left == q[0][1]:
                    q.popleft()
                totCost -= runningCosts[left]
                left += 1
            
            if q:
                ans = max(ans, right - left + 1)
        return ans
# @lc code=end

