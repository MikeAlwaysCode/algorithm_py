/*
 * @lc app=leetcode.cn id=1411 lang=golang
 *
 * [1411] 给 N x 3 网格图涂色的方案数
 *
 * https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/description/
 *
 * algorithms
 * Hard (56.88%)
 * Likes:    110
 * Dislikes: 0
 * Total Accepted:    9.7K
 * Total Submissions: 17.1K
 * Testcase Example:  '1'
 *
 * 你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿
 * 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。
 *
 * 给你网格图的行数 n 。
 *
 * 请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 1
 * 输出：12
 * 解释：总共有 12 种可行的方法：
 *
 *
 *
 * 示例 2：
 *
 * 输入：n = 2
 * 输出：54
 *
 *
 * 示例 3：
 *
 * 输入：n = 3
 * 输出：246
 *
 *
 * 示例 4：
 *
 * 输入：n = 7
 * 输出：106494
 *
 *
 * 示例 5：
 *
 * 输入：n = 5000
 * 输出：30228214
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == grid.length
 * grid[i].length == 3
 * 1 <= n <= 5000
 *
 *
 */

// @lc code=start
func numOfWays(n int) int {
	MOD := int(1e9 + 7)
	c0, c1 := 6, 6
	for i := 1; i < n; i++ {
		n0 := (3*c0 + 2*c1) % MOD
		n1 := 2 * (c0 + c1) % MOD
		c0, c1 = n0, n1
	}
	return (c0 + c1) % MOD
}

// @lc code=end

