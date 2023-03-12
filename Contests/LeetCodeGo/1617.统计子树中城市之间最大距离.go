/*
 * @lc app=leetcode.cn id=1617 lang=golang
 *
 * [1617] 统计子树中城市之间最大距离
 *
 * https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/description/
 *
 * algorithms
 * Hard (65.18%)
 * Likes:    72
 * Dislikes: 0
 * Total Accepted:    4.1K
 * Total Submissions: 5.7K
 * Testcase Example:  '4\n[[1,2],[2,3],[2,4]]'
 *
 * 给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui
 * 和 vi 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。
 *
 * 一棵 子树
 * 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。
 *
 * 对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。
 *
 * 请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。
 *
 * 请注意，两个城市间距离定义为它们之间需要经过的边的数目。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：n = 4, edges = [[1,2],[2,3],[2,4]]
 * 输出：[3,4,0]
 * 解释：
 * 子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
 * 子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
 * 不存在城市间最大距离为 3 的子树。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 2, edges = [[1,2]]
 * 输出：[1]
 *
 *
 * 示例 3：
 *
 *
 * 输入：n = 3, edges = [[1,2],[2,3]]
 * 输出：[2,1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2
 * edges.length == n-1
 * edges[i].length == 2
 * 1 i, vi
 * 题目保证 (ui, vi) 所表示的边互不相同。
 *
 *
 */

// @lc code=start
func countSubgraphsForEachDiameter(n int, edges [][]int) []int {
	// 建树
	g := make([][]int, n)
	for _, e := range edges {
		x, y := e[0]-1, e[1]-1 // 编号改为从 0 开始
		g[x] = append(g[x], y)
		g[y] = append(g[y], x)
	}

	// 计算树上任意两点的距离
	dis := make([][]int, n)
	for i := range dis {
		// 计算 i 到其余点的距离
		dis[i] = make([]int, n)
		var dfs func(int, int)
		dfs = func(x, fa int) {
			for _, y := range g[x] {
				if y != fa {
					dis[i][y] = dis[i][x] + 1 // 自顶向下
					dfs(y, x)
				}
			}
		}
		dfs(i, -1)
	}

	ans := make([]int, n-1)
	for i, di := range dis {
		for j := i + 1; j < n; j++ {
			dj := dis[j]
			d := di[j]
			var dfs func(int, int) int
			dfs = func(x, fa int) int {
				// 能递归到这，说明 x 可以选
				cnt := 1 // 选 x
				for _, y := range g[x] {
					if y != fa &&
						(di[y] < d || di[y] == d && y > j) &&
						(dj[y] < d || dj[y] == d && y > i) { // 满足这些条件就可以选
						cnt *= dfs(y, x) // 每棵子树互相独立，采用乘法原理
					}
				}
				if di[x]+dj[x] > d { // x 是可选点
					cnt++ // 不选 x
				}
				return cnt
			}
			ans[d-1] += dfs(i, -1)
		}
	}
	return ans
}

// @lc code=end

