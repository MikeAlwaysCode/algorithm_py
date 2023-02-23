/*
 * @lc app=leetcode.cn id=1326 lang=golang
 *
 * [1326] 灌溉花园的最少水龙头数目
 *
 * https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/
 *
 * algorithms
 * Hard (48.39%)
 * Likes:    144
 * Dislikes: 0
 * Total Accepted:    9.9K
 * Total Submissions: 19.6K
 * Testcase Example:  '5\n[3,4,1,1,0,0]'
 *
 * 在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。
 *
 * 花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。
 *
 * 给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：如果打开点 i
 * 处的水龙头，可以灌溉的区域为 [i -  ranges[i], i + ranges[i]] 。
 *
 * 请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：n = 5, ranges = [3,4,1,1,0,0]
 * 输出：1
 * 解释：
 * 点 0 处的水龙头可以灌溉区间 [-3,3]
 * 点 1 处的水龙头可以灌溉区间 [-3,5]
 * 点 2 处的水龙头可以灌溉区间 [1,3]
 * 点 3 处的水龙头可以灌溉区间 [2,4]
 * 点 4 处的水龙头可以灌溉区间 [4,4]
 * 点 5 处的水龙头可以灌溉区间 [5,5]
 * 只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 3, ranges = [0,0,0,0]
 * 输出：-1
 * 解释：即使打开所有水龙头，你也无法灌溉整个花园。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 10^4
 * ranges.length == n + 1
 * 0 <= ranges[i] <= 100
 *
 *
 */
package LeetCodeGo

// @lc code=start
func minTaps(n int, ranges []int) (ans int) {
	rightMost := make([]int, n+1)
	for i, r := range ranges {
		left := max(i-r, 0)
		rightMost[left] = max(rightMost[left], i+r)
	}

	curRight := 0                     // 已建造的桥的右端点
	nextRight := 0                    // 下一座桥的右端点的最大值
	for i, r := range rightMost[:n] { // 注意这里没有遍历到 n，因为它已经是终点了
		nextRight = max(nextRight, r)
		if i == curRight { // 到达已建造的桥的右端点
			if i == nextRight { // 无论怎么造桥，都无法从 i 到 i+1
				return -1
			}
			curRight = nextRight // 造一座桥
			ans++
		}
	}
	return
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

// @lc code=end
