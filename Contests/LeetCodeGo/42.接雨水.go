/*
 * @lc app=leetcode.cn id=42 lang=golang
 *
 * [42] 接雨水
 *
 * https://leetcode.cn/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (62.39%)
 * Likes:    4136
 * Dislikes: 0
 * Total Accepted:    639.5K
 * Total Submissions: 1M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * 输出：6
 * 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
 *
 *
 * 示例 2：
 *
 *
 * 输入：height = [4,2,0,3,2,5]
 * 输出：9
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
 *
 *
 */

// @lc code=start
func trap(height []int) int {
	n := len(height)

	var ans, i, j, pres, suff int
	j = n - 1
	for i <= j {
		pres = max(pres, height[i])
		suff = max(suff, height[j])
		if pres <= suff {
			ans += pres - height[i]
			i++
		} else {
			ans += suff - height[j]
			j--
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

