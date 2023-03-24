#
# @lc app=leetcode.cn id=1626 lang=python3
#
# [1626] 无矛盾的最佳球队
#
# https://leetcode.cn/problems/best-team-with-no-conflicts/description/
#
# algorithms
# Medium (41.85%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 21K
# Testcase Example:  '[1,3,5,10,15]\n[1,2,3,4,5]'
#
# 假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。
# 
# 然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于
# 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。
# 
# 给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回
# 所有可能的无矛盾球队中得分最高那支的分数 。
# 
# 
# 
# 示例 1：
# 
# 输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# 输出：34
# 解释：你可以选中所有球员。
# 
# 示例 2：
# 
# 输入：scores = [4,5,6,5], ages = [2,1,2,1]
# 输出：16
# 解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。
# 
# 
# 示例 3：
# 
# 输入：scores = [1,2,3,5], ages = [8,9,10,1]
# 输出：6
# 解释：最佳的选择是前 3 名球员。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= scores.length, ages.length <= 1000
# scores.length == ages.length
# 1 <= scores[i] <= 10^6
# 1 <= ages[i] <= 1000
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        u = max(ages)
        t = [0] * (u + 1)

        # 返回 max(max_sum[:i+1])
        def query(i: int) -> int:
            mx = 0
            while i:
                mx = max(mx, t[i])
                i &= i - 1
            return mx

        # 更新 max_sum[i] 为 mx
        def update(i: int, mx: int) -> None:
            while i < len(t):
                t[i] = max(t[i], mx)
                i += i & -i

        for score, age in sorted(zip(scores, ages)):
            update(age, query(age) + score)
        return query(u)
        '''
        max_sum = [0] * (max(ages) + 1)
        for score, age in sorted(zip(scores, ages)):
            max_sum[age] = max(max_sum[:age + 1]) + score
        return max(max_sum)
        '''
        '''
        a = sorted(zip(scores, ages))
        f = [0] * len(a)
        for i, (score, age) in enumerate(a):
            for j in range(i):
                if a[j][1] <= age:
                    f[i] = max(f[i], f[j])
            f[i] += score
        return max(f)
        '''
# @lc code=end

