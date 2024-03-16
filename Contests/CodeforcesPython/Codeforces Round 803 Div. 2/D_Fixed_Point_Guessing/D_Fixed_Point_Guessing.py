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
    n = sint()
    l, r = 1, n
    while l < r:
        mid = (l + r) // 2
        if (mid - l) & 1:
            mid -= 1
        print(f"? {l} {mid}", flush=True)
        nums = ints()
        cnt = 0
        for x in nums:
            if x < l or x > mid:
                cnt += 1
        if cnt & 1:
            l, r = mid + 1, r
        else:
            l, r = l, mid
    print(f"! {l}", flush=True)

for _ in range(int(input())):
    solve()
