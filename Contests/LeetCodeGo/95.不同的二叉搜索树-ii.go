/*
 * @lc app=leetcode.cn id=95 lang=golang
 *
 * [95] 不同的二叉搜索树 II
 *
 * https://leetcode.cn/problems/unique-binary-search-trees-ii/description/
 *
 * algorithms
 * Medium (73.10%)
 * Likes:    1381
 * Dislikes: 0
 * Total Accepted:    158.1K
 * Total Submissions: 216.3K
 * Testcase Example:  '3'
 *
 * 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 3
 * 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：[[1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 *
 *
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return nil
	}
	return helper(1, n)
}

func helper(start, end int) []*TreeNode {
	if start > end {
		return []*TreeNode{nil}
	}
	allTrees := []*TreeNode{}
	// 枚举可行根节点
	for i := start; i <= end; i++ {
		// 获得所有可行的左子树集合
		leftTrees := helper(start, i-1)
		// 获得所有可行的右子树集合
		rightTrees := helper(i+1, end)
		// 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
		for _, left := range leftTrees {
			for _, right := range rightTrees {
				currTree := &TreeNode{i, nil, nil}
				currTree.Left = left
				currTree.Right = right
				allTrees = append(allTrees, currTree)
			}
		}
	}
	return allTrees
}

// @lc code=end

