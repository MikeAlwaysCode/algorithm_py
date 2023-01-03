class GoThereExactly:
    def walk(self, r1, c1, r2, c2, s):
        dis = abs(r1 - r2) + abs(c1 - c2)

        round = s - dis
        # print(round)
        if (round < 0 or round & 1):
            return "IMPOSSIBLE"

        ans = ""
        if dis == 0 and s == 0:
            return ans
        
        if c2 >= c1:
            step1 = "L"
            step2 = "R"
        else:
            step1 = "R"
            step2 = "L"

        if r2 >= r1:
            step3 = "D"
        else:
            step3 = "U"

        ans = step1 * (round // 2) + step2 * (round // 2)
        ans += step2 * abs(c1 - c2)
        ans += step3 * abs(r1 - r2)

        return "".join(ans)

def main():
    # r1, c1, r2, c2, s = 18, 16, 16, 13, 5
    r1, c1, r2, c2, s = 4, 7, 4, 7, 12
    sol = GoThereExactly()

    print(sol.walk(r1, c1, r2, c2, s))

if __name__ == '__main__':
    main()