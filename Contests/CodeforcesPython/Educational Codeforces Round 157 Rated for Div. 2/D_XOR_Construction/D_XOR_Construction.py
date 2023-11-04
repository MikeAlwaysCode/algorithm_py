import sys
from functools import reduce
from operator import xor

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
    nums = ints()
    ans = [0] * n

    for i in range(1, n):
        ans[i] = nums[i - 1] ^ ans[i - 1]
    
    for bit in range(31):
        cnt = 0
        for b in ans:
            cnt += (b >> bit) & 1
        if cnt * 2 > n:
            for i in range(n):
                ans[i] ^= 1 << bit
        
    print(*ans)

solve()