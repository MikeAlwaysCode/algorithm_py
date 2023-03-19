/*
 * @lc app=leetcode.cn id=2576 lang=golang
 *
 * [2576] 求出最多标记下标
 *
 * https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/description/
 *
 * algorithms
 * Medium (36.46%)
 * Likes:    29
 * Dislikes: 0
 * Total Accepted:    5.8K
 * Total Submissions: 15.9K
 * Testcase Example:  '[3,5,2,4]'
 *
 * 给你一个下标从 0 开始的整数数组 nums 。
 *
 * 一开始，所有下标都没有被标记。你可以执行以下操作任意次：
 *
 *
 * 选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
 *
 *
 * 请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [3,5,2,4]
 * 输出：2
 * 解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
 * 没有其他更多可执行的操作，所以答案为 2 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [9,2,5,4]
 * 输出：4
 * 解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
 * 第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
 * 没有其他更多可执行的操作，所以答案为 4 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [7,6,8]
 * 输出：0
 * 解释：没有任何可以执行的操作，所以答案为 0 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 *
 *
 */

// @lc code=start
func maxNumOfMarkedIndices(nums []int) int {
	sort.Ints(nums)
	i := 0
	for _, x := range nums[(len(nums)+1)/2:] {
		if nums[i]*2 <= x {
			i++
		}
	}
	return i * 2
}

// @lc code=end

