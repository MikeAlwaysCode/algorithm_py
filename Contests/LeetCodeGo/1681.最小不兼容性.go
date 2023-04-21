/*
 * @lc app=leetcode.cn id=1681 lang=golang
 *
 * [1681] 最小不兼容性
 *
 * https://leetcode.cn/problems/minimum-incompatibility/description/
 *
 * algorithms
 * Hard (42.76%)
 * Likes:    56
 * Dislikes: 0
 * Total Accepted:    3.9K
 * Total Submissions: 9K
 * Testcase Example:  '[1,2,1,4]\n2'
 *
 * 给你一个整数数组 nums​​​ 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。
 *
 * 一个子集的 不兼容性 是该子集里面最大值和最小值的差。
 *
 * 请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。
 *
 * 子集的定义是数组中一些数字的集合，对数字顺序没有要求。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,1,4], k = 2
 * 输出：4
 * 解释：最优的分配是 [1,2] 和 [1,4] 。
 * 不兼容性和为 (2-1) + (4-1) = 4 。
 * 注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。
 *
 * 示例 2：
 *
 *
 * 输入：nums = [6,3,8,1,3,1,2,2], k = 4
 * 输出：6
 * 解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
 * 不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [5,3,3,6,3,3], k = 3
 * 输出：-1
 * 解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * nums.length 能被 k 整除。
 * 1
 *
 *
 */

// @lc code=start
func minimumIncompatibility(nums []int, k int) int {
	n := len(nums)
	if k == n {
		return 0
	}
	cnt := make([]int, n+1)
	for _, num := range nums {
		cnt[num]++
		if cnt[num] > k { // 存在某个数的数量超过k个，直接返回-1
			return -1
		}
	}
	m, div := 1<<uint(n), n/k
	f, sum := make([]int, m), make([]int, m)
	for i := range sum { // 预处理可以划分为同一个子集的所有情况
		sum[i] = 1000
		if bits.OnesCount(uint(i)) == div {
			curSum, curMax, curMin := 0, 0, n
			for j := i; j > 0; j ^= j & -j { // 参考树状数组的get  从低到高遍历i的每一个1
				jj := bits.TrailingZeros(uint(j))
				curSum |= 1 << uint(nums[jj])
				curMax, curMin = max(curMax, nums[jj]), min(curMin, nums[jj])
			}
			if bits.OnesCount(uint(curSum)) == div {
				sum[i] = curMax - curMin
			}
		}
	}
	for mask := 1; mask < m; mask++ {
		if bits.OnesCount(uint(mask))%div == 0 { // 只有mask中的1的数量可以被div整除，mask才可以进行有效的状态转移
			f[mask] = 1000
			for sub := mask; sub > 0; sub = (sub - 1) & mask {
				f[mask] = min(f[mask], f[mask^sub]+sum[sub])
			}
		}
	}
	if f[m-1] == 1000 {
		return -1
	}
	return f[m-1]
}

func min(a int, b int) int {
	if a <= b {
		return a
	}
	return b
}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}

// @lc code=end

