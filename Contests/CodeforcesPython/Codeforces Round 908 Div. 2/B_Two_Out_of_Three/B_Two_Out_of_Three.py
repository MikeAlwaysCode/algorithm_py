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
    cnt = 0
    pos = [[] for _ in range(101)]
    for i, x in enumerate(nums):
        pos[x].append(i)
        if len(pos[x]) == 2:
            cnt += 1
    if cnt < 2:
        print(-1)
        return
    ans = [3] * n
    for arr in pos:
        if len(arr) > 1:
            ans[arr[0]] = 2 - (cnt & 1)
            cnt -= 1
    print(*ans)


for _ in range(int(input())):
    solve()
