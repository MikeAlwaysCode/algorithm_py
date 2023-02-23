/*
 * @lc app=leetcode.cn id=1140 lang=golang
 *
 * [1140] 石子游戏 II
 *
 * https://leetcode.cn/problems/stone-game-ii/description/
 *
 * algorithms
 * Medium (66.26%)
 * Likes:    167
 * Dislikes: 0
 * Total Accepted:    11.4K
 * Total Submissions: 16.9K
 * Testcase Example:  '[2,7,9,4,4]'
 *
 * 爱丽丝和鲍勃继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。
 *
 * 爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，M = 1。
 *
 * 在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。
 *
 * 游戏一直持续到所有石子都被拿走。
 *
 * 假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：piles = [2,7,9,4,4]
 * 输出：10
 * 解释：如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 =
 * 10堆。如果Alice一开始拿走了两堆，那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。
 *
 *
 * 示例 2:
 *
 *
 * 输入：piles = [1,2,3,4,5,100]
 * 输出：104
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= piles.length <= 100
 * 1 <= piles[i] <= 10^4
 *
 *
 */

// @lc code=start
func stoneGameII(piles []int) int {
	n := len(piles)
	s := 0
	dp := make([][]int, n)
	for i := n - 1; i >= 0; i-- {
		dp[i] = make([]int, n+1)
		s += piles[i]
		for m := 1; m <= i/2+1; m++ {
			if i+m*2 >= n {
				dp[i][m] = s
			} else {
				mn := math.MaxInt
				for j := 1; j <= m*2; j++ {
					mn = min(mn, dp[i+j][max(j, m)])
				}
				dp[i][m] = s - mn
			}
		}
	}
	return dp[0][1]

	// for i := n - 2; i >= 0; i-- {
	// 	s[i] += s[i+1] // 后缀和
	// }

	// cache := make([][]int, n-1)
	// for i := range cache {
	// 	cache[i] = make([]int, (n+1)/4+1)
	// 	for j := range cache[i] {
	// 		cache[i][j] = -1 // -1 表示没有访问过
	// 	}
	// }
	// var dfs func(int, int) int
	// dfs = func(i, m int) int {
	// 	if i+m*2 >= n {
	// 		return s[i]
	// 	}
	// 	v := &cache[i][m]
	// 	if *v != -1 {
	// 		return *v
	// 	}
	// 	mn := math.MaxInt
	// 	for x := 1; x <= m*2; x++ {
	// 		mn = min(mn, dfs(i+x, max(m, x)))
	// 	}
	// 	res := s[i] - mn
	// 	*v = res
	// 	return res
	// }
	// return dfs(0, 1)
}

func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

// @lc code=end

