import math
import itertools
import sys

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

def check(x: int) -> bool:
    return pow(math.isqrt(x), 2) == x

def solve() -> None:
    n = sint()

    if n == 1:
        print(1)
        return
    
    if n == 3:
        print(169, 196, 961)
        return
    
    d = ['1', '6', '9']
    zero = n - 3
    ans = []
    for p in itertools.permutations(d):
        for n1 in range(zero + 1):
            for n2 in range(zero - n1 + 1):
                s = p[0] + '0' * n1 + p[1] + '0' * n2 + p[2] + '0' * (zero - n1 - n2)
                if check(int(s)):
                    ans.append(s)
                    if len(ans) >= n:
                        print(*ans)
                        return


for _ in range(int(input())):
    solve()