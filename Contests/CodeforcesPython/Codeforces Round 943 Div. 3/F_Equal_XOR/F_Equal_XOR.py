import sys
from collections import defaultdict
from bisect import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, q = mint()
    nums = ints()
    xors = [0] * (n + 1)
    pos = defaultdict(list)
    
    for i, x in enumerate(nums, 1):
        xors[i] = xors[i - 1] ^ x
        pos[xors[i]].append(i)
    for _ in range(q):
        l, r = mint()
        x = xors[r] ^ xors[l - 1]
        if x == 0:
            print("YES")
            continue
        i = bisect_left(pos[xors[r]], l)
        if i >= len(pos[xors[r]]):
            print("NO")
            continue
        cl = pos[xors[r]][i]
        i = bisect(pos[xors[l - 1]], cl)
        if i >= len(pos[xors[l - 1]]):
            print("NO")
            continue
        cr = pos[xors[l - 1]][i]
        print("YES" if cr < r else "NO")

    '''
    # cnt = [[0] * (n + 1) for _ in range(31)]
    pos = [[] for _ in range(31)]
    for i, x in enumerate(nums, 1):
        xors[i] = xors[i - 1] ^ x
        for bit in range(31):
            # cnt[bit][i] = cnt[bit][i - 1]
            if (x >> bit) & 1:
                # cnt[bit][i] += 1
                pos[bit].append(i)
    for _ in range(q):
        l, r = mint()
        x = xors[r] ^ xors[l - 1]
        if x == 0:
            print("YES")
            continue
        cr = r
        for bit in range(31):
            mask = (1 << (bit + 1)) - 1
            if (xors[r] ^ xors[cr]) & mask == x & mask:
                continue
            i = bisect(pos[bit], cr)
            while i > 0 and pos[bit][i - 1] - 1 > l:
                cr = pos[bit][i - 1] - 1
                if (xors[r] ^ xors[cr]) & mask == x & mask:
                    break
                i -= 2
            if i <= 0 or cr <= l:
                break
        if cr <= l or xors[r] ^ xors[cr] != x:
            print("NO")
            continue
        cl = l - 1
        for bit in range(31):
            mask = (1 << (bit + 1)) - 1
            if (xors[cl] ^ xors[l - 1]) & mask == x & mask:
                continue
            i = bisect(pos[bit], cl)
            while i < len(pos[bit]) and pos[bit][i] < cr:
                cl = pos[bit][i]
                if (xors[cl] ^ xors[l - 1]) & mask == x & mask:
                    break
                i += 2
            if i >= len(pos[bit]) or cl >= cr:
                break
        if cl >= cr or xors[cl] ^ xors[l - 1] != x:
            print("NO")
            continue
        print("YES")
    '''

for _ in range(int(input())):
    solve()
