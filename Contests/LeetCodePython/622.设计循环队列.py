#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#
# https://leetcode.cn/problems/design-circular-queue/description/
#
# algorithms
# Medium (46.37%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    99.6K
# Total Submissions: 214.9K
# Testcase Example:  '["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n' + '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于
# FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
# 
# 
# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。
# 
# 你的实现应该支持如下操作：
# 
# 
# MyCircularQueue(k): 构造器，设置队列长度为 k 。
# Front: 从队首获取元素。如果队列为空，返回 -1 。
# Rear: 获取队尾元素。如果队列为空，返回 -1 。
# enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
# deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
# isEmpty(): 检查循环队列是否为空。
# isFull(): 检查循环队列是否已满。
# 
# 
# 
# 
# 示例：
# 
# MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
# circularQueue.enQueue(1);  // 返回 true
# circularQueue.enQueue(2);  // 返回 true
# circularQueue.enQueue(3);  // 返回 true
# circularQueue.enQueue(4);  // 返回 false，队列已满
# circularQueue.Rear();  // 返回 3
# circularQueue.isFull();  // 返回 true
# circularQueue.deQueue();  // 返回 true
# circularQueue.enQueue(4);  // 返回 true
# circularQueue.Rear();  // 返回 4
# 
# 
# 
# 提示：
# 
# 
# 所有的值都在 0 至 1000 的范围内；
# 操作数将在 1 至 1000 的范围内；
# 请不要使用内置的队列库。
# 
# 
#

# @lc code=start
class MyCircularQueue:
  def __init__(self, k: int):
    # self.capability = k
    self.queue = [0] * (k + 1)
    self.front = self.rear = 0

  def enQueue(self, value: int) -> bool:
    if self.isFull():
      return False
    else:
      self.queue[self.rear] = value
      self.rear = (self.rear + 1) % len(self.queue)
      return True

  def deQueue(self) -> bool:
    if self.isEmpty():
      return False
    else:
      self.front = (self.front + 1) % len(self.queue)
      return True

  def Front(self) -> int:
    if self.isEmpty():
      return -1
    else:
      return self.queue[self.front]


  def Rear(self) -> int:
    if self.isEmpty():
      return -1
    else:
      return self.queue[(self.rear - 1) % len(self.queue)]


  def isEmpty(self) -> bool:
    if self.rear == self.front:
      return True
    else:
      return False


  def isFull(self) -> bool:
    if (self.rear + 1) % len(self.queue) == self.front:
      return True
    else:
      return False
'''
class MyCircularQueue:
    def __init__(self, k: int):
        self.head = self.tail = None
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
'''

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
