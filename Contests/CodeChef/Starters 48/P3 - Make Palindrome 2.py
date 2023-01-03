from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())

    c = Counter(s)
    # sc = c.most_common(1)[0][0]
    
    ans = [c.most_common(1)[0][0]] * c.most_common(1)[0][1]
    
    print("".join(ans))