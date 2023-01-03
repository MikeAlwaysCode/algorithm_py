#
# @lc app=leetcode.cn id=6134 lang=python3
#
# [6134] 找到离给定两个节点最近的节点
#
# https://leetcode.cn/problems/find-closest-node-to-given-two-nodes/description/
#
# algorithms
# Medium (25.27%)
# Likes:    2
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 16.4K
# Testcase Example:  '[2,2,3,-1]\n0\n1'
#
# 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，每个节点 至多 有一条出边。
# 
# 有向图用大小为 n 下标从 0 开始的数组 edges 表示，表示节点 i 有一条有向边指向 edges[i] 。如果节点 i 没有出边，那么
# edges[i] == -1 。
# 
# 同时给你两个节点 node1 和 node2 。
# 
# 请你返回一个从 node1 和 node2 都能到达节点的编号，使节点 node1 和节点 node2 到这个节点的距离
# 较大值最小化。如果有多个答案，请返回 最小 的节点编号。如果答案不存在，返回 -1 。
# 
# 注意 edges 可能包含环。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：edges = [2,2,3,-1], node1 = 0, node2 = 1
# 输出：2
# 解释：从节点 0 到节点 2 的距离为 1 ，从节点 1 到节点 2 的距离为 1 。
# 两个距离的较大值为 1 。我们无法得到一个比 1 更小的较大值，所以我们返回节点 2 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：edges = [1,2,-1], node1 = 0, node2 = 2
# 输出：2
# 解释：节点 0 到节点 2 的距离为 2 ，节点 2 到它自己的距离为 0 。
# 两个距离的较大值为 2 。我们无法得到一个比 2 更小的较大值，所以我们返回节点 2 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == edges.length
# 2 <= n <= 10^5
# -1 <= edges[i] < n
# edges[i] != i
# 0 <= node1, node2 < n
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n, min_dis, ans = len(edges), len(edges), -1
        def calc_dis(x: int) -> List[int]:
            dis = [n] * n
            d = 0
            while x >= 0 and dis[x] == n:
                dis[x] = d
                d += 1
                x = edges[x]
            return dis
        for i, d1, d2 in zip(range(n), calc_dis(node1), calc_dis(node2)):
            d = max(d1, d2)
            if d < min_dis:
                min_dis, ans = d, i
        return ans
        '''
        n = len(edges)
        s1, s2 = set([node1]), set([node2])
        l1, l2 = [0] * n, [0] * n
        cur = node1
        dis = 0
        while True:
            if edges[cur] == -1:
                break
            elif edges[cur] in s1:
                break
            else:
                s1.add(edges[cur])
                cur = edges[cur]
                dis += 1
                l1[cur] = dis
        cur = node2
        dis = 0
        while True:
            if edges[cur] == -1:
                break
            elif edges[cur] in s2:
                break
            else:
                s2.add(edges[cur])
                cur = edges[cur]
                dis += 1
                l2[cur] = dis
        s3 = s1 & s2
        l3 = list(s3)
        if len(l3) == 0:
            return -1
        elif len(l3) == 1:
            return l3[0]
        else:
            maxDis = n
            ans = l3[0]
            for x in l3:
                cd = max(l1[x], l2[x])
                if cd < maxDis:
                    ans = x
                    maxDis = cd
                elif cd == maxDis:
                    ans = min(ans, x)
            return ans
        '''
# @lc code=end

