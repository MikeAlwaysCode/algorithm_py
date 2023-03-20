/*
 * @lc app=leetcode.cn id=307 lang=golang
 *
 * [307] 区域和检索 - 数组可修改
 *
 * https://leetcode.cn/problems/range-sum-query-mutable/description/
 *
 * algorithms
 * Medium (51.94%)
 * Likes:    588
 * Dislikes: 0
 * Total Accepted:    64.4K
 * Total Submissions: 124K
 * Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
 *
 * 给你一个数组 nums ，请你完成两类查询。
 *
 *
 * 其中一类查询要求 更新 数组 nums 下标对应的值
 * 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
 *
 *
 * 实现 NumArray 类：
 *
 *
 * NumArray(int[] nums) 用整数数组 nums 初始化对象
 * void update(int index, int val) 将 nums[index] 的值 更新 为 val
 * int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含
 * ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：
 * ["NumArray", "sumRange", "update", "sumRange"]
 * [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
 * 输出：
 * [null, 9, null, 8]
 *
 * 解释：
 * NumArray numArray = new NumArray([1, 3, 5]);
 * numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
 * numArray.update(1, 2);   // nums = [1,2,5]
 * numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 3 * 10^4
 * -100 <= nums[i] <= 100
 * 0 <= index < nums.length
 * -100 <= val <= 100
 * 0 <= left <= right < nums.length
 * 调用 update 和 sumRange 方法次数不大于 3 * 10^4
 *
 *
 */

// @lc code=start
type NumArray []int

func Constructor(nums []int) NumArray {
	n := len(nums)
	seg := make(NumArray, n*4)
	seg.build(nums, 0, 0, n-1)
	return seg
}

func (seg NumArray) build(nums []int, node, s, e int) {
	if s == e {
		seg[node] = nums[s]
		return
	}
	m := s + (e-s)/2
	seg.build(nums, node*2+1, s, m)
	seg.build(nums, node*2+2, m+1, e)
	seg[node] = seg[node*2+1] + seg[node*2+2]
}

func (seg NumArray) change(index, val, node, s, e int) {
	if s == e {
		seg[node] = val
		return
	}
	m := s + (e-s)/2
	if index <= m {
		seg.change(index, val, node*2+1, s, m)
	} else {
		seg.change(index, val, node*2+2, m+1, e)
	}
	seg[node] = seg[node*2+1] + seg[node*2+2]
}

func (seg NumArray) range_(left, right, node, s, e int) int {
	if left == s && right == e {
		return seg[node]
	}
	m := s + (e-s)/2
	if right <= m {
		return seg.range_(left, right, node*2+1, s, m)
	}
	if left > m {
		return seg.range_(left, right, node*2+2, m+1, e)
	}
	return seg.range_(left, m, node*2+1, s, m) + seg.range_(m+1, right, node*2+2, m+1, e)
}

func (seg NumArray) Update(index, val int) {
	seg.change(index, val, 0, 0, len(seg)/4-1)
}

func (seg NumArray) SumRange(left, right int) int {
	return seg.range_(left, right, 0, 0, len(seg)/4-1)
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */
// @lc code=end

