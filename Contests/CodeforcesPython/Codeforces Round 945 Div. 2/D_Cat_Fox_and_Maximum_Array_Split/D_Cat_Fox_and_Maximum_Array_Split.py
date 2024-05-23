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
    n, k = mint()

    mx = -1
    for i in range(1, n + 1):
        x = i * n
        print(f"? 1 {x}", flush=True)
        r = sint()
        if r == n:
            mx = i
            break
    ans = -1
    for l in range(1, n // k + 1):
        cnt = r = 0
        x = mx * l
        while r < n and cnt < k:
            l = r + 1
            print(f"? {l} {x}", flush=True)
            r = sint()
            if r <= n:
                cnt += 1
        if cnt == k and r == n:
            ans = x
            break
    print(f"! {ans}", flush=True)
    sint()


for _ in range(int(input())):
    solve()
