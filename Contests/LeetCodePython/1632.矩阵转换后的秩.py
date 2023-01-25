#
# @lc app=leetcode.cn id=1632 lang=python3
#
# [1632] 矩阵转换后的秩
#
# https://leetcode.cn/problems/rank-transform-of-a-matrix/description/
#
# algorithms
# Hard (35.05%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 9.3K
# Testcase Example:  '[[1,2],[3,4]]'
#
# 给你一个 m x n 的矩阵 matrix ，请你返回一个新的矩阵 answer ，其中 answer[row][col] 是
# matrix[row][col] 的秩。
# 
# 每个元素的 秩 是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算：
# 
# 
# 秩是从 1 开始的一个整数。
# 如果两个元素 p 和 q 在 同一行 或者 同一列 ，那么：
# 
# 如果 p < q ，那么 rank(p) < rank(q)
# 如果 p == q ，那么 rank(p) == rank(q)
# 如果 p > q ，那么 rank(p) > rank(q)
# 
# 
# 秩 需要越 小 越好。
# 
# 
# 题目保证按照上面规则 answer 数组是唯一的。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2],[3,4]]
# 输出：[[1,2],[2,3]]
# 解释：
# matrix[0][0] 的秩为 1 ，因为它是所在行和列的最小整数。
# matrix[0][1] 的秩为 2 ，因为 matrix[0][1] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
# matrix[1][0] 的秩为 2 ，因为 matrix[1][0] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
# matrix[1][1] 的秩为 3 ，因为 matrix[1][1] > matrix[0][1]， matrix[1][1] >
# matrix[1][0] 且 matrix[0][1] 和 matrix[1][0] 的秩都为 2 。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[7,7],[7,7]]
# 输出：[[1,1],[1,1]]
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# 输出：[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
# 
# 
# 示例 4：
# 
# 
# 输入：matrix = [[7,3,6],[1,4,5],[9,8,2]]
# 输出：[[5,1,4],[1,2,3],[6,3,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -10^9 
# 
# 
#
from collections import deque
from typing import List


# @lc code=start
class Solution: 
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]: 
        LIM = 512
        R, C = len(matrix), len(matrix[0])
        res = [[0]*C for _ in range(R)]
        countR, countC = [0]*R, [0]*C
        
        # 按元素大小分别存储元素坐标
        ls = collections.defaultdict(list)
        for r, row in enumerate(matrix): 
            for c, val in enumerate(row): 
                ls[val].append((r, c))
                
        # 并查集用于合并行或列相同的元素
        union = list(range(LIM*2))
        def find(i): 
            if union[i] == i: return i
            union[i] = find(union[i])
            return union[i]
        
        # 按val从小到大遍历
        pool = collections.defaultdict(list)
        for val in sorted(ls.keys()): 

            # 用并查集合并行和列相同的元素并分组
            for r, c in ls[val]: 
                union[find(r)] = find(c+LIM)
            pool.clear()
            for r, c in ls[val]: 
                pool[find(r)].append((r, c))

                
            # 行和列相同的元素，共享相同的rank
            for group in pool.values(): 
                rank = max(max((countR[r], countC[c])) for r, c in group) + 1
                for r, c in group: 
                    countR[r] = countC[c] = res[r][c] = rank
                    # 重置并查集
                    union[r] = r
                    union[c+LIM] = c+LIM
        return res
'''
class UnionFind:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.root = [[[i, j] for j in range(n)] for i in range(m)]
        self.size = [[1] * n for _ in range(m)]

    def find(self, i, j):
        ri, rj = self.root[i][j]
        if [ri, rj] == [i, j]:
            return [i, j]
        self.root[i][j] = self.find(ri, rj)
        return self.root[i][j]

    def union(self, i1, j1, i2, j2):
        ri1, rj1 = self.find(i1, j1)
        ri2, rj2 = self.find(i2, j2)
        if [ri1, rj1] != [ri2, rj2]:
            if self.size[ri1][rj1] >= self.size[ri2][rj2]:
                self.root[ri2][rj2] = [ri1, rj1]
                self.size[ri1][rj1] += self.size[ri2][rj2]
            else:
                self.root[ri1][rj1] = [ri2, rj2]
                self.size[ri2][rj2] += self.size[ri1][rj1]

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])

        uf = UnionFind(n, m)

        idx = list(range(m))
        for i in range(n):
            idx.sort(key = lambda x: matrix[i][x])
            prej = idx[0]
            for nxtj in idx[1:]:
                if matrix[i][nxtj] == matrix[i][prej]:
                    uf.union(i, prej, i, nxtj)
                else:
                    prej = nxtj
        
        idx = list(range(n))
        for j in range(m):
            idx.sort(key = lambda x: matrix[x][j])
            prei = idx[0]
            for nxti in idx[1:]:
                uprei, uprej = uf.find(prei, j)
                unxti, unxtj = uf.find(nxti, j)
                if matrix[nxti][j] == matrix[prei][j]:
                    uf.union(uprei, uprej, unxti, unxtj)
                else:
                    prei = nxti
                    
        incnt = [[0] * m for _ in range(n)]
        edge = [[[] for _ in range(m)] for _ in range(n)]
        
        idx = list(range(m))
        for i in range(n):
            idx.sort(key = lambda x: matrix[i][x])
            prej = idx[0]
            for nxtj in idx[1:]:
                if matrix[i][nxtj] != matrix[i][prej]:
                    uprei, uprej = uf.find(i, prej)
                    unxti, unxtj = uf.find(i, nxtj)
                    incnt[unxti][unxtj] += 1
                    edge[uprei][uprej].append((unxti, unxtj))
                    prej = nxtj
        
        idx = list(range(n))
        for j in range(m):
            idx.sort(key = lambda x: matrix[x][j])
            prei = idx[0]
            for nxti in idx[1:]:
                if matrix[nxti][j] != matrix[prei][j]:
                    uprei, uprej = uf.find(prei, j)
                    unxti, unxtj = uf.find(nxti, j)
                    incnt[unxti][unxtj] += 1
                    edge[uprei][uprej].append((unxti, unxtj))
                    prei = nxti
        # print(edge[1][1])
        # print(edge[2][1])
        ans = [[1] * m for _ in range(n)]
        q = deque((i, j) for i, row in enumerate(incnt) for j, v in enumerate(row) if v == 0)
        # print(incnt)
        while q:
            i, j = q.popleft()
            
            for nxti, nxtj in edge[i][j]:
                incnt[nxti][nxtj] -= 1
                
                if incnt[nxti][nxtj] == 0:
                    ans[nxti][nxtj] = max(ans[nxti][nxtj], ans[i][j] + 1)
                    q.append((nxti, nxtj))
        
        for i in range(n):
            for j in range(m):
                ui, uj = uf.find(i, j)
                ans[i][j] = ans[ui][uj]
        
        return ans
'''
# @lc code=end

