from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

N = int(input())
arr = list(map(int, input().split()))
ans = list()

def operate(i: int):
    ans.append(i+1)
    arr[i], arr[i+1] = arr[i+1], arr[i]

i = 0
while i < N * 2 - 1:
    order = i&1
    if order == (arr[i] > arr[i+1]):
        i += 1
    else:
        if i < N*2 - 2 and order == (arr[i+2] < arr[i]):
            operate(i+1)
        else:
            operate(i)
        i += 2

print(len(ans))
print(*ans)
