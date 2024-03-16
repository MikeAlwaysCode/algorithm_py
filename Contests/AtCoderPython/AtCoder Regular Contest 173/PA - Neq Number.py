import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    k = sint()
    ans = []
    while k:
        ans.append(k % 9)
        k //= 9
    carry = 0
    for i in range(len(ans) - 1):
        if ans[i]:
            ans[i] -= carry
            carry = 0
        if ans[i] == 0:
            ans[i] = 9 - carry
            carry = 1
    ans[-1] -= carry

    for i in range(len(ans) - 2, -1, -1):
        if ans[i] == 0:
            ans[i + 1] -= 1
            ans[i] = 9
        elif ans[i] <= ans[i + 1]:
            ans[i] -= 1
    while ans[-1] == 0:
        ans.pop()
    ans.reverse()
    print(*ans, sep='')

for _ in range(sint()):
    solve()
