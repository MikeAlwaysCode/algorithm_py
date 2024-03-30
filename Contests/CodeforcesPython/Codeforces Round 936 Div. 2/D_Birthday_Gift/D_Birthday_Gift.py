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

def solve() -> None:
    n, x = mint()
    nums = ints()
    s = 0
    cnt = [0] * 30
    for a in nums:
        s ^= a
        for bit in range(30):
            cnt[bit] += (a >> bit) & 1
    if s > x:
        print(-1)
        return
    ans = 1
    for bit in range(29, -1, -1):
        if cnt[bit] & 1:
            continue
        if (x >> bit) & 1:
            k = cur = 0
            mask = s | ((1 << bit) - 1)
            for a in nums:
                cur ^= a
                if cur | mask == mask:
                    k += 1
                    cur = 0
            ans = max(ans, k)
            if s | (1 << bit) <= x:
                s |= 1 << bit
    
    k = cur = 0
    for a in nums:
        cur ^= a
        if cur | s == s:
            k += 1
            cur = 0
    ans = max(ans, k)
    print(ans)


for _ in range(int(input())):
    solve()
