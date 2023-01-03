class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        res = 0
        first = True

        if s[0] == '-':
            sign = -1
        else:
            sign = 1

        for x in s:
            if x in digit:
                res = res * 10 + int(x)
            elif first == True:
                if x == '-':
                    sign = -1
                elif x == ' ':
                    continue
                elif x != '+':
                    return 0
            else:
                res *= sign

                if res < INT_MIN:
                    return INT_MIN
                elif res > INT_MAX:
                    return INT_MAX
                else:
                    return res

            if first == True:
                first = False

        res *= sign

        if res < INT_MIN:
            return INT_MIN
        elif res > INT_MAX:
            return INT_MAX
        else:
            return res

    def myAtoi2(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        
    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1
