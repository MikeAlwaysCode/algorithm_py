/*
 * @lc app=leetcode.cn id=1494 lang=golang
 *
 * [1494] 并行课程 II
 *
 * https://leetcode.cn/problems/parallel-courses-ii/description/
 *
 * algorithms
 * Hard (40.61%)
 * Likes:    110
 * Dislikes: 0
 * Total Accepted:    4.3K
 * Total Submissions: 10.7K
 * Testcase Example:  '4\n[[2,1],[3,1],[1,4]]\n2'
 *
 * 给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 relations 中， relations[i] = [xi, yi]
 * 表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。
 *
 * 在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。
 *
 * 请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
 * 输出：3
 * 解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
 *
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入：n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
 * 输出：4
 * 解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：n = 11, relations = [], k = 2
 * 输出：6
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 15
 * 1 <= k <= n
 * 0 <= relations.length <= n * (n-1) / 2
 * relations[i].length == 2
 * 1 <= xi, yi <= n
 * xi != yi
 * 所有先修关系都是不同的，也就是说 relations[i] != relations[j] 。
 * 题目输入的图是个有向无环图。
 *
 *
 */

// @lc code=start
func minNumberOfSemesters(n int, relations [][]int, k int) int {
	// 计算每门课的先修课集合
	pre := make([]int, n)
	for _, d := range relations {
		pre[d[1]-1] |= 1 << (d[0] - 1)
	}
	m := 1 << n
	// 计算所有课程集合的先修课集合，不合法的标记为 -1
	totPre := make([]int, m)
	for i := range totPre {
		if bits.OnesCount(uint(i)) > k {
			totPre[i] = -1
			continue
		}
		for s := uint(i); s > 0; s &= s - 1 {
			p := pre[bits.TrailingZeros(s)]
			if p&i > 0 {
				totPre[i] = -1
				break
			}
			totPre[i] |= p
		}
	}
	dp := make([]int, 1<<n)
	for i := range dp {
		dp[i] = n
	}
	dp[0] = 0
	for s, v := range dp {
		t := m - 1 ^ s                               // 补集
		for sub := t; sub > 0; sub = (sub - 1) & t { // 枚举下个学期要学的课
			if p := totPre[sub]; p >= 0 && s&p == p { // 这些课的先修课必须合法且在之前的学期里必须上过
				dp[s|sub] = min(dp[s|sub], v+1)
			}
		}
	}
	return dp[m-1]
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end

