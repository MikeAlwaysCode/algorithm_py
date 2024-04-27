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
    ans = []
    d = dict()
    for i in range(1, n + 1):
        k = sint()
        nums = ints()
        if ans:
            continue
        s = sum(nums)
        for j, x in enumerate(nums, 1):
            if s - x in d and d[s - x][0] < i:
                ans.append(d[s - x])
                ans.append((i, j))
                break
            d[s - x] = (i, j)
    
    if ans:
        print("YES")
        print(*ans[0])
        print(*ans[1])
    else:
        print("NO")


solve()
