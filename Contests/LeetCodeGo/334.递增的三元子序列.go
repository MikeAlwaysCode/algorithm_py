/*
 * @lc app=leetcode.cn id=334 lang=golang
 *
 * [334] 递增的三元子序列
 *
 * https://leetcode.cn/problems/increasing-triplet-subsequence/description/
 *
 * algorithms
 * Medium (43.40%)
 * Likes:    665
 * Dislikes: 0
 * Total Accepted:    115.9K
 * Total Submissions: 267.1K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
 *
 * 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回
 * true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3,4,5]
 * 输出：true
 * 解释：任何 i < j < k 的三元组都满足题意
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [5,4,3,2,1]
 * 输出：false
 * 解释：不存在满足题意的三元组
 *
 * 示例 3：
 *
 *
 * 输入：nums = [2,1,5,0,4,6]
 * 输出：true
 * 解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 5 * 10^5
 * -2^31 <= nums[i] <= 2^31 - 1
 *
 *
 *
 *
 * 进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？
 *
 */

// @lc code=start
func increasingTriplet(nums []int) bool {
	dp := []int{}
	for _, num := range nums {
		if len(dp) == 0 || dp[len(dp)-1] < num {
			dp = append(dp, num)
			if len(dp) >= 3 {
				return true
			}
		} else {
			l, r := 0, len(dp)-1
			for l < r {
				mid := (l + r) >> 1
				if dp[mid] >= num {
					r = mid
				} else {
					l = mid + 1
				}
			}
			dp[r] = num
		}
	}
	return false
}

// @lc code=end

