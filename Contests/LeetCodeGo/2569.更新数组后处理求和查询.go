/*
 * @lc app=leetcode.cn id=2569 lang=golang
 *
 * [2569] 更新数组后处理求和查询
 *
 * https://leetcode.cn/problems/handling-sum-queries-after-update/description/
 *
 * algorithms
 * Hard (30.19%)
 * Likes:    6
 * Dislikes: 0
 * Total Accepted:    1.2K
 * Total Submissions: 3.9K
 * Testcase Example:  '[1,0,1]\n[0,0,0]\n[[1,1,1],[2,1,0],[3,0,0]]'
 *
 * 给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：
 *
 *
 * 操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 或将 1 反转成
 * 0 。l 和 r 下标都从 0 开始。
 * 操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i]
 * + nums1[i] * p 。
 * 操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
 *
 *
 * 请你返回一个数组，包含所有第三种操作类型的答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
 * 输出：[3]
 * 解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3]
 * 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
 * 输出：[5]
 * 解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums1.length,nums2.length <= 10^5
 * nums1.length = nums2.length
 * 1 <= queries.length <= 10^5
 * queries[i].length = 3
 * 0 <= l <= r <= nums1.length - 1
 * 0 <= p <= 10^6
 * 0 <= nums1[i] <= 1
 * 0 <= nums2[i] <= 10^9
 *
 *
 */

// @lc code=start
func handleQuery(nums1 []int, nums2 []int, queries [][]int) []int64 {

}

// @lc code=end

