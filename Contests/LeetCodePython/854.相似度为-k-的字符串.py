#
# @lc app=leetcode.cn id=854 lang=python3
#
# [854] 相似度为 K 的字符串
#
# https://leetcode.cn/problems/k-similar-strings/description/
#
# algorithms
# Hard (37.16%)
# Likes:    167
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 22.3K
# Testcase Example:  '"ab"\n"ba"'
#
# 对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。
# 
# 给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "ab", s2 = "ba"
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：s1 = "abc", s2 = "bca"
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s1.length <= 20
# s2.length == s1.length
# s1 和 s2  只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母
# s2 是 s1 的一个字母异位词
# 
# 
#
from collections import deque
from heapq import heappop, heappush
# @lc code=start
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # A* 算法（进阶）

        # A* 搜索算法（A* 读作 A-star），简称 A* 算法，是一种在图形平面上，对于有多个节点的路径求出最低通过成本的算法。它属于图遍历和最佳优先搜索算法（英文：Best-first search），亦是 BFS 的改进。

        # A* 算法主要步骤如下：

        # 1. 将方法一中的 BFS 队列转换为优先队列（小根堆）；
        # 2. 队列中的每个元素为 (dist[s] + f(s), s)，dist[s] 表示从初始状态 s1 到当前状态 s' 的距离，f(s) 表示从当前状态 s' 到目标状态 s2的估计距离，这两个距离之和作为堆排序的依据；
        # 3. 当终点第一次出队时，说明找到了从起点 s1 到终点 s2 的最短路径，直接返回对应的距离；
        # 4. f(s) 是估价函数，并且估价函数要满足 f(s) <= g(s)，其中 g(s) 表示 s' 到终点 s2 的真实距离；
        # 需要注意的是，A* 算法只能保证终点第一次出队时，即找到了一条从起点到终点的最小路径，不能保证其他点出队时也是从起点到当前点的最短路径。
        def f(s):
            cnt = sum(c != s2[i] for i, c in enumerate(s))
            return (cnt + 1) >> 1

        def next(s):
            i = 0
            while s[i] == s2[i]:
                i += 1
            res = []
            for j in range(i + 1, n):
                if s[j] == s2[i] and s[j] != s2[j]:
                    res.append(s2[: i + 1] + s[i + 1 : j] + s[i] + s[j + 1 :])
            return res

        q = [(f(s1), s1)]
        dist = {s1: 0}
        n = len(s1)
        while 1:
            _, s = heappop(q)
            if s == s2:
                return dist[s]
            for nxt in next(s):
                if nxt not in dist or dist[nxt] > dist[s] + 1:
                    dist[nxt] = dist[s] + 1
                    heappush(q, (dist[nxt] + f(nxt), nxt))
        '''
        # 62/62 cases passed (168 ms)
        # Your runtime beats 74.6 % of python3 submissions
        # Your memory usage beats 73.02 % of python3 submissions (16.1 MB)
        def next(s):
            i = 0
            while s[i] == s2[i]:
                i += 1
            res = []
            for j in range(i + 1, n):
                if s[j] == s2[i] and s[j] != s2[j]:
                    res.append(s2[: i + 1] + s[i + 1 : j] + s[i] + s[j + 1 :])
            return res

        q = deque([s1])
        vis = {s1}
        ans, n = 0, len(s1)
        while 1:
            for _ in range(len(q)):
                s = q.popleft()
                if s == s2:
                    return ans
                for nxt in next(s):
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append(nxt)
            ans += 1
        '''
        '''
        # BFS
        # 62/62 cases passed (160 ms)
        # Your runtime beats 77.78 % of python3 submissions
        # Your memory usage beats 55.56 % of python3 submissions (16.4 MB)
        step, n = 0, len(s1)
        q, vis = [(s1, 0)], {s1}
        while True:
            tmp = q
            q = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == s2[i] != s2[j]:  # 剪枝，只在 s[j] != s2[j] 时去交换
                        t = list(s)
                        t[i], t[j] = t[j], t[i]
                        t = ''.join(t)
                        if t not in vis:
                            vis.add(t)
                            q.append((t, i + 1))
            step += 1
        '''
        '''
        # DFS
        # 62/62 cases passed (56 ms)
        # Your runtime beats 84.13 % of python3 submissions
        # Your memory usage beats 98.41 % of python3 submissions (14.9 MB)
        s, t = [], []
        for x, y in zip(s1, s2):
            if x != y:
                s.append(x)
                t.append(y)
        n = len(s)
        if n == 0:
            return 0

        ans = n - 1
        def dfs(i: int, cost: int) -> None:
            nonlocal ans
            if cost > ans:
                return
            while i < n and s[i] == t[i]:
                i += 1
            if i == n:
                ans = min(ans, cost)
                return
            diff = sum(s[j] != t[j] for j in range(i, len(s)))
            min_swap = (diff + 1) // 2
            if cost + min_swap >= ans:  # 当前状态的交换次数下限大于等于当前的最小交换次数
                return
            for j in range(i + 1, n):
                if s[j] == t[i]:
                    s[i], s[j] = s[j], s[i]
                    dfs(i + 1, cost + 1)
                    s[i], s[j] = s[j], s[i]
        dfs(0, 0)
        return ans
        '''
# @lc code=end

