/*
 * @lc app=leetcode.cn id=2444 lang=golang
 *
 * [2444] 统计定界子数组的数目
 *
 * https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/description/
 *
 * algorithms
 * Hard (43.20%)
 * Likes:    68
 * Dislikes: 0
 * Total Accepted:    6.3K
 * Total Submissions: 14.4K
 * Testcase Example:  '[1,3,5,2,7,5]\n1\n5'
 *
 * 给你一个整数数组 nums 和两个整数 minK 以及 maxK 。
 *
 * nums 的定界子数组是满足下述条件的一个子数组：
 *
 *
 * 子数组中的 最小值 等于 minK 。
 * 子数组中的 最大值 等于 maxK 。
 *
 *
 * 返回定界子数组的数目。
 *
 * 子数组是数组中的一个连续部分。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [1,3,5,2,7,5], minK = 1, maxK = 5
 * 输出：2
 * 解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [1,1,1,1], minK = 1, maxK = 1
 * 输出：10
 * 解释：nums 的每个子数组都是一个定界子数组。共有 10 个子数组。
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= nums.length <= 10^5
 * 1 <= nums[i], minK, maxK <= 10^6
 *
 *
 */

// @lc code=start
func countSubarrays(nums []int, minK int, maxK int) (ans int64) {
	mnPos, mxPos, left := -1, -1, 0
	for i, x := range nums {
		if x == minK {
			mnPos = i
		}
		if x == maxK {
			mxPos = i
		}
		if x < minK || x > maxK {
			left = i + 1
		}
		m := min(mnPos, mxPos)
		if left <= m {
			ans += int64(m - left + 1)
		}
	}
	return
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end

