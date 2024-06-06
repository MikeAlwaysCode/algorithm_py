import sys
from collections import Counter
from random import getrandbits

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
    n = sint()
    A = ints()
    B = ints()
    m = sint()
    D = ints()
    h = getrandbits(30)
    cnt = Counter(b ^ h for a, b in zip(A, B) if a != b)
    s = set(b ^ h for b in B)
    if D[-1] ^ h not in s:
        print("NO")
        return
    for d in D:
        if cnt[d ^ h]:
            cnt[d ^ h] -= 1
    print("NO" if any(cnt.values()) else "YES")


for _ in range(int(input())):
    solve()
