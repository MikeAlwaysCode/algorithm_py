#
# @lc app=leetcode.cn id=1383 lang=python3
#
# [1383] 最大的团队表现值
#
# https://leetcode.cn/problems/maximum-performance-of-a-team/description/
#
# algorithms
# Hard (34.84%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 18K
# Testcase Example:  '6\n[2,10,3,1,5,8]\n[5,4,3,9,7,2]\n2'
#
# 公司有编号为 1 到 n 的 n 个工程师，给你两个数组 speed 和 efficiency ，其中 speed[i] 和 efficiency[i]
# 分别代表第 i 位工程师的速度和效率。请你返回由最多 k 个工程师组成的 ​​​​​​最大团队表现值 ，由于答案可能很大，请你返回结果对 10^9 + 7
# 取余后的结果。
# 
# 团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# 输出：60
# 解释：
# 我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为
# performance = (10 + 5) * min(4, 7) = 60 。
# 
# 
# 示例 2：
# 
# 输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# 输出：68
# 解释：
# 此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance =
# (2 + 10 + 5) * min(5, 4, 7) = 68 。
# 
# 
# 示例 3：
# 
# 输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# 输出：72
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^5
# speed.length == n
# efficiency.length == n
# 1 <= speed[i] <= 10^5
# 1 <= efficiency[i] <= 10^8
# 1 <= k <= n
# 
# 
#
from heapq import heappush, heapreplace
from typing import List


# @lc code=start
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        idx = sorted(range(n), key = lambda x: efficiency[x], reverse = True)
        ans = s = 0
        h = []
        for i in idx:
            if len(h) < k:
                s += speed[i]
                heappush(h, speed[i])
            elif speed[i] > h[0]:
                s += speed[i] - h[0]
                heapreplace(h, speed[i])
            #if len(h) == k:
            ans = max(ans, s * efficiency[i])
        return ans % (10**9+7)
# @lc code=end

