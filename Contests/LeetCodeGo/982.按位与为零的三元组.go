/*
 * @lc app=leetcode.cn id=982 lang=golang
 *
 * [982] 按位与为零的三元组
 *
 * https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/description/
 *
 * algorithms
 * Hard (57.66%)
 * Likes:    81
 * Dislikes: 0
 * Total Accepted:    8.4K
 * Total Submissions: 13.1K
 * Testcase Example:  '[2,1,3]'
 *
 * 给你一个整数数组 nums ，返回其中 按位与三元组 的数目。
 *
 * 按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：
 *
 *
 * 0 <= i < nums.length
 * 0 <= j < nums.length
 * 0 <= k < nums.length
 * nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [2,1,3]
 * 输出：12
 * 解释：可以选出如下 i, j, k 三元组：
 * (i=0, j=0, k=1) : 2 & 2 & 1
 * (i=0, j=1, k=0) : 2 & 1 & 2
 * (i=0, j=1, k=1) : 2 & 1 & 1
 * (i=0, j=1, k=2) : 2 & 1 & 3
 * (i=0, j=2, k=1) : 2 & 3 & 1
 * (i=1, j=0, k=0) : 1 & 2 & 2
 * (i=1, j=0, k=1) : 1 & 2 & 1
 * (i=1, j=0, k=2) : 1 & 2 & 3
 * (i=1, j=1, k=0) : 1 & 1 & 2
 * (i=1, j=2, k=0) : 1 & 3 & 2
 * (i=2, j=0, k=1) : 3 & 2 & 1
 * (i=2, j=1, k=0) : 3 & 1 & 2
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,0,0]
 * 输出：27
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 1000
 * 0 <= nums[i] < 2^16
 *
 *
 */

// @lc code=start
func countTriplets(nums []int) (ans int) {
	u := 1
	for _, x := range nums {
		for u <= x {
			u <<= 1
		}
	}
	cnt := make([]int, u)
	cnt[0] = len(nums) // 直接统计空集
	for _, m := range nums {
		m ^= u - 1
		for s := m; s > 0; s = (s - 1) & m { // 枚举 m 的非空子集
			cnt[s]++
		}
	}
	for _, x := range nums {
		for _, y := range nums {
			ans += cnt[x&y]
		}
	}
	return
}

// @lc code=end

