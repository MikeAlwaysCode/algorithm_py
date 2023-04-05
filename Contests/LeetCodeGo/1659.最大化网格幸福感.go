/*
 * @lc app=leetcode.cn id=1659 lang=golang
 *
 * [1659] 最大化网格幸福感
 *
 * https://leetcode.cn/problems/maximize-grid-happiness/description/
 *
 * algorithms
 * Hard (44.23%)
 * Likes:    57
 * Dislikes: 0
 * Total Accepted:    2.1K
 * Total Submissions: 4.8K
 * Testcase Example:  '2\n3\n1\n2'
 *
 * 给你四个整数 m、n、introvertsCount 和 extrovertsCount 。有一个 m x n
 * 网格，和两种类型的人：内向的人和外向的人。总共有 introvertsCount 个内向的人和 extrovertsCount 个外向的人。
 *
 * 请你决定网格中应当居住多少人，并为每个人分配一个网格单元。 注意，不必 让所有人都生活在网格中。
 *
 * 每个人的 幸福感 计算如下：
 *
 *
 * 内向的人 开始 时有 120 个幸福感，但每存在一个邻居（内向的或外向的）他都会 失去  30 个幸福感。
 * 外向的人 开始 时有 40 个幸福感，每存在一个邻居（内向的或外向的）他都会 得到  20 个幸福感。
 *
 *
 * 邻居是指居住在一个人所在单元的上、下、左、右四个直接相邻的单元中的其他人。
 *
 * 网格幸福感 是每个人幸福感的 总和 。 返回 最大可能的网格幸福感 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
 * 输出：240
 * 解释：假设网格坐标 (row, column) 从 1 开始编号。
 * 将内向的人放置在单元 (1,1) ，将外向的人放置在单元 (1,3) 和 (2,3) 。
 * - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (0 * 30)（0 位邻居）= 120
 * - 位于 (1,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
 * - 位于 (2,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
 * 网格幸福感为：120 + 60 + 60 = 240
 * 上图展示该示例对应网格中每个人的幸福感。内向的人在浅绿色单元中，而外向的人在浅紫色单元中。
 *
 *
 * 示例 2：
 *
 *
 * 输入：m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
 * 输出：260
 * 解释：将内向的人放置在单元 (1,1) 和 (3,1) ，将外向的人放置在单元 (2,1) 。
 * - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
 * - 位于 (2,1) 的外向的人的幸福感：40（初始幸福感）+ (2 * 20)（2 位邻居）= 80
 * - 位于 (3,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
 * 网格幸福感为 90 + 80 + 90 = 260
 *
 *
 * 示例 3：
 *
 *
 * 输入：m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
 * 输出：240
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 0
 *
 *
 */

// @lc code=start
func getMaxGridHappiness(m int, n int, nx int, wx int) int {
	// 初始化相临状态产生的偏差值
	calcMap := [3][3]int{{0, 0, 0}, {0, -60, -10}, {0, -10, 40}}
	// 初始化0到矩阵宽度n之间的三次方
	n3 := 1
	nn := make([]int, n+1)
	nn[0] = 1
	for i := 0; i < n; i++ {
		n3 *= 3
		nn[i+1] = n3
	}
	// ML：最后一位
	ML := n * m
	// 初始化上一位的状态集
	preMax := make([][]int, n3)
	for i := range preMax {
		preMax[i] = make([]int, (nx+1)*(wx+1))
	}
	// 初始化当前位的状态集，用于给下一位使用
	maxs := make([][]int, n3)
	for i := range maxs {
		maxs[i] = make([]int, (nx+1)*(wx+1))
	}
	// 初始化使用到的中间参数：
	// P：当前位置（从ML-1开始到0结束）；
	// N：当前位置可以使用到的内向人数；
	// W：当前位置可以使用到的外向人数；
	// nidx：当前位置的最大前置压缩状态的索引，初始为宽度n；
	// tn,tw：临时数据，用于遍历内向外向的人数做状态压缩
	for P, N, W, nidx, tn, tw := ML-1, 0, 0, n, 0, 0; P >= 0; P-- {
		// 当剩余位置小于n时，最大前置压缩状态索引则用剩余位置索引
		if P < nidx {
			nidx = P
		}
		// 当使用到的位置小于内向人数时，内向人数为使用人数
		if (ML - P) <= nx {
			N = ML - P
		}
		// 当使用到的位置小于外向人数时，外向人数为使用人数
		if (ML - P) <= wx {
			W = ML - P
		}
		// 遍历所有可能的压缩状态
		for idx := 0; idx < nn[nidx]; idx++ {
			lf, top, calcIdx := idx%3, (idx*3)/n3, (idx*3)%n3
			if P%n == 0 {
				lf = 0
			}
			// 遍历所有可能的人数情况
			for tn = N; tn >= 0; tn-- {
				for tw = W; tw >= 0; tw-- {
					max := preMax[calcIdx][tn*(wx+1)+tw]
					if tn > 0 {
						if tm := preMax[calcIdx+1][(tn-1)*(wx+1)+tw] + 120 + calcMap[1][lf] + calcMap[1][top]; tm > max {
							max = tm
						}
					}
					if tw > 0 {
						if tm := preMax[calcIdx+2][tn*(wx+1)+tw-1] + 40 + calcMap[2][lf] + calcMap[2][top]; tm > max {
							max = tm
						}
					}
					// 将最大值放置在对应压缩状态和使用人数的位置上
					maxs[idx][tn*(wx+1)+tw] = max
				}
			}
		}
		// 将当前位置的窗口压缩状态赋值到上一位，给下一位使用
		preMax, maxs = maxs, preMax
	}
	max := 0
	// 遍历所有的压缩状态，获取最大的状态值
	for _, m := range preMax[0] {
		if m > max {
			max = m
		}
	}
	return max
}

// @lc code=end

