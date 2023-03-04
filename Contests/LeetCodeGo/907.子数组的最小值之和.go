/*
 * @lc app=leetcode.cn id=907 lang=golang
 *
 * [907] 子数组的最小值之和
 *
 * https://leetcode.cn/problems/sum-of-subarray-minimums/description/
 *
 * algorithms
 * Medium (38.31%)
 * Likes:    617
 * Dislikes: 0
 * Total Accepted:    44.7K
 * Total Submissions: 116.6K
 * Testcase Example:  '[3,1,2,4]'
 *
 * 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
 *
 * 由于答案可能很大，因此 返回答案模 10^9 + 7 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：arr = [3,1,2,4]
 * 输出：17
 * 解释：
 * 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
 * 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
 *
 * 示例 2：
 *
 *
 * 输入：arr = [11,81,94,43,3]
 * 输出：444
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 1
 *
 *
 *
 *
 */

// @lc code=start
func sumSubarrayMins(arr []int) int {
	arr = append(arr, -1)
	stk := []int{-1}
	ans := 0
	for r, x := range arr {
		for len(stk) > 1 && arr[stk[len(stk)-1]] >= x {
			ans += arr[stk[len(stk)-1]] * (r - stk[len(stk)-1]) * (stk[len(stk)-1] - stk[len(stk)-2])
			stk = stk[:len(stk)-1]
		}
		stk = append(stk, r)
	}
	return ans % (1e9 + 7)
}

// @lc code=end

