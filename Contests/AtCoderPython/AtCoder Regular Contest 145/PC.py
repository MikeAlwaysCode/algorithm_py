from collections import defaultdict
N = int(input())

s = defaultdict(int)
for i in range(N):
    f = input()
    if s[f] == 0:
        print(f)
    else:
        print(f + '(' + str(s[f]) + ')')
    
    s[f] += 1