import math
import collections
import random
from heapq import heapify, heappush, heappop
from functools import reduce
from bisect import bisect, bisect_left

# Sample Inputs/Output 
# region fastio
import sys, os
from io import BytesIO, IOBase
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
        
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n = int(input())
    # tree = [[] for _ in range(n)]
    vals = [0] * n
    root = 0
    tot = 0
    incnt = [0] * n
    parent = [0] * n
    for i in range(n):
        p, v = map(int, input().split())
        vals[i] = v
        tot += v
        if p == 0:
            root = i
        else:
            # tree[i].append(p-1)
            # tree[p - 1].append(i)
            incnt[p - 1] += 1
            parent[i] = p - 1
            
    if tot % 3 != 0:
        print(-1)
        return
    
    target = tot // 3
    ans = []

    # # DFS
    # def dfs(x, p) -> int:
    #     res = vals[x]

    #     if len(ans) == 2:
    #         return res

    #     for u in tree[x]:
    #         if u == p:
    #             continue
    #         sub = dfs(u, x)
    #         res += sub
        
    #     if res == target:
    #         if x != root:
    #             ans.append(x+1)
    #         return 0
    #     else:
    #         return res

    # dfs(root, -1)

    # # BFS
    # parent = [0] * n
    # nodes = []
    # # q = [(root, -1)]
    # q = [root]
    # while q:
    #     tmp = q
    #     q = []
    #     # curNode = []
    #     nodes.append(list())
    #     for x in tmp:
    #         # curNode.append(x)
    #         nodes[-1].append(x)
    #         # parent[x] = p
    #         for u in tree[x]:
    #             # if u != p:
    #                 # q.append((u, x))
    #             parent[u] = x
    #             q.append(u)
    #     # nodes.append(curNode)
    #     # nodes = curNode

    # # cnt = [0] * n    
    # for i in range(len(nodes) - 1, -1, -1):
    #     curNode = nodes[i]
    #     for x in curNode:
    #         # cnt[x] += vals[x]
    #         # if cnt[x] == target:
    #         #     cnt[x] = 0
    #         if vals[x] == target:
    #             vals[x] = 0
    #             ans.append(x+1)
    #             if len(ans) == 2:
    #                 print(*ans)
    #                 return
                
    #         # cnt[parent[x]] += cnt[x]
    #         vals[parent[x]] += vals[x]

    q = collections.deque(i for i, v in enumerate(incnt) if v == 0)
            
    while q:
        x = q.popleft()
        if vals[x] == target:
            vals[x] = 0
            if x != root:
                ans.append(x+1)
        if len(ans) == 2:
            print(*ans)
            return
        
        vals[parent[x]] += vals[x]
        incnt[parent[x]] -= 1

        if not incnt[parent[x]]:
            q.append(parent[x])

    if len(ans) < 2:
        print(-1)
    else:
        print(*ans)

# t = int(input())
# for _ in range(t):
solve()