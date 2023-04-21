/*
 * @lc app=leetcode.cn id=1187 lang=golang
 *
 * [1187] 使数组严格递增
 *
 * https://leetcode.cn/problems/make-array-strictly-increasing/description/
 *
 * algorithms
 * Hard (47.99%)
 * Likes:    129
 * Dislikes: 0
 * Total Accepted:    5.2K
 * Total Submissions: 9.3K
 * Testcase Example:  '[1,5,3,6,7]\n[1,3,2,4]'
 *
 * 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
 *
 * 每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j
 * < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
 *
 * 如果无法让 arr1 严格递增，请返回 -1。
 *
 *
 *
 * 示例 1：
 *
 * 输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
 * 输出：1
 * 解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
 *
 *
 * 示例 2：
 *
 * 输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
 * 输出：2
 * 解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
 *
 *
 * 示例 3：
 *
 * 输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
 * 输出：-1
 * 解释：无法使 arr1 严格递增。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr1.length, arr2.length <= 2000
 * 0 <= arr1[i], arr2[i] <= 10^9
 *
 *
 *
 *
 */

// @lc code=start
func makeArrayIncreasing(a, b []int) int {
	a = append(a, math.MaxInt) // 简化代码逻辑
	sort.Ints(b)
	m := 0
	for _, x := range b[1:] {
		if b[m] != x {
			m++
			b[m] = x // 原地去重
		}
	}
	b = b[:m+1]

	n := len(a)
	f := make([]int, n)
	for i, x := range a {
		k := sort.SearchInts(b, x)
		res := 0 // 小于 a[i] 的数全部替换
		if k < i {
			res = math.MinInt
		}
		if i > 0 && a[i-1] < x { // 无替换
			res = max(res, f[i-1])
		}
		for j := i - 2; j >= i-k-1 && j >= 0; j-- {
			if b[k-(i-j-1)] > a[j] {
				// a[j+1] 到 a[i-1] 替换成 b[k-(i-j-1)] 到 b[k-1]
				res = max(res, f[j])
			}
		}
		f[i] = res + 1 // 把 +1 移到这里，表示 a[i] 不替换
	}
	if f[n-1] < 0 { // 注意 a 已经添加了一个元素
		return -1
	}
	return n - f[n-1]
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

// @lc code=end

