from collections import Counter, defaultdict
from threading import local
# from sortedcontainers import SortedSet, SortedList

rowa, cola = map(int, input().split())
arra = [[] for _ in range(rowa)]
for i in range(rowa):
    arra[i] = list(map(int, input().split()))

rowb, colb = map(int, input().split())
arrb = [[] for _ in range(rowb)]
for i in range(rowb):
    arrb[i] = list(map(int, input().split()))

hvec = list()
wvec = list()
match = False

for i in range(1<<rowa):
    for j in range(1<<cola):
        if bin(i).count("1") != rowa - rowb or bin(j).count("1") != cola - colb:
            continue

        hvec.clear()
        wvec.clear()

        for k in range(rowa):
            if not i & (1<<k):
                hvec.append(k)
        for k in range(cola):
            if not j & (1<<k):
                wvec.append(k)

        match = True
        for k in range(rowb):
            for l in range(colb):
                if arra[hvec[k]][wvec[l]] != arrb[k][l]:
                    match = False
                    break
            if not match:
                break
        
        if match:
            break
    if match:
        break

if match:
    print("Yes")
else:
    print("No")