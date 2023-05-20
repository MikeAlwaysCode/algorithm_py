#
# @lc app=leetcode.cn id=1195 lang=python3
#
# [1195] 交替打印字符串
#
# https://leetcode.cn/problems/fizz-buzz-multithreaded/description/
#
# concurrency
# Medium (65.08%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    20.8K
# Total Submissions: 32K
# Testcase Example:  '15'
#
# 编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是：
# 
# 
# 如果这个数字可以被 3 整除，输出 "fizz"。
# 如果这个数字可以被 5 整除，输出 "buzz"。
# 如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。
# 
# 
# 例如，当 n = 15，输出： 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13,
# 14, fizzbuzz。
# 
# 假设有这么一个类：
# 
# 
# class FizzBuzz {
# public FizzBuzz(int n) { ... }               // constructor
# ⁠ public void fizz(printFizz) { ... }          // only output "fizz"
# ⁠ public void buzz(printBuzz) { ... }          // only output "buzz"
# ⁠ public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
# ⁠ public void number(printNumber) { ... }      // only output the numbers
# }
# 
# 请你实现一个有四个线程的多线程版  FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用：
# 
# 
# 线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。
# 线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。
# 线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。
# 线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。
# 
# 
# 
# 
# 提示：
# 
# 
# 本题已经提供了打印字符串的相关方法，如 printFizz() 等，具体方法名请参考答题模板中的注释部分。
# 
# 
# 
# 
#

# @lc code=start
from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.sem_fizz = Semaphore(0)
        self.sem_buzz = Semaphore(0)
        self.sem_fibu = Semaphore(0)
        self.sem_num = Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 != 0:
                self.sem_fizz.acquire()
                printFizz()
                self.sem_num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 != 0 and i % 5 == 0:
                self.sem_buzz.acquire()
                printBuzz()
                self.sem_num.release()


    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.sem_fibu.acquire()
                printFizzBuzz()
                self.sem_num.release()


    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.sem_num.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.sem_fibu.release()
            elif i % 3 == 0:
                self.sem_fizz.release()
            elif i % 5 == 0:
                self.sem_buzz.release()
            else:
                printNumber(i)
                self.sem_num.release()
# @lc code=end

