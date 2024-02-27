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
    m, n = mint()
    days = ints()
    nums = ints()

    if m < n:
        print(-1)
        return

    def check(x: int) -> bool:
        last = [-1] * n
        for i in range(x):
            if days[i]:
                last[days[i] - 1] = i
        if -1 in last:
            return False

        cnt = 0
        for i in range(x):
            if i == last[days[i] - 1]:
                if nums[days[i] - 1] > cnt:
                    return False
                cnt -= nums[days[i] - 1]
            else:
                cnt += 1
        return True
    
    l, r = n, m + 1
    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1

    print(-1 if r > m else r)

solve()
