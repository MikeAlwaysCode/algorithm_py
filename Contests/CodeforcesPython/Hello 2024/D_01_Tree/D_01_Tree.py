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
    return


for _ in range(int(input())):
    solve()
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low = str(start)
        high = str(finish)
        n = len(high)
        low = '0' * (n - len(low)) + low  # 补前导零，和 high 对齐
        diff = n - len(s)

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 个数位可以从 lo 枚举到 hi
            # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9

            res = 0
            if i < diff:  # 枚举这个数位填什么
                for d in range(lo, min(hi, limit) + 1):
                    res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            else:  # 这个数位只能填 s[i-diff]
                x = int(s[i - diff])
                if lo <= x <= min(hi, limit):
                    res = dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
            return res

        return dfs(0, True, True)