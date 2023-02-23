/*
 * @lc app=leetcode.cn id=689 lang=golang
 *
 * [689] 三个无重叠子数组的最大和
 *
 * https://leetcode.cn/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
 *
 * algorithms
 * Hard (56.30%)
 * Likes:    334
 * Dislikes: 0
 * Total Accepted:    22.3K
 * Total Submissions: 39.6K
 * Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
 *
 * 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且全部数字和（3 * k 项）最大的子数组，并返回这三个子数组。
 *
 * 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,1,2,6,7,5,1], k = 2
 * 输出：[0,3,5]
 * 解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
 * 也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
 * 输出：[0,2,4]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * 1 <= nums[i] < 2^16
 * 1 <= k <= floor(nums.length / 3)
 *
 *
 */
// @lc code=start
func maxSumOfThreeSubarrays(nums []int, k int) []int {
	n := len(nums)
	pres := make([]int, n+1)
	for i := 0; i < n; i++ {
		pres[i+1] = pres[i] + nums[i]
	}
	dp := make([][]int, 4)
	dp[0] = make([]int, n+3)
	for j := 1; j < 4; j++ {
		dp[j] = make([]int, n+3)
		for i := n - j*k + 1; i > 0; i-- {
			dp[j][i] = max(dp[j][i+1], dp[j-1][i+k]+pres[i+k-1]-pres[i-1])
		}
	}
	ans := []int{0, 0, 0}
	i, idx := 1, 0
	for j := 3; j > 0; j-- {
		for ; dp[j][i+1] > dp[j-1][i+k]+pres[i+k-1]-pres[i-1]; i++ {
		}
		ans[idx] = i - 1
		idx++
		i += k
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
