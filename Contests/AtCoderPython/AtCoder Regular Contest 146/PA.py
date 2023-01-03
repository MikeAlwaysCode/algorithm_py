from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = []
ans.append(str(arr[-1]))
ans.append(str(arr[-2]))
ans.append(str(arr[-3]))
ans.sort(reverse=True)
print("".join(ans))