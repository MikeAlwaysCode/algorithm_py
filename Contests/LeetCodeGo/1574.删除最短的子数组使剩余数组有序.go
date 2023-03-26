/*
 * @lc app=leetcode.cn id=1574 lang=golang
 *
 * [1574] 删除最短的子数组使剩余数组有序
 *
 * https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/
 *
 * algorithms
 * Medium (36.68%)
 * Likes:    101
 * Dislikes: 0
 * Total Accepted:    9.6K
 * Total Submissions: 26.2K
 * Testcase Example:  '[1,2,3,10,4,2,3,5]'
 *
 * 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
 *
 * 一个子数组指的是原数组中连续的一个子序列。
 *
 * 请你返回满足题目要求的最短子数组的长度。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：arr = [1,2,3,10,4,2,3,5]
 * 输出：3
 * 解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
 * 另一个正确的解为删除子数组 [3,10,4] 。
 *
 * 示例 2：
 *
 *
 * 输入：arr = [5,4,3,2,1]
 * 输出：4
 * 解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
 *
 *
 * 示例 3：
 *
 *
 * 输入：arr = [1,2,3]
 * 输出：0
 * 解释：数组已经是非递减的了，我们不需要删除任何元素。
 *
 *
 * 示例 4：
 *
 *
 * 输入：arr = [1]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr.length <= 10^5
 * 0 <= arr[i] <= 10^9
 *
 *
 */

// @lc code=start
func findLengthOfShortestSubarray(arr []int) int {
	n := len(arr)
	right := n - 1
	for right > 0 && arr[right-1] <= arr[right] {
		right--
	}
	if right == 0 { // arr 已经是非递减数组
		return 0
	}
	// 此时 arr[right-1] > arr[right]
	ans := right // 删除 arr[:right]
	for left := 0; left == 0 || arr[left-1] <= arr[left]; left++ {
		for right < n && arr[right] < arr[left] {
			right++
		}
		ans = min(ans, right-left-1) // 删除 arr[left+1:right]
	}
	return ans
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

// @lc code=end

