/*
 * @lc app=leetcode.cn id=6340 lang=golang
 *
 * [6340] 统计上升四元组
 *
 * https://leetcode.cn/problems/count-increasing-quadruplets/description/
 *
 * algorithms
 * Hard (33.59%)
 * Likes:    2
 * Dislikes: 0
 * Total Accepted:    799
 * Total Submissions: 2.4K
 * Testcase Example:  '[1,3,2,4,5]'
 *
 * 给你一个长度为 n 下标从 0 开始的整数数组 nums ，它包含 1 到 n 的所有数字，请你返回上升四元组的数目。
 *
 * 如果一个四元组 (i, j, k, l) 满足以下条件，我们称它是上升的：
 *
 *
 * 0 <= i < j < k < l < n 且
 * nums[i] < nums[k] < nums[j] < nums[l] 。
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [1,3,2,4,5]
 * 输出：2
 * 解释：
 * - 当 i = 0 ，j = 1 ，k = 2 且 l = 3 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。
 * - 当 i = 0 ，j = 1 ，k = 2 且 l = 4 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。
 * 没有其他的四元组，所以我们返回 2 。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [1,2,3,4]
 * 输出：0
 * 解释：只存在一个四元组 i = 0 ，j = 1 ，k = 2 ，l = 3 ，但是 nums[j] < nums[k] ，所以我们返回 0
 * 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 4 <= nums.length <= 4000
 * 1 <= nums[i] <= nums.length
 * nums 中所有数字 互不相同 ，nums 是一个排列。
 *
 *
 */

// @lc code=start
func countQuadruplets(nums []int) (ans int64) {
	// i < j < k < l
	// nums[i] < nums[k] < nums[j] < nums[l]
	n := len(nums)
	cnt := make([]int64, n) // 132个数
	var large int64
	for i := 0; i < n; i++ {
		large = 0
		for j := 0; j < i; j++ {
			if nums[i] > nums[j] {
				// i < j < k且nums[i] < nums[k] < nums[j] 的个数
				ans += cnt[j]
				// 前面小于nums[i]的个数
				large++
			} else {
				// i < j < k且nums[i] < nums[k] < nums[j] 的个数
				cnt[j] += large
			}
		}
	}
	return
}

// @lc code=end

