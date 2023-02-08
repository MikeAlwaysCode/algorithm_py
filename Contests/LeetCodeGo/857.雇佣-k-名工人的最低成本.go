/*
 * @lc app=leetcode.cn id=857 lang=golang
 *
 * [857] 雇佣 K 名工人的最低成本
 *
 * https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/description/
 *
 * algorithms
 * Hard (63.83%)
 * Likes:    295
 * Dislikes: 0
 * Total Accepted:    19.8K
 * Total Submissions: 31K
 * Testcase Example:  '[10,20,5]\n[70,50,30]\n2'
 *
 * 有 n 名工人。 给定两个数组 quality 和 wage ，其中，quality[i] 表示第 i 名工人的工作质量，其最低期望工资为
 * wage[i] 。
 *
 * 现在我们想雇佣 k 名工人组成一个工资组。在雇佣 一组 k 名工人时，我们必须按照下述规则向他们支付工资：
 *
 *
 * 对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。
 * 工资组中的每名工人至少应当得到他们的最低期望工资。
 *
 *
 * 给定整数 k ，返回 组成满足上述条件的付费群体所需的最小金额 。在实际答案的 10^-5 以内的答案将被接受。。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入： quality = [10,20,5], wage = [70,50,30], k = 2
 * 输出： 105.00000
 * 解释： 我们向 0 号工人支付 70，向 2 号工人支付 35。
 *
 * 示例 2：
 *
 *
 * 输入： quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
 * 输出： 30.66667
 * 解释： 我们向 0 号工人支付 4，向 2 号和 3 号分别支付 13.33333。
 *
 *
 *
 * 提示：
 *
 *
 * n == quality.length == wage.length
 * 1 <= k <= n <= 10^4
 * 1 <= quality[i], wage[i] <= 10^4
 *
 *
 */

// @lc code=start
func mincostToHireWorkers(quality []int, wage []int, k int) float64 {
	type pair struct{ q, w int }
	qw := make([]pair, len(quality))
	for i, q := range quality {
		qw[i] = pair{q, wage[i]}
	}
	sort.Slice(qw, func(i, j int) bool { a, b := qw[i], qw[j]; return a.w*b.q < b.w*a.q }) // 按照 r 值排序
	h := hp{make([]int, k)}
	sumQ := 0
	for i, p := range qw[:k] {
		h.IntSlice[i] = p.q
		sumQ += p.q
	}
	heap.Init(&h)
	ans := float64(sumQ*qw[k-1].w) / float64(qw[k-1].q) // 选 r 值最小的 k 名工人组成当前的最优解
	for _, p := range qw[k:] {
		if p.q < h.IntSlice[0] { // sumQ 可以变小，从而可能得到更优的答案
			sumQ -= h.IntSlice[0] - p.q
			h.IntSlice[0] = p.q
			heap.Fix(&h, 0) // 更新堆顶
			ans = math.Min(ans, float64(sumQ*p.w)/float64(p.q))
		}
	}
	return ans
}

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool { return h.IntSlice[i] > h.IntSlice[j] } // 最大堆
func (hp) Push(interface{})     {}                                       // 由于没有用到，可以什么都不写
func (hp) Pop() (_ interface{}) { return }

// @lc code=end

