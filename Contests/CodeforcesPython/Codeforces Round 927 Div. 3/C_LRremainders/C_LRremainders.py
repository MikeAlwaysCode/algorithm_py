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
    n, m = mint()
    nums = ints()
    s = input()
    i, k = s.count('L') - int(s[-1] == 'L'), n - 2
    cur = nums[i] % m
    ans = [cur]
    j = i + 1
    i -= 1
    while k >= 0:
        if s[k] == 'L':
            cur = cur * nums[i] % m
            i -= 1
        else:
            cur = cur * nums[j] % m
            j += 1
        k -= 1
        ans.append(cur)
        
    print(*reversed(ans))


for _ in range(int(input())):
    solve()
