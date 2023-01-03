#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#
# https://leetcode.cn/problems/linked-list-components/description/
#
# algorithms
# Medium (59.34%)
# Likes:    150
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 54.2K
# Testcase Example:  '[0,1,2,3]\n[0,1,3]'
#
# 给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表 nums，该列表是上述链表中整型值的一个子集。
# 
# 返回列表 nums 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 nums 中）构成的集合。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入: head = [0,1,2,3], nums = [0,1,3]
# 输出: 2
# 解释: 链表中,0 和 1 是相连接的，且 nums 中不包含 2，所以 [0, 1] 是 nums 的一个组件，同理 [3] 也是一个组件，故返回
# 2。
# 
# 示例 2：
# 
# 
# 
# 
# 输入: head = [0,1,2,3,4], nums = [0,3,1,4]
# 输出: 2
# 解释: 链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数为n
# 1 <= n <= 10^4
# 0 <= Node.val < n
# Node.val 中所有值 不同
# 1 <= nums.length <= n
# 0 <= nums[i] < n
# nums 中所有值 不同
# 
# 
#
from typing import List, Optional
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
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        ans = mx = 0
        while head:
            if head.val in s:
                mx += 1
            else:
                if mx:
                    ans += 1
                mx = 0
            head = head.next
        if mx:
            ans += 1
        return ans
# @lc code=end

