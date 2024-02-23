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
    nums = ints()
    qry = []
    for _ in range(sint()):
        qry.append(ints())
    seen = [False] * n
    mx = 0
    for q in qry[::-1]:
        if q[0] == 2:
            mx = max(mx, q[1])
        elif not seen[q[1] - 1]:
            nums[q[1] - 1] = max(q[2], mx)
            seen[q[1] - 1] = True
    for i in range(n):
        if seen[i]:
            continue
        nums[i] = max(nums[i], mx)
    print(*nums)


solve()
