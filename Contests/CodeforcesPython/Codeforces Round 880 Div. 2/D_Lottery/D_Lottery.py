from collections import Counter
import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# # region interactive
# def printQry(a, b) -> None:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = True)

# def printAns(ans) -> None:
#     s = str(ans)
#     print(f"! {s}", flush = True)
# # endregion interactive

# # region dfsconvert
# from types import GeneratorType
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc
# # endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m, k = mint()
    nums = ints()
    nums.sort()
    if k == 1:
        cur = 0
        for x in nums:
            if x > cur:
                break
            else:
                cur = x + 1
        if cur > m:
            print(0, 0)
        else:
            print(1, cur)
        return
    
    if n < k:
        print(m + 1, 0)
        return
    if n == k:
        print(m + 1, nums[0] + 1)
        return
    
    cnt = Counter(nums)
    mx, x = nums[k - 1] // 2 + 1, 0
    lst = sorted(cnt.items())
    s = l = 0

solve()