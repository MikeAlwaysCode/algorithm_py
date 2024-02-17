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
    nums = ints()
    pres = [0] * (n + 1)

    def check(x: int) -> bool:
        s = 0
        for i, a in enumerate(nums):
            pres[i + 1] = pres[i]
            if a >= x:
                pres[i + 1] += 1
            else:
                pres[i + 1] -= 1
            if i >= k:
                s = min(s, pres[i + 1 - k])
            if i + 1 >= k and pres[i + 1] - s > 0:
                return True
            
        return False

    l, r = min(nums), max(nums)
    while l < r:
        mid = (l + r + 1) >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)

solve()
