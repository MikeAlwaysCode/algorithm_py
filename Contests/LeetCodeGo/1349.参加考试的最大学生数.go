/*
 * @lc app=leetcode.cn id=1349 lang=golang
 *
 * [1349] 参加考试的最大学生数
 *
 * https://leetcode.cn/problems/maximum-students-taking-exam/description/
 *
 * algorithms
 * Hard (53.83%)
 * Likes:    152
 * Dislikes: 0
 * Total Accepted:    5.6K
 * Total Submissions: 10.4K
 * Testcase Example:  '[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]'
 *
 * 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
 *
 *
 * 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试且无法作弊的最大学生人数。
 *
 * 学生必须坐在状况良好的座位上。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：seats = [["#",".","#","#",".","#"],
 * [".","#","#","#","#","."],
 * ["#",".","#","#",".","#"]]
 * 输出：4
 * 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。
 *
 *
 * 示例 2：
 *
 * 输入：seats = [[".","#"],
 * ["#","#"],
 * ["#","."],
 * ["#","#"],
 * [".","#"]]
 * 输出：3
 * 解释：让所有学生坐在可用的座位上。
 *
 *
 * 示例 3：
 *
 * 输入：seats = [["#",".",".",".","#"],
 * [".","#",".","#","."],
 * [".",".","#",".","."],
 * [".","#",".","#","."],
 * ["#",".",".",".","#"]]
 * 输出：10
 * 解释：让学生坐在第 1、3 和 5 列的可用座位上。
 *
 *
 *
 *
 * 提示：
 *
 *
 * seats 只包含字符 '.' 和'#'
 * m == seats.length
 * n == seats[i].length
 * 1 <= m <= 8
 * 1 <= n <= 8
 *
 *
 */

// @lc code=start
func maxStudents(seats [][]byte) (ans int) {
	m, n := len(seats), len(seats[0])
	mm := 1 << uint(n)
	ss, f := make([]int, m+1), make([]int, mm)
	ss[0] = 0
	for i := range seats {
		for j := range seats[i] {
			if seats[i][j] == '.' {
				ss[i+1] |= 1 << uint(j)
			}
		}
	}
	preMax := 0
	for i := 1; i <= m; i++ {
		ff := make([]int, mm)
		for mask := 0; mask < mm; mask++ {
			ff[mask] = preMax
			curMax := 0
			if mask&ss[i] == mask && mask<<1&mask == 0 {
				preMask := (mask<<1 ^ ss[i-1]) & (ss[i-1] ^ mask>>1)
				curCnt := bits.OnesCount(uint(mask))
				curMax = max(curMax, f[preMask])
				for sub := preMask; sub > 0; sub = (sub - 1) & preMask {
					curMax = max(curMax, f[sub])
				}
				ff[mask] = max(ff[mask], curMax+curCnt)
			}
			ans = max(ans, ff[mask])
		}
		preMax = ans
		f = ff
	}

	return
}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}

// @lc code=end

