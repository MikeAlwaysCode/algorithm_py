from collections import Counter, defaultdict

# from sortedcontainers import SortedSet, SortedList

d = {"Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5}

# N = int(input())
S = str(input())
# t = int(input())
# for _ in range(t):
#     n, m, k = map(int, input().split())
#     arr = list(map(int, input().split()))

ans = 6 - d[S]
    
print(ans)