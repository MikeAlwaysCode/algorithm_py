/*
 * @lc app=leetcode.cn id=1931 lang=golang
 *
 * [1931] 用三种不同颜色为网格涂色
 *
 * https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/description/
 *
 * algorithms
 * Hard (58.91%)
 * Likes:    40
 * Dislikes: 0
 * Total Accepted:    3.1K
 * Total Submissions: 5.2K
 * Testcase Example:  '1\n1'
 *
 * 给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝
 * 三种颜色为每个单元格涂色。所有单元格都需要被涂色。
 *
 * 涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 10^9 + 7 取余 的结果。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：m = 1, n = 1
 * 输出：3
 * 解释：如上图所示，存在三种可能的涂色方案。
 *
 *
 * 示例 2：
 *
 *
 * 输入：m = 1, n = 2
 * 输出：6
 * 解释：如上图所示，存在六种可能的涂色方案。
 *
 *
 * 示例 3：
 *
 *
 * 输入：m = 5, n = 5
 * 输出：580986
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 1
 *
 *
 */

// @lc code=start
const mod int = 1e9 + 7

func colorTheGrid(m, n int) (ans int) {
	m *= 2
	// 预处理所有合法状态：用四进制表示颜色
	valid := []int{}
outer:
	for mask := 0; mask < 1<<m; mask++ {
		pre := 0
		for j := 0; j < m; j += 2 {
			color := mask >> j & 3
			if color == 0 || color == pre { // 未涂色或相邻颜色相同
				continue outer
			}
			pre = color
		}
		valid = append(valid, mask)
	}

	// 预处理所有合法状态能转移到哪些合法状态（记录合法状态的下标）
	to := make([][]int, len(valid))
	for i, v := range valid {
		for j, w := range valid {
			chk := true
			for k := 0; k < m; k += 2 {
				if v>>k&3 == w>>k&3 {
					chk = false
					break
				}
			}
			if chk {
				to[i] = append(to[i], j)
			}
		}
	}

	// 滚动数组，用当前行更新下一行不同状态的方案数
	dp := make([]int, len(valid))
	for i := range dp {
		dp[i] = 1
	}
	for i := 1; i < n; i++ {
		tmp := dp
		dp = make([]int, len(valid))
		for j, dv := range tmp {
			for _, t := range to[j] {
				dp[t] = (dp[t] + dv) % mod
			}
		}
	}
	for _, dv := range dp {
		ans += dv
	}
	return ans % mod
}

// @lc code=end

