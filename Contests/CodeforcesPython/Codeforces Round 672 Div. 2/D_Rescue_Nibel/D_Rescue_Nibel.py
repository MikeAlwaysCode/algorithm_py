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

MOD = 998244353
# MOD = 10 ** 9 + 7

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, k = map(int, input().split())
    # rng = []
    # for _ in range(n):
    #     l, r = map(int, input().split())
    #     rng.append((l, r))
    
    '''
    # 1996 ms
    rng.sort()
    rng.append((10 ** 10, 0))
    h = []
    cnt = [0] * (n + 1)
    mx = 0
    for i in range(n + 1):
        if (h and h[0] < rng[i][0]) and len(h) >= k:
            cnt[len(h)] += 1
            if len(h) > mx:
                mx = len(h)
        if i == n:
            break
        chk = False
        while h and h[0] < rng[i][0]:
            chk = True
            heappop(h)
        if chk and len(h) >= k:
            cnt[len(h)] -= 1
        heappush(h, rng[i][1])
    ans = cnt[k]
    res = 1
    for i in range(k + 1, mx + 1):
        res = res * i * pow(i - k, MOD - 2, MOD) % MOD
        if cnt[i]:
            ans += res * cnt[i] % MOD
    ans %= MOD
    '''
    # # 差分哈希表 1902 ms
    # d = collections.defaultdict(int)
    # lcnt = collections.defaultdict(int)
    # for l, r in rng:
    #     d[l] += 1
    #     d[r + 1] -= 1
    #     lcnt[l] += 1
    
    # keys = list(d.keys())
    # keys.sort()
    # tot = dict()
    # s = 0
    # # cnt = collections.defaultdict(int)
    # # mx = 0
    # for key in keys:
    #     s += d[key]
    #     tot[key] = s
    #     # cnt[s] += 1
    #     # cnt[s - lcnt[key]] -= 1
    #     # mx = max(mx, s)
        
    # ans = cnt[k]
    # res = 1
    # for i in range(k + 1, mx + 1):
    #     res = res * i * pow(i - k, MOD - 2, MOD) % MOD
    #     if i in cnt:
    #         ans += res * cnt[i] % MOD
    # ans %= MOD

    # 预处理阶乘、逆元和组合数 1154 ms
    # 阶乘
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD
    # 逆元
    inverse = [0] * (n + 1)
    inverse[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inverse[i-1] = inverse[i] * i % MOD
    # 组合数
    def comb(n: int, m: int, MOD: int) -> int:
        if m < 0 or m > n:
            return 0
        return fact[n] * inverse[m] % MOD * inverse[n-m] % MOD

    # ans = 0
    # for key, v in lcnt.items():
    #     ans += comb(tot[key], k, MOD) - comb(tot[key] - v, k, MOD)
    # ans %= MOD
    # print(ans)

    # 扫描线 343 ms
    rng = []
    for _ in range(n):
        l, r = map(int, input().split())
        rng.append(l<<1|1)
        rng.append((r+1)<<1)
    rng.sort()
    ans = s = c = 0
    for i, x in enumerate(rng):
        s += (x & 1) * 2 - 1  # l: + 1, r: - 1
        if x & 1:   # l ?
            c += 1
            if not rng[i+1] & 1:    # l 后面一定会有 r，所以不会越界
                ans += comb(s, k, MOD) - comb(s - c, k, MOD)
                c = 0
    ans %= MOD
    print(ans)

# t = int(input())
# for _ in range(t):
solve()