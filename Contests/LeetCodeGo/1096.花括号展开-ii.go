/*
 * @lc app=leetcode.cn id=1096 lang=golang
 *
 * [1096] 花括号展开 II
 *
 * https://leetcode.cn/problems/brace-expansion-ii/description/
 *
 * algorithms
 * Hard (57.43%)
 * Likes:    64
 * Dislikes: 0
 * Total Accepted:    2.7K
 * Total Submissions: 4.6K
 * Testcase Example:  '"{a,b}{c,{d,e}}"'
 *
 * 如果你熟悉 Shell 编程，那么一定了解过花括号展开，它可以用来生成任意字符串。
 *
 * 花括号展开的表达式可以看作一个由 花括号、逗号 和 小写英文字母 组成的字符串，定义下面几条语法规则：
 *
 *
 * 如果只给出单一的元素 x，那么表达式表示的字符串就只有 "x"。R(x) = {x}
 *
 *
 * 例如，表达式 "a" 表示字符串 "a"。
 * 而表达式 "w" 就表示字符串 "w"。
 *
 *
 * 当两个或多个表达式并列，以逗号分隔，我们取这些表达式中元素的并集。R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪
 * ...
 *
 * 例如，表达式 "{a,b,c}" 表示字符串 "a","b","c"。
 * 而表达式 "{{a,b},{b,c}}" 也可以表示字符串 "a","b","c"。
 *
 *
 * 要是两个或多个表达式相接，中间没有隔开时，我们从这些表达式中各取一个元素依次连接形成字符串。R(e_1 + e_2) = {a + b for (a,
 * b) in R(e_1) × R(e_2)}
 *
 * 例如，表达式 "{a,b}{c,d}" 表示字符串 "ac","ad","bc","bd"。
 *
 *
 * 表达式之间允许嵌套，单一元素与表达式的连接也是允许的。
 *
 * 例如，表达式 "a{b,c,d}" 表示字符串 "ab","ac","ad"​​​​​​。
 * 例如，表达式 "a{b,c}{d,e}f{g,h}" 可以表示字符串 "abdfg", "abdfh", "abefg", "abefh",
 * "acdfg", "acdfh", "acefg", "acefh"。
 *
 *
 *
 *
 * 给出表示基于给定语法规则的表达式 expression，返回它所表示的所有字符串组成的有序列表。
 *
 * 假如你希望以「集合」的概念了解此题，也可以通过点击 “显示英文描述” 获取详情。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：expression = "{a,b}{c,{d,e}}"
 * 输出：["ac","ad","ae","bc","bd","be"]
 *
 * 示例 2：
 *
 *
 * 输入：expression = "{{a,z},a{b,c},{ab,z}}"
 * 输出：["a","ab","ac","z"]
 * 解释：输出中 不应 出现重复的组合结果。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= expression.length <= 60
 * expression[i] 由 '{'，'}'，',' 或小写英文字母组成
 * 给出的表达式 expression 用以表示一组基于题目描述中语法构造的字符串
 *
 *
 */

// @lc code=start
func braceExpansionII(expression string) []string {
	stk := [][]string{}
	res, cur := []string{}, []string{}
	for i := range expression {
		if expression[i] == ',' {
			res = append(res, cur...)
			cur = []string{}
		} else if expression[i] == '{' {
			stk = append(stk, res)
			stk = append(stk, cur)
			res, cur = []string{}, []string{}
		} else if expression[i] == '}' {
			res = append(res, cur...)
			pre := stk[len(stk)-1]
			cur := []string{}
			for _, s1 := range pre {
				for _, s2 := range res {
					cur = append(cur, s1+s2)
				}
			}

			res = stk[len(stk)-2]
			stk = stk[:len(stk)-2]
		} else {
			if len(cur) == 0 {
				cur = append(cur, string(expression[i]))
			} else {
				for i := range cur {
					cur[i] = cur[i] + string(expression[i])
				}
			}
		}
	}
	s := map[string]struct{}{}
	for _, s2 := range cur {
		s[s2] = struct{}
	}
	for _, s2 := range res {
		s[s2] = struct{}
	}
	ans := make([]string, 0, len(s))
	for k := range s {
		ans = append(ans, k)
	}
	sort.Strings(ans)
	return ans
	
	// s := map[string]struct{}{}
	// var dfs func(string)
	// dfs = func(exp string) {
	// 	j := strings.Index(exp, "}")
	// 	if j == -1 {
	// 		s[exp] = struct{}{}
	// 		return
	// 	}
	// 	i := strings.LastIndex(exp[:j], "{")
	// 	a, c := exp[:i], exp[j+1:]
	// 	for _, b := range strings.Split(exp[i+1:j], ",") {
	// 		dfs(a + b + c)
	// 	}
	// }
	// dfs(expression)
	// ans := make([]string, 0, len(s))
	// for k := range s {
	// 	ans = append(ans, k)
	// }
	// sort.Strings(ans)
	// return ans
}

// @lc code=end

