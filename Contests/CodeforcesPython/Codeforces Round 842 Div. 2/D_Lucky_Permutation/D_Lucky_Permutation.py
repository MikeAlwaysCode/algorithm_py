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
    arr = ints()

    sa = sorted(arr)
    d = dict()
    for i in range(n):
        d[sa[i]] = i
    loops = 0
    flag = [0] * n
    for i in range(n):
        if not flag[i]:
            j = i
            while not flag[j]:
                flag[j] = loops + 1
                j = d[arr[j]]
            loops += 1
    k = n - loops

    for i in range(n - 1):
        if flag[i] == flag[i + 1]:
            print(k - 1)
            return

    print(k + 1)


for _ in range(int(input())):
    solve()
