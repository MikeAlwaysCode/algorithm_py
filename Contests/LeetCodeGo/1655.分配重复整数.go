/*
 * @lc app=leetcode.cn id=1655 lang=golang
 *
 * [1655] 分配重复整数
 *
 * https://leetcode.cn/problems/distribute-repeating-integers/description/
 *
 * algorithms
 * Hard (39.57%)
 * Likes:    48
 * Dislikes: 0
 * Total Accepted:    3.8K
 * Total Submissions: 9.5K
 * Testcase Example:  '[1,2,3,4]\n[2]'
 *
 * 给你一个长度为 n 的整数数组 nums ，这个数组中至多有 50 个不同的值。同时你有 m 个顾客的订单 quantity ，其中，整数
 * quantity[i] 是第 i 位顾客订单的数目。请你判断是否能将 nums 中的整数分配给这些顾客，且满足：
 *
 *
 * 第 i 位顾客 恰好 有 quantity[i] 个整数。
 * 第 i 位顾客拿到的整数都是 相同的 。
 * 每位顾客都满足上述两个要求。
 *
 *
 * 如果你可以分配 nums 中的整数满足上面的要求，那么请返回 true ，否则返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3,4], quantity = [2]
 * 输出：false
 * 解释：第 0 位顾客没办法得到两个相同的整数。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3,3], quantity = [2]
 * 输出：true
 * 解释：第 0 位顾客得到 [3,3] 。整数 [1,2] 都没有被使用。
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,1,2,2], quantity = [2,2]
 * 输出：true
 * 解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [2,2] 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == nums.length
 * 1 <= n <= 10^5
 * 1 <= nums[i] <= 1000
 * m == quantity.length
 * 1 <= m <= 10
 * 1 <= quantity[i] <= 10^5
 * nums 中至多有 50 个不同的数字。
 *
 *
 */

// @lc code=start
func canDistribute(nums []int, quantity []int) bool {
	n := len(quantity)
	need := make([]int, 1<<n)
	for mask := 1; mask < (1 << n); mask++ {
		for j, v := range quantity {
			if (mask>>j)&1 > 0 {
				need[mask] += v
			}
		}
	}
	cnt := map[int]int{}
	for _, v := range nums {
		cnt[v]++
	}
	dp := make([][]bool, len(cnt)+1)
	for i := range dp {
		dp[i] = make([]bool, 1<<n)
	}
	dp[0][0] = true
	i := 0
	for _, v := range cnt {
		for mask := range dp[i] {
			if dp[i][mask] {
				dp[i+1][mask] = true
				continue
			}
			for sub := mask; sub > 0; sub = (sub - 1) & mask {
				if need[sub] <= v && dp[i][mask^sub] {
					dp[i+1][mask] = true
					break
				}
			}
		}
		if dp[i+1][(1<<n)-1] {
			return true
		}
		i++
	}
	return false
}

// @lc code=end

