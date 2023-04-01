/*
 * @lc app=leetcode.cn id=691 lang=golang
 *
 * [691] 贴纸拼词
 *
 * https://leetcode.cn/problems/stickers-to-spell-word/description/
 *
 * algorithms
 * Hard (59.55%)
 * Likes:    258
 * Dislikes: 0
 * Total Accepted:    23.4K
 * Total Submissions: 39.3K
 * Testcase Example:  '["with","example","science"]\n"thehat"'
 *
 * 我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。
 *
 * 您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。
 *
 * 返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。
 *
 * 注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入： stickers = ["with","example","science"], target = "thehat"
 * 输出：3
 * 解释：
 * 我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
 * 把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
 * 此外，这是形成目标字符串所需的最小贴纸数量。
 *
 *
 * 示例 2:
 *
 *
 * 输入：stickers = ["notice","possible"], target = "basicbasic"
 * 输出：-1
 * 解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
 *
 *
 *
 * 提示:
 *
 *
 * n == stickers.length
 * 1 <= n <= 50
 * 1 <= stickers[i].length <= 10
 * 1 <= target.length <= 15
 * stickers[i] 和 target 由小写英文单词组成
 *
 *
 */

// @lc code=start
func minStickers(stickers []string, target string) int {
	targetSet := map[rune]bool{}
	for _, r := range target {
		targetSet[r] = true
	}
	availables := []map[rune]int{}
	for _, s := range stickers {
		if c := getCounter(s, targetSet); c != nil {
			availables = append(availables, c)
		}
	}
	queue, explored := []string{target}, map[string]int{target: 0}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, avl := range availables {
			if avl[rune(cur[0])] > 0 {
				nxt := transfer(cur, avl)
				if len(nxt) == 0 {
					return explored[cur] + 1
				}
				if _, ok := explored[nxt]; !ok {
					queue = append(queue, nxt)
					explored[nxt] = explored[cur] + 1
				}
			}
		}
	}
	return -1
}

func getCounter(s string, chars map[rune]bool) map[rune]int {
	res := map[rune]int{}
	for _, r := range s {
		if chars[r] {
			res[r]++
		}
	}
	if len(res) == 0 {
		return nil
	}
	return res
}

func transfer(s string, mp map[rune]int) string {
	for k, v := range mp {
		s = strings.Replace(s, string(k), "", v)
	}
	return s
}

// @lc code=end

