/*
 * @lc app=leetcode.cn id=1172 lang=golang
 *
 * [1172] 餐盘栈
 *
 * https://leetcode.cn/problems/dinner-plate-stacks/description/
 *
 * algorithms
 * Hard (28.28%)
 * Likes:    61
 * Dislikes: 0
 * Total Accepted:    5.3K
 * Total Submissions: 16K
 * Testcase Example:  '["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]\n' +
  '[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]'
 *
 * 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。
 *
 * 实现一个叫「餐盘」的类 DinnerPlates：
 *
 *
 * DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
 * void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
 * int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
 * int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回
 * -1。
 *
 *
 *
 *
 * 示例：
 *
 * 输入：
 *
 * ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
 * [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
 * 输出：
 * [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
 *
 * 解释：
 * DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
 * D.push(1);
 * D.push(2);
 * D.push(3);
 * D.push(4);
 * D.push(5);         // 栈的现状为：    2  4
 * 1  3  5
 * ⁠                                   ﹈ ﹈ ﹈
 * D.popAtStack(0);   // 返回 2。栈的现状为：      4
 * ⁠                                         1  3  5
 * ⁠                                         ﹈ ﹈ ﹈
 * D.push(20);        // 栈的现状为：  20  4
 * 1  3  5
 * ⁠                                  ﹈ ﹈ ﹈
 * D.push(21);        // 栈的现状为：  20  4 21
 * 1  3  5
 * ⁠                                  ﹈ ﹈ ﹈
 * D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
 * ⁠                                           1  3  5
 * ⁠                                           ﹈ ﹈ ﹈
 * D.popAtStack(2);   // 返回 21。栈的现状为：       4
 * ⁠                                           1  3  5
 * ⁠                                           ﹈ ﹈ ﹈
 * D.pop()            // 返回 5。栈的现状为：        4
 * ⁠                                           1  3
 * ⁠                                           ﹈ ﹈
 * D.pop()            // 返回 4。栈的现状为：    1  3
 * ⁠                                          ﹈ ﹈
 * D.pop()            // 返回 3。栈的现状为：    1
 * ⁠                                          ﹈
 * D.pop()            // 返回 1。现在没有栈。
 * D.pop()            // 返回 -1。仍然没有栈。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= capacity <= 20000
 * 1 <= val <= 20000
 * 0 <= index <= 100000
 * 最多会对 push，pop，和 popAtStack 进行 200000 次调用。
 *
 *
*/

// @lc code=start
type DinnerPlates struct {
	capacity int     // 栈的容量
	stacks   [][]int // 所有栈
	idx      hp      // 最小堆，保存未满栈的下标
}

func Constructor(capacity int) DinnerPlates {
	return DinnerPlates{capacity: capacity}
}

func (d *DinnerPlates) Push(val int) {
	if d.idx.Len() > 0 && d.idx.IntSlice[0] >= len(d.stacks) {
		d.idx = hp{} // 堆中都是越界下标，直接清空
	}
	if d.idx.Len() == 0 { // 所有栈都是满的
		d.stacks = append(d.stacks, []int{val}) // 添加一个新的栈
		if d.capacity > 1 {                     // 新的栈没有满
			heap.Push(&d.idx, len(d.stacks)-1) // 入堆
		}
	} else { // 还有未满栈
		i := d.idx.IntSlice[0]
		d.stacks[i] = append(d.stacks[i], val) // 入栈
		if len(d.stacks[i]) == d.capacity {    // 栈满了
			heap.Pop(&d.idx) // 从堆中去掉
		}
	}
}

func (d *DinnerPlates) Pop() int {
	// 等价为 popAtStack 最后一个非空栈
	return d.PopAtStack(len(d.stacks) - 1)
}

func (d *DinnerPlates) PopAtStack(index int) int {
	if index < 0 || index >= len(d.stacks) || len(d.stacks[index]) == 0 {
		return -1 // 非法操作
	}
	if len(d.stacks[index]) == d.capacity { // 满栈
		heap.Push(&d.idx, index) // 元素出栈后，栈就不满了，把下标入堆
	}
	bk := len(d.stacks[index]) - 1
	val := d.stacks[index][bk]
	d.stacks[index] = d.stacks[index][:bk]
	for len(d.stacks) > 0 && len(d.stacks[len(d.stacks)-1]) == 0 {
		d.stacks = d.stacks[:len(d.stacks)-1] // 去掉末尾的空栈（懒删除，堆中下标在 push 时处理）
	}
	return val
}

type hp struct{ sort.IntSlice }

func (h *hp) Push(v any) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() any   { a := h.IntSlice; v := a[len(a)-1]; h.IntSlice = a[:len(a)-1]; return v }

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * obj.Push(val);
 * param_2 := obj.Pop();
 * param_3 := obj.PopAtStack(index);
 */
// @lc code=end

