#
# @lc app=leetcode.cn id=1349 lang=python3
#
# [1349] 参加考试的最大学生数
#
# https://leetcode.cn/problems/maximum-students-taking-exam/description/
#
# algorithms
# Hard (53.83%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    5.6K
# Total Submissions: 10.4K
# Testcase Example:  '[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]'
#
# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
# 
# 
# 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试且无法作弊的最大学生人数。
# 
# 学生必须坐在状况良好的座位上。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：seats = [["#",".","#","#",".","#"],
# [".","#","#","#","#","."],
# ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。 
# 
# 
# 示例 2：
# 
# 输入：seats = [[".","#"],
# ["#","#"],
# ["#","."],
# ["#","#"],
# [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。
# 
# 
# 示例 3：
# 
# 输入：seats = [["#",".",".",".","#"],
# [".","#",".","#","."],
# [".",".","#",".","."],
# [".","#",".","#","."],
# ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
# 
# 
# 
# 
# 提示：
# 
# 
# seats 只包含字符 '.' 和'#'
# m == seats.length
# n == seats[i].length
# 1 <= m <= 8
# 1 <= n <= 8
# 
# 
#
from functools import cache
from typing import List


# @lc code=start
class Solution:
    @cache
    def f(self, X, row_num, width):
        ans = 0
        for scheme in range(1 << width):
            if scheme & ~X or scheme & (scheme << 1):
                continue
            curans = 0
            for j in range(8):
                if (1 << j) & scheme:
                    curans += 1
            if row_num == len(self.seats) - 1:
                ans = max(ans, curans)
            else:
                next_seats = self.seats[row_num + 1]
                next_seats &= ~(scheme << 1)
                next_seats &= ~(scheme >> 1)
                ans = max(ans, curans + self.f(next_seats, row_num + 1, width))
        return ans

    def compress(self, row):
        ans = 0
        for c in row:
            ans <<= 1
            if c == '.':
                ans += 1
        return ans

    def maxStudents(self, seats: List[List[str]]) -> int:
        self.seats = [self.compress(row) for row in seats]
        return self.f(self.seats[0], 0, len(seats[0]))
# @lc code=end

