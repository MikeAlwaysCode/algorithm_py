#
# @lc app=leetcode.cn id=1115 lang=python3
#
# [1115] 交替打印 FooBar
#
# https://leetcode.cn/problems/print-foobar-alternately/description/
#
# concurrency
# Medium (56.97%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    63.8K
# Total Submissions: 111.9K
# Testcase Example:  '1'
#
# 给你一个类：
# 
# 
# class FooBar {
# ⁠ public void foo() {
# for (int i = 0; i < n; i++) {
# print("foo");
# }
# ⁠ }
# 
# ⁠ public void bar() {
# for (int i = 0; i < n; i++) {
# print("bar");
# }
# ⁠ }
# }
# 
# 
# 两个不同的线程将会共用一个 FooBar 实例：
# 
# 
# 线程 A 将会调用 foo() 方法，而
# 线程 B 将会调用 bar() 方法
# 
# 
# 请设计修改程序，以确保 "foobar" 被输出 n 次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 1
# 输出："foobar"
# 解释：这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 2
# 输出："foobarfoobar"
# 解释："foobar" 将被输出两次。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 1000
# 
# 
#
# @lc code=start
from threading import Lock
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockFoo = Lock()
        self.lockBar = Lock()
        self.lockBar.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lockFoo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lockBar.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lockBar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lockFoo.release()
# @lc code=end

