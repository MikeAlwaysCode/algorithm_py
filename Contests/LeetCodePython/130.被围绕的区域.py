#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode.cn/problems/surrounded-regions/description/
#
# algorithms
# Medium (46.08%)
# Likes:    889
# Dislikes: 0
# Total Accepted:    205.1K
# Total Submissions: 445.1K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X'
# 填充。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
# 
# 示例 2：
# 
# 
# 输入：board = [["X"]]
# 输出：[["X"]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n == board[i].length
# 1 
# board[i][j] 为 'X' 或 'O'
# 
# 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
        n, m = len(board), len(board[0])
        def dfs(x, y) -> None:
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != 'O':
                return
            board[x][y] = 'N'
            for dr, dc in DIR:
                nx, ny = x + dr, y + dc
                dfs(nx, ny)

                
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
        
        for j in range(1, m-1):
            dfs(0, j)
            dfs(n-1, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'N':
                    board[i][j] = 'O'
        '''
        def dfs1(x, y) -> bool:
            board[x][y] = '.'
            if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                return False
            for dr, dc in DIR:
                nx, ny = x + dr, y + dc
                # if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 'O':
                    chk = dfs1(nx, ny)
                    if not chk:
                        return chk
            return True
        
        def dfs2(x, y, res) -> None:
            board[x][y] = res
            for dr, dc in DIR:
                nx, ny = x + dr, y + dc
                if 0 <= nx < n and 0 <= ny < m and (board[nx][ny] == '.' or board[nx][ny] == 'O'):
                    board[nx][ny] == res
                    dfs2(nx, ny, res)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    chk = dfs1(i, j)
                    if chk:
                        res = 'X'
                    else:
                        res = 'N'
                    dfs2(i, j, res)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
        '''
# @lc code=end

