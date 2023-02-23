/*
 * @lc app=leetcode.cn id=2572 lang=golang
 *
 * [2572] 无平方子集计数
 *
 * https://leetcode.cn/problems/count-the-number-of-square-free-subsets/description/
 *
 * algorithms
 * Medium (23.13%)
 * Likes:    12
 * Dislikes: 0
 * Total Accepted:    1.8K
 * Total Submissions: 7.6K
 * Testcase Example:  '[3,4,4,5]'
 *
 * 给你一个正整数数组 nums 。
 *
 * 如果数组 nums 的子集中的元素乘积是一个 无平方因子数 ，则认为该子集是一个 无平方 子集。
 *
 * 无平方因子数 是无法被除 1 之外任何平方数整除的数字。
 *
 * 返回数组 nums 中 无平方 且 非空 的子集数目。因为答案可能很大，返回对 10^9 + 7 取余的结果。
 *
 * nums 的 非空子集 是可以由删除 nums
 * 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [3,4,4,5]
 * 输出：3
 * 解释：示例中有 3 个无平方子集：
 * - 由第 0 个元素 [3] 组成的子集。其元素的乘积是 3 ，这是一个无平方因子数。
 * - 由第 3 个元素 [5] 组成的子集。其元素的乘积是 5 ，这是一个无平方因子数。
 * - 由第 0 个和第 3 个元素 [3,5] 组成的子集。其元素的乘积是 15 ，这是一个无平方因子数。
 * 可以证明给定数组中不存在超过 3 个无平方子集。
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1]
 * 输出：1
 * 解释：示例中有 1 个无平方子集：
 * - 由第 0 个元素 [1] 组成的子集。其元素的乘积是 1 ，这是一个无平方因子数。
 * 可以证明给定数组中不存在超过 1 个无平方子集。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 1000
 * 1 <= nums[i] <= 30
 *
 *
 */

// @lc code=start
var primes = [...]int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
var nsq2mask = [31]int{} // nsq2mask[i] 为 i 对应的质数集合（用二进制表示）

func init() {
	for i := 2; i <= 30; i++ {
		for j, p := range primes {
			if i%p == 0 {
				if i%(p*p) == 0 { // 有平方因子
					nsq2mask[i] = -1
					break
				}
				nsq2mask[i] |= 1 << j // 把 j 加到集合中
			}
		}
	}
}
func squareFreeSubsets(a []int) int {
	const mod int = 1e9 + 7
	cnt, pow2 := [31]int{}, 1
	for _, x := range a {
		if x == 1 {
			pow2 = pow2 * 2 % mod
		} else {
			cnt[x]++
		}
	}

	const m = 1 << len(primes)
	f := [m]int{1} // f[j] 表示恰好组成集合 j 的方案数，其中空集的方案数为 1
	for nsq, mask := range nsq2mask {
		if mask > 0 && cnt[nsq] > 0 {
			other := (m - 1) ^ mask // mask 的补集
			for j := other; ; {     // 枚举 other 的子集 j
				f[j|mask] = (f[j|mask] + f[j]*cnt[nsq]) % mod // 不选 mask + 选 mask
				j = (j - 1) & other
				if j == other {
					break
				}
			}
		}
	}
	ans := 0
	for _, v := range f {
		ans += v
	}
	return (ans%mod*pow2 - 1 + mod) % mod // -1 去掉空集，+mod 保证非负
}

// @lc code=end

