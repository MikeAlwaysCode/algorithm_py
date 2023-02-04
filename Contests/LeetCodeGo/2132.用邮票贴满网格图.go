/*
 * @lc app=leetcode.cn id=2132 lang=golang
 *
 * [2132] 用邮票贴满网格图
 *
 * https://leetcode.cn/problems/stamping-the-grid/description/
 *
 * algorithms
 * Hard (29.18%)
 * Likes:    45
 * Dislikes: 0
 * Total Accepted:    2.5K
 * Total Submissions: 8.5K
 * Testcase Example:  '[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]\n4\n3'
 *
 * 给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。
 *
 * 给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：
 *
 *
 * 覆盖所有 空 格子。
 * 不覆盖任何 被占据 的格子。
 * 我们可以放入任意数目的邮票。
 * 邮票可以相互有 重叠 部分。
 * 邮票不允许 旋转 。
 * 邮票必须完全在矩阵 内 。
 *
 *
 * 如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight =
 * 4, stampWidth = 3
 * 输出：true
 * 解释：我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2,
 * stampWidth = 2
 * 输出：false
 * 解释：没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == grid.length
 * n == grid[r].length
 * 1 <= m, n <= 10^5
 * 1 <= m * n <= 2 * 10^5
 * grid[r][c] 要么是 0 ，要么是 1 。
 * 1 <= stampHeight, stampWidth <= 10^5
 *
 *
 */

// @lc code=start
func possibleToStamp(grid [][]int, stampHeight int, stampWidth int) bool {
	m, n := len(grid), len(grid[0])
	sum := make([][]int, m+1)
	sum[0] = make([]int, n+1)
	diff := make([][]int, m+1)
	diff[0] = make([]int, n+1)
	for i, row := range grid {
		sum[i+1] = make([]int, n+1)
		for j, v := range row { // grid 的二维前缀和
			sum[i+1][j+1] = sum[i+1][j] + sum[i][j+1] - sum[i][j] + v
		}
		diff[i+1] = make([]int, n+1)
	}

	for i, row := range grid {
		for j, v := range row {
			if v == 0 {
				x, y := i+stampHeight, j+stampWidth // 注意这是矩形右下角横纵坐标都 +1 后的位置
				if x <= m && y <= n && sum[x][y]-sum[x][j]-sum[i][y]+sum[i][j] == 0 {
					diff[i][j]++
					diff[i][y]--
					diff[x][j]--
					diff[x][y]++ // 更新二维差分
				}
			}
		}
	}

	// 还原二维差分矩阵对应的计数矩阵，这里用滚动数组实现
	cnt := make([]int, n+1)
	pre := make([]int, n+1)
	for i, row := range grid {
		for j, v := range row {
			cnt[j+1] = cnt[j] + pre[j+1] - pre[j] + diff[i][j]
			if cnt[j+1] == 0 && v == 0 {
				return false
			}
		}
		cnt, pre = pre, cnt
	}
	return true
}

// @lc code=end

