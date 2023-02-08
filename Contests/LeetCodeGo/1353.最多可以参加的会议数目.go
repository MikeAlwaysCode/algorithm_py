/*
 * @lc app=leetcode.cn id=1353 lang=golang
 *
 * [1353] 最多可以参加的会议数目
 *
 * https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/description/
 *
 * algorithms
 * Medium (29.50%)
 * Likes:    244
 * Dislikes: 0
 * Total Accepted:    17.6K
 * Total Submissions: 59.6K
 * Testcase Example:  '[[1,2],[2,3],[3,4]]'
 *
 * 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于
 * endDayi 。
 *
 * 你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。注意，一天只能参加一个会议。
 *
 * 请你返回你可以参加的 最大 会议数目。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：events = [[1,2],[2,3],[3,4]]
 * 输出：3
 * 解释：你可以参加所有的三个会议。
 * 安排会议的一种方案如上图。
 * 第 1 天参加第一个会议。
 * 第 2 天参加第二个会议。
 * 第 3 天参加第三个会议。
 *
 *
 * 示例 2：
 *
 *
 * 输入：events= [[1,2],[2,3],[3,4],[1,2]]
 * 输出：4
 *
 *
 *
 *
 * 提示：​​​​​​
 *
 *
 * 1 <= events.length <= 10^5
 * events[i].length == 2
 * 1 <= startDayi <= endDayi <= 10^5
 *
 *
 */

// @lc code=start
func maxEvents(events [][]int) int {
	sort.Slice(events, func(i, j int) bool {
		if events[i][0] == events[j][0] {
			return events[i][1] <= events[j][1]
		} else {
			return events[i][0] < events[j][0]
		}
	})
	h := &hp{}
	var ans, curr int
	for i := 0; i < len(events) || h.Len() > 0; {
		if h.Len() > 0 && (i >= len(events) || curr < events[i][0]) {
			e := heap.Pop(h).(int)
			if e >= curr {
				ans++
				curr++
			}
		} else {
			heap.Push(h, events[i][1])
			curr = events[i][0]
			i++
		}
	}
	return ans
}

type hp struct{ sort.IntSlice }

// func (h hp) Less(i, j int) bool  { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}

// @lc code=end

