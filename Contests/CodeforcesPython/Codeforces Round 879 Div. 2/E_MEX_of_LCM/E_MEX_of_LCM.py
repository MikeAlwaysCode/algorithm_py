import math
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

mxn = 2 * 10 ** 5
factor = [1] * (mxn + 1)

def init():
    for i in range(2, mxn + 1):
        if factor[i] != 1:
            continue
        for j in range(i, mxn + 1, i):
            factor[j] = i

def solve() -> None:
    n = sint()
    nums = ints()
    s = set(nums)
    left = dict()
    right = dict()
    for i in range(n):
        if nums[i] not in left:
            left[nums[i]] = i - 1
            right[nums[i]] = i + 1

    ans = 1
    while True:
        if ans not in s:
            p = factor[ans]
            if p == 1: break
            # while p in left and left[p] >= 0:

        ans += 1
    print(ans)

init()
for _ in range(int(input())):
    solve()