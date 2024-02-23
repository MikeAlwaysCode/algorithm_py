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
    n, q = mint()
    nums = ints()
    cnt = [0] * (n + 1)
    pres = [0] * (n + 1)
    for i in range(n):
        pres[i + 1] = pres[i] + nums[i]
        cnt[i + 1] = cnt[i] + (nums[i] == 1)
    
    for _ in range(q):
        l, r = mint()
        if l == r:
            print("NO")
        else:
            s, c = pres[r] - pres[l - 1], cnt[r] - cnt[l - 1]
            print("YES" if s - r + l - 1 >= c else "NO")

for _ in range(int(input())):
    solve()
