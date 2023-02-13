#
# @lc app=leetcode.cn id=1851 lang=python3
#
# [1851] 包含每个查询的最小区间
#
# https://leetcode.cn/problems/minimum-interval-to-include-each-query/description/
#
# algorithms
# Hard (43.23%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 7.4K
# Testcase Example:  '[[1,4],[2,4],[3,6],[4,4]]\n[2,3,4,5]'
#
# 给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示第 i 个区间开始于 lefti
# 、结束于 righti（包含两侧取值，闭区间）。区间的 长度 定义为区间中包含的整数数目，更正式地表达是 righti - lefti + 1 。
# 
# 再给你一个整数数组 queries 。第 j 个查询的答案是满足 lefti i 的 长度最小区间 i 的长度 。如果不存在这样的区间，那么答案是 -1
# 。
# 
# 以数组形式返回对应查询的所有答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
# 输出：[3,3,1,4]
# 解释：查询处理如下：
# - Query = 2 ：区间 [2,4] 是包含 2 的最小区间，答案为 4 - 2 + 1 = 3 。
# - Query = 3 ：区间 [2,4] 是包含 3 的最小区间，答案为 4 - 2 + 1 = 3 。
# - Query = 4 ：区间 [4,4] 是包含 4 的最小区间，答案为 4 - 4 + 1 = 1 。
# - Query = 5 ：区间 [3,6] 是包含 5 的最小区间，答案为 6 - 3 + 1 = 4 。
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
# 输出：[2,-1,4,6]
# 解释：查询处理如下：
# - Query = 2 ：区间 [2,3] 是包含 2 的最小区间，答案为 3 - 2 + 1 = 2 。
# - Query = 19：不存在包含 19 的区间，答案为 -1 。
# - Query = 5 ：区间 [2,5] 是包含 5 的最小区间，答案为 5 - 2 + 1 = 4 。
# - Query = 22：区间 [20,25] 是包含 22 的最小区间，答案为 25 - 20 + 1 = 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# queries[i].length == 2
# 1 i i 
# 1 
# 
# 
#
import bisect
from typing import List


# @lc code=start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[1] - x[0])

        m = len(queries)
        fa = list(range(m + 1))
        def find(x: int):
            cur = x
            while x != fa[x]:
                x = fa[x]
            if cur != x:
                fa[cur] = x
            return x
        def union(fr: int, to: int):
            fa[find(fr)] = find(to)

        ans = [-1] * m
        idx = sorted(range(m), key = lambda x: queries[x])
        # print(idx)
        for l, r in intervals:
            length = r - l + 1
            i = bisect.bisect_left(idx, l, key = lambda x: queries[x])
            # print(i)
            i = find(i)
            # print(l, i)
            while i < m and queries[idx[i]] <= r:
                ans[idx[i]] = length
                union(i, i + 1)
                i = find(i + 1)
        return ans
# @lc code=end

