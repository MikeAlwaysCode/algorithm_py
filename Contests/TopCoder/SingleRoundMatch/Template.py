class WordleColors:
    def color(self, hidden, guess):
        count = [0] * 5
        ans = ['-'] * 5
        for i in range(5):
            if guess[i] == hidden[i]:
                ans[i] = 'g'
                count[i] += 1
        for i in range(5):
            if ans[i] != 'g':
                for j in range(5):
                    if j == i: continue
                    if guess[i] == hidden[j] and count[j] == 0:
                        ans[i] = ('y')
                        count[j] += 1
                        break

        return "".join(ans)
        
def main():
    r1, c1, r2, c2, s = 4, 7, 4, 7, 12
    # sol = WordleColors()

    # print(sol.color(r1, c1, r2, c2, s))

if __name__ == '__main__':
    main()