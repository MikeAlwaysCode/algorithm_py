import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, k = mint()
    s = list(input())
    i = s.index("I")
    left = s[:i]
    right = s[:i:-1]
    # print(left)
    # print(right)
    for _ in range(k):
        op = input()
        if op == "backspace":
            if left:
                if right and left[-1] == '(' and right[-1] == ')':
                    right.pop()
                left.pop()
        else:
            if right:
                right.pop()
    print("".join(left) + "I" + "".join(right[::-1]))


solve()
