from collections import defaultdict
from functools import cmp_to_key
from math import lcm, gcd

print("Hello, World!")
'''
n = 3
print([i for i in range(n)])
print([False] * n)
dp = [[False] * n for _ in range(n)]
print(dp)
'''
# num = 1234
# numStrList = list(str(num))
# numList = [int(x) for x in numStrList]
# numStrList.reverse()
# print(numStrList)
# print(numList)
# print("".join(numStrList))

# r = 0
# c = 0

# steps.append((r, c))
# steps.append((r, c))
# print([str(step[0]) + " " + str(step[0]) for step in steps])
# print(*[str(step[0]) + " " + str(step[1]) for step in steps], end="")
# print(steps[0])
'''
for step in steps:
    print(str(step[0]) + " " + str(step[1]))
'''

# a, b = 1, 2
# print(a//b)

# steps = list()
# steps.append(((1, 1), 1))
# steps.append(((0, 0), -1))
# steps.append(((3, 3), 2))
# steps.append(((4, 4), 0))
# steps.sort(key = lambda x: x[1])
# for step in steps:
#     print(str(step[0]) + " " + str(step[1]))

# vcount = defaultdict(int)
# v = 1
# # vcount[v] = 1
# # vcount[v] = vcount[v] + 1
# vcount[v] += 3
# v = 2
# vcount[v] += 2
# keys = list(sorted(vcount.items(), key = lambda x:x[1]))
# print(keys)

# vcount = [defaultdict(int) for _ in range(6)]
# vcount[0][1] += 2
# print(vcount)

# a = [(2,"ee"), (1,"lafzximxh")]

# print(a)

# def custom_key(a, b):
#     if a[0] != b[0]:
#         return a[0] - b[0]
#     else:
#         return b[1] < a[1]

# a.sort(reverse = True, key = lambda x:(x[0],x[1]))
# print(a)

# s = "L" * 10
# s += "R" * 10
# print("".join(s))

# a = [[] for _ in range(2)]
# a[0] = [2, 3]
# print(a)

# a, b = 4, 6
# print(lcm(a, b))
# a, b = -4, 6
# print(gcd(a, b))

expression = "-5/2+10/3+7/9"
for x in expression:
    print(x, x.isdigit())