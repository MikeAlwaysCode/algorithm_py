/*
 * @lc app=leetcode.cn id=85 lang=golang
 *
 * [85] 最大矩形
 *
 * https://leetcode.cn/problems/maximal-rectangle/description/
 *
 * algorithms
 * Hard (54.34%)
 * Likes:    1455
 * Dislikes: 0
 * Total Accepted:    163.3K
 * Total Submissions: 300.4K
 * Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
 *
 * 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：matrix =
 * [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
 * 输出：6
 * 解释：最大矩形如上图所示。
 *
 *
 * 示例 2：
 *
 *
 * 输入：matrix = []
 * 输出：0
 *
 *
 * 示例 3：
 *
 *
 * 输入：matrix = [["0"]]
 * 输出：0
 *
 *
 * 示例 4：
 *
 *
 * 输入：matrix = [["1"]]
 * 输出：1
 *
 *
 * 示例 5：
 *
 *
 * 输入：matrix = [["0","0"]]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * rows == matrix.length
 * cols == matrix[0].length
 * 1 <= row, cols <= 200
 * matrix[i][j] 为 '0' 或 '1'
 *
 *
 */

// @lc code=start
func maximalRectangle(matrix [][]byte) int {
	n, m := len(matrix), len(matrix[0])
	left := make([][]int, n)
	for i, row := range matrix {
		left[i] = make([]int, m)
		for j, v := range row {
			if v == '0' {
				continue
			}
			if j == 0 {
				left[i][j] = 1
			} else {
				left[i][j] = left[i][j-1] + 1
			}
		}
	}
	ans := 0
	up := make([]int, n)
	down := make([]int, n)

	for j := 0; j < m; j++ {
		for i := 0; i < n; i++ {
			up[i] = -1
			down[i] = n
		}
		stk := []int{}
		for i, l := range left {
			for len(stk) > 0 && left[stk[len(stk)-1]][j] >= l[j] {
				down[stk[len(stk)-1]] = i
				stk = stk[:len(stk)-1]
			}
			if len(stk) > 0 {
				up[i] = stk[len(stk)-1]
			}
			stk = append(stk, i)
		}
		for i, l := range left {
			ans = max(ans, l[j]*(down[i]-up[i]-1))
		}
	}
	return ans
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

