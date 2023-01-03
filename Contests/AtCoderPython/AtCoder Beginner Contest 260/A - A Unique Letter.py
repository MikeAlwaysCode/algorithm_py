from collections import defaultdict
S = input()

c = defaultdict(int)
for x in S:
    c[x] += 1
# print(c)
print(next((k for k, v in c.items() if v == 1), -1))