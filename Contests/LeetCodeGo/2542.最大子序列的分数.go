/*
 * @lc app=leetcode.cn id=2542 lang=golang
 *
 * [2542] 最大子序列的分数
 *
 * https://leetcode.cn/problems/maximum-subsequence-score/description/
 *
 * algorithms
 * Medium (48.19%)
 * Likes:    23
 * Dislikes: 0
 * Total Accepted:    1.9K
 * Total Submissions: 3.9K
 * Testcase Example:  '[1,3,3,2]\n[2,1,3,4]\n3'
 *
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都是 n ，再给你一个正整数 k 。你必须从 nums1 中选一个长度为 k
 * 的 子序列 对应的下标。
 *
 * 对于选择的下标 i0 ，i1 ，...， ik - 1 ，你的 分数 定义如下：
 *
 *
 * nums1 中下标对应元素求和，乘以 nums2 中下标对应元素的 最小值 。
 * 用公示表示： (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] ,
 * nums2[i1], ... ,nums2[ik - 1]) 。
 *
 *
 * 请你返回 最大 可能的分数。
 *
 * 一个数组的 子序列 下标是集合 {0, 1, ..., n-1} 中删除若干元素得到的剩余集合，也可以不删除任何元素。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
 * 输出：12
 * 解释：
 * 四个可能的子序列分数为：
 * - 选择下标 0 ，1 和 2 ，得到分数 (1+3+3) * min(2,1,3) = 7 。
 * - 选择下标 0 ，1 和 3 ，得到分数 (1+3+2) * min(2,1,4) = 6 。
 * - 选择下标 0 ，2 和 3 ，得到分数 (1+3+2) * min(2,3,4) = 12 。
 * - 选择下标 1 ，2 和 3 ，得到分数 (3+3+2) * min(1,3,4) = 8 。
 * 所以最大分数为 12 。
 *
 *
 * 示例 2：
 *
 * 输入：nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
 * 输出：30
 * 解释：
 * 选择下标 2 最优：nums1[2] * nums2[2] = 3 * 10 = 30 是最大可能分数。
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == nums1.length == nums2.length
 * 1 <= n <= 10^5
 * 0 <= nums1[i], nums2[j] <= 10^5
 * 1 <= k <= n
 *
 *
 */

// @lc code=start
func maxScore(nums1 []int, nums2 []int, k int) int64 {
	n := len(nums1)
	type pair struct{ s, e int }
	a := make([]pair, n)
	for i := 0; i < n; i++ {
		a[i] = pair{nums1[i], nums2[i]}
	}
	sort.Slice(a, func(i, j int) bool {
		if a[i].e == a[j].e {
			return a[i].s >= a[j].s
		} else {
			return a[i].e > a[j].e
		}
	})
	var ans, s int64
	h := &hp{}
	for i := 0; i < n; i++ {
		if h.Len() < k {
			s += int64(a[i].s)
			heap.Push(h, a[i].s)
		} else {
			// p := heap.pushPop(h, a[i].s)
			p := h.pushPop(a[i].s)
			s += int64(a[i].s - p)
		}
		if h.Len() == k {
			ans = max(ans, s*int64(a[i].e))
		}
	}
	return ans
}

type hp struct{ sort.IntSlice }

//func (h hp) Less(i, j int) bool  { return h.IntSlice[i] > h.IntSlice[j] } //加上是最大堆
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}
func (h *hp) pushPop(v int) int {
	if len(h.IntSlice) > 0 && v > h.IntSlice[0] { // 最大堆改成 v < h.IntSlice[0]
		v, h.IntSlice[0] = h.IntSlice[0], v
		heap.Fix(h, 0)
	}
	return v
}
func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

