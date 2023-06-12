#
# @lc app=leetcode.cn id=1171 lang=python3
#
# [1171] 从链表中删去总和值为零的连续节点
#
# https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/
#
# algorithms
# Medium (48.45%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 45.4K
# Testcase Example:  '[1,2,-3,3,1]'
#
# 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
# 
# 删除完毕后，请你返回最终结果链表的头节点。
# 
# 
# 
# 你可以返回任何满足题目要求的答案。
# 
# （注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）
# 
# 示例 1：
# 
# 输入：head = [1,2,-3,3,1]
# 输出：[3,1]
# 提示：答案 [1,2,1] 也是正确的。
# 
# 
# 示例 2：
# 
# 输入：head = [1,2,3,-3,4]
# 输出：[1,2,4]
# 
# 
# 示例 3：
# 
# 输入：head = [1,2,3,-3,-2]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 给你的链表中可能有 1 到 1000 个节点。
# 对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
# 
# 
#
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = dict()
        t = dict()
        st = dict()
        time = s = 0
        node = head
        while node:
            time += 1
            s += node.val
            if s == 0:
                head = node.next
                time = 0
            elif s in t and t[s] < time and st[t[s]] == s:
                d[t[s]].next = node.next
                time = t[s]
            else:
                t[s] = time
                st[time] = s
                d[time] = node
            node = node.next
        return head
# @lc code=end

