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
    cnt = [0] * (n + 1)
    first = [-1] * (n + 1)
    last = [-1] * (n + 1)
    for i, x in enumerate(nums, 1):
        cnt[x] += 1
        if first[x] == -1:
            first[x] = i
        last[x] = i
    if cnt[0] == 0:
        print(2)
        print(1, 1)
        print(2, n)
        return
    if cnt[0] == 1:
        print(-1)
        return
    l, r = first[0], last[0]
    for i in range(1, n + 1):
        if cnt[i] == 1:
            print(-1)
            return
        elif cnt[i] > 1:
            l = max(l, first[i])
            r = min(r, last[i])
            if r <= l:
                print(-1)
                return
        else:
            print(2)
            print(1, l)
            print(l + 1, n)
            return


for _ in range(int(input())):
    solve()
