/*
 * @lc app=leetcode.cn id=1233 lang=golang
 *
 * [1233] 删除子文件夹
 *
 * https://leetcode.cn/problems/remove-sub-folders-from-the-filesystem/description/
 *
 * algorithms
 * Medium (51.37%)
 * Likes:    99
 * Dislikes: 0
 * Total Accepted:    16.9K
 * Total Submissions: 30.1K
 * Testcase Example:  '["/a","/a/b","/c/d","/c/d/e","/c/f"]'
 *
 * 你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
 *
 * 如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的 子文件夹 。
 *
 * 文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：'/' 后跟一个或者多个小写英文字母。
 *
 *
 * 例如，"/leetcode" 和 "/leetcode/problems" 都是有效的路径，而空字符串和 "/" 不是。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
 * 输出：["/a","/c/d","/c/f"]
 * 解释："/a/b" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。
 *
 *
 * 示例 2：
 *
 *
 * 输入：folder = ["/a","/a/b/c","/a/b/d"]
 * 输出：["/a"]
 * 解释：文件夹 "/a/b/c" 和 "/a/b/d" 都会被删除，因为它们都是 "/a" 的子文件夹。
 *
 *
 * 示例 3：
 *
 *
 * 输入: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
 * 输出: ["/a/b/c","/a/b/ca","/a/b/d"]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= folder.length <= 4 * 10^4
 * 2 <= folder[i].length <= 100
 * folder[i] 只包含小写字母和 '/'
 * folder[i] 总是以字符 '/' 起始
 * 每个文件夹名都是 唯一 的
 *
 *
 */

// @lc code=start
// func removeSubfolders(folder []string) (ans []string) {
// 	sort.Strings(folder)
// 	ans = append(ans, folder[0])
// 	for _, f := range folder[1:] {
// 		last := ans[len(ans)-1]
// 		if !strings.HasPrefix(f, last) || f[len(last)] != '/' {
// 			ans = append(ans, f)
// 		}
// 	}
// 	return
// }
type Trie struct {
	children map[string]*Trie
	isEnd    bool
}

func newTrie() *Trie {
	m := map[string]*Trie{}
	return &Trie{children: m}
}

func (this *Trie) insert(w string) {
	node := this
	for _, p := range strings.Split(w, "/")[1:] {
		if _, ok := node.children[p]; !ok {
			node.children[p] = newTrie()
		}
		node, _ = node.children[p]
	}
	node.isEnd = true
}

func (this *Trie) search(w string) bool {
	node := this
	for _, p := range strings.Split(w, "/")[1:] {
		if _, ok := node.children[p]; !ok {
			return false
		}
		node, _ = node.children[p]
		if node.isEnd {
			return true
		}
	}
	return false
}

func removeSubfolders(folder []string) []string {
	sort.Slice(folder, func(i, j int) bool {
		return len(strings.Split(folder[i], "/")) < len(strings.Split(folder[j], "/"))
	})
	trie := newTrie()
	var ans []string
	for _, v := range folder {
		if !trie.search(v) {
			trie.insert(v)
			ans = append(ans, v)
		}
	}
	return ans
}

// @lc code=end

