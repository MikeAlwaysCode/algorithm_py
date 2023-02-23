/*
 * @lc app=leetcode.cn id=115 lang=golang
 *
 * [115] 不同的子序列
 *
 * https://leetcode.cn/problems/distinct-subsequences/description/
 *
 * algorithms
 * Hard (52.51%)
 * Likes:    939
 * Dislikes: 0
 * Total Accepted:    121.3K
 * Total Submissions: 231.2K
 * Testcase Example:  '"rabbbit"\n"rabbit"'
 *
 * 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
 *
 * 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE"
 * 的一个子序列，而 "AEC" 不是）
 *
 * 题目数据保证答案符合 32 位带符号整数范围。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "rabbbit", t = "rabbit"
 * 输出：3
 * 解释：
 * 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
 * rabbbit
 * rabbbit
 * rabbbit
 *
 * 示例 2：
 *
 *
 * 输入：s = "babgbag", t = "bag"
 * 输出：5
 * 解释：
 * 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
 * babgbag
 * babgbag
 * babgbag
 * babgbag
 * babgbag
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * s 和 t 由英文字母组成
 *
 *
 */

// @lc code=start
func numDistinct(s string, t string) int {
	n, m := len(s), len(t)
	if n < m {
		return 0
	}
	dp := make([][]int, n+1)
	dp[0] = make([]int, m+1)
	for i := 0; i < n; i++ {
		dp[i+1] = make([]int, m+1)
		dp[i][0] = 1
		for j := 0; j <= i && j < m; j++ {
			dp[i+1][j+1] = dp[i][j+1]
			if s[i] == t[j] {
				dp[i+1][j+1] += dp[i][j]
			}
		}
	}
	return dp[n][m]
}

// @lc code=end

