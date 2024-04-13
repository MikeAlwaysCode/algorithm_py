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
    s = input()
    cntb = [0] * (n + 1)
    cntr = [0] * (n + 1)
    for i, v in enumerate(nums):
        if s[i] == 'B':
            if v < 1:
                print("NO")
                return
            cntb[min(v, n)] += 1
        else:
            if v > n:
                print("NO")
                return
            cntr[max(1, v)] += 1
    left = 0
    for i in range(1, n + 1):
        left += 1 - cntb[i]
        if left < 0:
            print("NO")
            return
    left = 0
    for i in range(n, 0, -1):
        left += 1 - cntr[i]
        if left < 0:
            print("NO")
            return
    print("YES")


for _ in range(int(input())):
    solve()
