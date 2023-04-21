#
# @lc app=leetcode.cn id=1723 lang=python3
#
# [1723] 完成所有工作的最短时间
#
# https://leetcode.cn/problems/find-minimum-time-to-finish-all-jobs/description/
#
# algorithms
# Hard (50.84%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    30.5K
# Total Submissions: 60K
# Testcase Example:  '[3,2,3]\n3'
#
# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
# 
# 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间
# 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
# 
# 返回分配方案中尽可能 最小 的 最大工作时间 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#
from typing import List


# @lc code=start
subsets = [[] for _ in range(1 << 12)]
for i in range(1 << 12):
    s = i
    while s:
        subsets[i].append(s)
        s = (s - 1) & i

class Solution:
    def minimumTimeRequired(self, cookies: List[int], k: int) -> int:
        m = 1 << len(cookies)
        SUM = [0] * m
        for i, v in enumerate(cookies):
            bit = 1 << i
            for j in range(bit):
                SUM[bit | j] = SUM[j] + v

        f = SUM.copy()
        for _ in range(1, k):
            for j in range(m - 1, 0, -1):
                for s in subsets[j]:
                    v = f[j ^ s]
                    if SUM[s] > v: v = SUM[s]  # 不要用 max 和 min，那样会有额外的函数调用开销
                    if v < f[j]: f[j] = v
        return f[-1]
# @lc code=end

