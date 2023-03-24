/*
 * @lc app=leetcode.cn id=1626 lang=golang
 *
 * [1626] 无矛盾的最佳球队
 *
 * https://leetcode.cn/problems/best-team-with-no-conflicts/description/
 *
 * algorithms
 * Medium (41.85%)
 * Likes:    102
 * Dislikes: 0
 * Total Accepted:    10.1K
 * Total Submissions: 21K
 * Testcase Example:  '[1,3,5,10,15]\n[1,2,3,4,5]'
 *
 * 假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。
 *
 * 然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于
 * 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。
 *
 * 给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回
 * 所有可能的无矛盾球队中得分最高那支的分数 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
 * 输出：34
 * 解释：你可以选中所有球员。
 *
 * 示例 2：
 *
 * 输入：scores = [4,5,6,5], ages = [2,1,2,1]
 * 输出：16
 * 解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。
 *
 *
 * 示例 3：
 *
 * 输入：scores = [1,2,3,5], ages = [8,9,10,1]
 * 输出：6
 * 解释：最佳的选择是前 3 名球员。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= scores.length, ages.length <= 1000
 * scores.length == ages.length
 * 1 <= scores[i] <= 10^6
 * 1 <= ages[i] <= 1000
 *
 *
 */

// @lc code=start
type BIT []int

// 返回 max(maxSum[:i+1])
func (t BIT) query(i int) (mx int) {
	for ; i > 0; i &= i - 1 {
		mx = max(mx, t[i])
	}
	return
}

// 更新 maxSum[i] 为 mx
func (t BIT) update(i, mx int) {
	for ; i < len(t); i += i & -i {
		t[i] = max(t[i], mx)
	}
}

func bestTeamScore(scores, ages []int) (ans int) {
	type pair struct{ score, age int }
	a, u := make([]pair, len(scores)), 0
	for i, age := range ages {
		a[i] = pair{scores[i], age}
		u = max(u, age)
	}
	sort.Slice(a, func(i, j int) bool {
		a, b := a[i], a[j]
		return a.score < b.score || a.score == b.score && a.age < b.age
	})

	t := make(BIT, u+1)
	for _, p := range a {
		t.update(p.age, t.query(p.age)+p.score)
	}
	return t.query(u)
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

// func bestTeamScore(scores []int, ages []int) int {
// 	n := len(scores)
// 	type pair struct{ score, age int }
// 	a := make([]pair, n)
// 	for i, age := range ages {
// 		a[i] = pair{scores[i], age}
// 	}
// 	sort.Slice(a, func(i, j int) bool {
// 		a, b := a[i], a[j]
// 		return a.score < b.score || a.score == b.score && a.age < b.age
// 	})

// 	maxSum := make([]int, max(ages)+1)
// 	for _, p := range a {
// 		maxSum[p.age] = max(maxSum[:p.age+1]) + p.score
// 	}
// 	return max(maxSum)
// 	// ans := 0
// 	// n := len(scores)
// 	// type pair struct{ score, age int }
// 	// a := make([]pair, n)
// 	// for i, s := range scores {
// 	// 	a[i] = pair{s, ages[i]}
// 	// }
// 	// sort.Slice(a, func(i, j int) bool {
// 	// 	a, b := a[i], a[j]
// 	// 	return a.score < b.score || a.score == b.score && a.age < b.age
// 	// })

// 	// f := make([]int, n)
// 	// for i, p := range a {
// 	// 	for j, q := range a[:i] {
// 	// 		if q.age <= p.age {
// 	// 			f[i] = max(f[i], f[j])
// 	// 		}
// 	// 	}
// 	// 	f[i] += p.score
// 	// 	ans = max(ans, f[i])
// 	// }
// 	// return ans
// }
// func max(a []int) int {
// 	mx := a[0]
// 	for _, x := range a {
// 		if x > mx {
// 			mx = x
// 		}
// 	}
// 	return mx
// }

// func max(a, b int) int {
// 	if a < b {
// 		return b
// 	}
// 	return a
// }

// @lc code=end

