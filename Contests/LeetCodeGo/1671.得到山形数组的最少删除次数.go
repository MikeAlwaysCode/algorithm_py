/*
 * @lc app=leetcode.cn id=1671 lang=golang
 *
 * [1671] 得到山形数组的最少删除次数
 *
 * https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/description/
 *
 * algorithms
 * Hard (47.19%)
 * Likes:    31
 * Dislikes: 0
 * Total Accepted:    3.5K
 * Total Submissions: 7.3K
 * Testcase Example:  '[1,3,1]'
 *
 * 我们定义 arr 是 山形数组 当且仅当它满足：
 *
 *
 * arr.length >= 3
 * 存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
 *
 * arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
 * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
 *
 *
 *
 *
 * 给你整数数组 nums​ ，请你返回将 nums 变成 山形状数组 的​ 最少 删除次数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,3,1]
 * 输出：0
 * 解释：数组本身就是山形数组，所以我们不需要删除任何元素。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [2,1,1,5,6,2,3,1]
 * 输出：3
 * 解释：一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= nums.length <= 1000
 * 1 <= nums[i] <= 10^9
 * 题目保证 nums 删除一些元素后一定能得到山形数组。
 *
 *
 */

// @lc code=start
func minimumMountainRemovals(nums []int) int {
	pres := preLis(nums, false)
	suff := preLis(nums, true)
	n := len(nums)
	ans := n
	for i := 1; i < n-1; i++ {
		if pres[i] > 1 && suff[i] > 1 {
			ans = min(ans, n+1-pres[i]-suff[i])
		}
	}
	return ans
}
func preLis(nums []int, reverse bool) []int {
	n := len(nums)
	plis := make([]int, n)
	d := []int{}
	var s, e, p int
	if reverse {
		s, e, p = n-1, -1, -1
	} else {
		s, e, p = 0, n, 1
	}
	for i := s; i != e; i += p {
		if len(d) == 0 || nums[i] > d[len(d)-1] {
			d = append(d, nums[i])
			plis[i] = len(d)
		} else {
			l, r := 0, len(d)-1
			for l < r {
				mid := l + (r-l)/2
				if d[mid] >= nums[i] {
					r = mid
				} else {
					l = mid + 1
				}
			}
			d[r] = nums[i]
			plis[i] = r + 1
		}
	}
	return plis
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end

