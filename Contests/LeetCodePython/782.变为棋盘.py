#
# @lc app=leetcode.cn id=782 lang=python3
#
# [782] 变为棋盘
#
# https://leetcode.cn/problems/transform-to-chessboard/description/
#
# algorithms
# Hard (57.49%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    6.9K
# Total Submissions: 12K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]'
#
# 一个 n x n 的二维网络 board 仅由 0 和 1 组成 。每次移动，你能任意交换两列或是两行的位置。
# 
# 返回 将这个矩阵变为  “棋盘”  所需的最小移动次数 。如果不存在可行的变换，输出 -1。
# 
# “棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# 输出: 2
# 解释:一种可行的变换方式如下，从左到右：
# 第一次移动交换了第一列和第二列。
# 第二次移动交换了第二行和第三行。
# 
# 
# 示例 2:
# 
# 
# 
# 
# 输入: board = [[0, 1], [1, 0]]
# 输出: 0
# 解释: 注意左上角的格值为0时也是合法的棋盘，也是合法的棋盘.
# 
# 
# 示例 3:
# 
# 
# 
# 
# 输入: board = [[1, 0], [1, 0]]
# 输出: -1
# 解释: 任意的变换都不能使这个输入变为合法的棋盘。
# 
# 
# 
# 
# 提示：
# 
# 
# n == board.length
# n == board[i].length
# 2 <= n <= 30
# board[i][j] 将只包含 0或 1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # 棋盘的第一行与第一列
        rowMask = colMask = 0
        for i in range(n):
            rowMask |= board[0][i] << i
            colMask |= board[i][0] << i
        reverseRowMask = ((1 << n) - 1) ^ rowMask
        reverseColMask = ((1 << n) - 1) ^ colMask
        rowCnt = colCnt = 0
        for i in range(n):
            currRowMask = currColMask = 0
            for j in range(n):
                currRowMask |= board[i][j] << j
                currColMask |= board[j][i] << j
            # 检测每一行和每一列的状态是否合法
            if currRowMask != rowMask and currRowMask != reverseRowMask or \
               currColMask != colMask and currColMask != reverseColMask:
                return -1
            rowCnt += currRowMask == rowMask  # 记录与第一行相同的行数
            colCnt += currColMask == colMask  # 记录与第一列相同的列数

        def getMoves(mask: int, count: int) -> int:
            ones = mask.bit_count()
            if n & 1:
                # 如果 n 为奇数，则每一行中 1 与 0 的数目相差为 1，且满足相邻行交替
                if abs(n - 2 * ones) != 1 or abs(n - 2 * count) != 1:
                    return -1
                if ones == n // 2:
                    # 偶数位变为 1 的最小交换次数
                    return n // 2 - (mask & 0xAAAAAAAA).bit_count()
                else:
                    # 奇数位变为 1 的最小交换次数
                    return (n + 1) // 2 - (mask & 0x55555555).bit_count()
            else:
                # 如果 n 为偶数，则每一行中 1 与 0 的数目相等，且满足相邻行交替
                if ones != n // 2 or count != n // 2:
                    return -1
                # 偶数位变为 1 的最小交换次数
                count0 = n // 2 - (mask & 0xAAAAAAAA).bit_count()
                # 奇数位变为 1 的最小交换次数
                count1 = n // 2 - (mask & 0x55555555).bit_count()
                return min(count0, count1)

        rowMoves = getMoves(rowMask, rowCnt)
        colMoves = getMoves(colMask, colCnt)
        return -1 if rowMoves == -1 or colMoves == -1 else rowMoves + colMoves
# @lc code=end

