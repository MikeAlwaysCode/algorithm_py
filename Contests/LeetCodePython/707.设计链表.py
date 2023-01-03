#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#
# https://leetcode.cn/problems/design-linked-list/description/
#
# algorithms
# Medium (33.93%)
# Likes:    521
# Dislikes: 0
# Total Accepted:    138.8K
# Total Submissions: 409.1K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +  '[[],[1],[3],[1,2],[1],[1],[1]]'
#
# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next
# 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
# 
# 在链表类中实现这些功能：
# 
# 
# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index
# 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
# 
# 
# 
# 
# 示例：
# 
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
# linkedList.get(1);            //返回2
# linkedList.deleteAtIndex(1);  //现在链表是1-> 3
# linkedList.get(1);            //返回3
# 
# 
# 
# 
# 提示：
# 
# 
# 所有val值都在 [1, 1000] 之内。
# 操作次数将在  [1, 1000] 之内。
# 请不要使用内置的 LinkedList 库。
# 
# 
#

# @lc code=start
# 1. 单链表
'''
class ListNode:
  def __init__(self, val: int) -> None:
    self.val = val
    self.next = None

class MyLinkedList:

  def __init__(self):
    self.size = 0
    self.head = ListNode(0)

  def get(self, index: int) -> int:
    if index < 0 or index >= self.size:
      return -1
    
    cur = self.head.next
    while index > 0:
      cur = cur.next
      index -= 1
    return cur.val

  def addAtHead(self, val: int) -> None:
    self.addAtIndex(0, val)

  def addAtTail(self, val: int) -> None:
    self.addAtIndex(self.size, val)

  def addAtIndex(self, index: int, val: int) -> None:
    if index > self.size:
      return

    self.size += 1

    index = max(index, 0)
    cur = self.head
    for _ in range(index):
      cur = cur.next
    newNode = ListNode(val)
    newNode.next = cur.next
    cur.next = newNode

  def deleteAtIndex(self, index: int) -> None:
    if index < 0 or index >= self.size:
      return
    
    self.size -= 1

    cur = self.head
    for _ in range(index):
      cur = cur.next
    cur.next = cur.next.next
'''
# 2. 双链表
class ListNode:
  def __init__(self, val: int) -> None:
    self.val = val
    self.prev = self.next = None

class MyLinkedList:

  def __init__(self):
    self.size = 0
    self.head = ListNode(0)
    self.tail = ListNode(0)
    self.head.next = self.tail
    self.tail.prev = self.head

  def get(self, index: int) -> int:
    if index < 0 or index >= self.size:
      return -1
    
    if index + 1 < self.size - index:
      # 从前往后
      curr = self.head
      for _ in range(index + 1):
          curr = curr.next
    else:
      # 从后往前
      curr = self.tail
      for _ in range(self.size - index):
          curr = curr.prev

    return curr.val

  def addAtHead(self, val: int) -> None:
    self.addAtIndex(0, val)

  def addAtTail(self, val: int) -> None:
    self.addAtIndex(self.size, val)

  def addAtIndex(self, index: int, val: int) -> None:
    if index > self.size:
      return

    index = max(index, 0)

    newNode = ListNode(val)
    if index <= self.size - index:
      pred = self.head
      for _ in range(index):
        pred = pred.next
      succ = pred.next
    else:
      succ = self.tail
      for _ in range(self.size - index):
        succ = succ.prev
      pred = succ.prev
    
    newNode = ListNode(val)
    newNode.next = succ
    newNode.prev = pred
    pred.next = newNode
    succ.prev = newNode

    self.size += 1

  def deleteAtIndex(self, index: int) -> None:
    if index < 0 or index >= self.size:
      return
    
    if index < self.size - index:
      pred = self.head
      for _ in range(index):
        pred = pred.next
      succ = pred.next.next
    else:
      succ = self.tail
      for _ in range(self.size - index - 1):
        succ = succ.prev
      pred = succ.prev.prev
    
    pred.next = succ
    succ.prev = pred
    self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

