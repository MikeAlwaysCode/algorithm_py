def solve() -> None:
    c = set()
    for _ in range(2):
        s = input()
        c.add(s[0])
        c.add(s[1])

    print(len(c) - 1)

t = int(input())
for _ in range(t):
    solve()