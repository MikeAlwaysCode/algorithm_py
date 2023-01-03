import random
import sys
from copy import deepcopy

random.seed(1)


class Result:

    def __init__(self, moves, connects):
        self.moves = moves
        self.connects = connects


class Solver:
    USED = 9
    VECS = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]

    def __init__(self, N, K, C):
        self.N = N
        self.K = K
        self.C = C
        self.LIM = K * 100

    def _move(self, lim=None):
        if lim is None:
            lim = self.K * 50
        moves = []
        for _ in range(lim):
            i = random.randint(0, self.N - 1)
            j = random.randint(0, self.N - 1)
            if self.C[i][j] == 0:
                continue
            v = random.choice(self.VECS)
            i2 = i + v[0]
            j2 = j + v[1]
            if i2 < 0 or i2 >= self.N or j2 < 0 or j2 >= self.N:
                continue
            if self.C[i2][j2] != 0:
                continue
            self.C[i2][j2] = self.C[i][j]
            self.C[i][j] = 0
            moves.append([i, j, i2, j2])
        return moves

    def _connect(self, lim: int):
        connects = []

        def can_connect(i, j, v):
            i2 = i + v[0]
            j2 = j + v[1]
            while i2 < self.N and j2 < self.N:
                if self.C[i2][j2] == 0:
                    i2 += v[0]
                    j2 += v[1]
                    continue
                elif self.C[i2][j2] == self.C[i][j]:
                    return True
                return False
            return False

        def do_connect(i, j, v):
            i2 = i + v[0]
            j2 = j + v[1]
            while i2 < self.N and j2 < self.N:
                if self.C[i2][j2] == 0:
                    self.C[i2][j2] = self.USED
                elif self.C[i2][j2] == self.C[i][j]:
                    connects.append([i, j, i2, j2])
                    return
                else:
                    raise AssertionError()
                i2 += v[0]
                j2 += v[1]

        for i in range(self.N):
            for j in range(self.N):
                if self.C[i][j] in (0, self.USED):
                    continue
                for v in [[0, 1], [1, 0]]:
                    if can_connect(i, j, v):
                        do_connect(i, j, v)
                        if len(connects) >= lim:
                            return connects
        return connects

    def solve(self):
        # create random moves
        moves = self._move()
        # from each computer, connect to right and/or bottom if it will reach the same type
        connects = self._connect(self.LIM - len(moves))

        return Result(moves, connects)


class UnionFind:

    def __init__(self):
        self.parents = {}

    def find(self, x):
        if x not in self.parents:
            self.parents[x] = x
            return x
        elif self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            self.parents[x] = y


def calc_score(N, K, C, res: Result):
    for v in res.moves:
        i, j, i2, j2 = v
        assert 1 <= C[i][j] <= K
        assert C[i2][j2] == 0
        C[i2][j2] = C[i][j]
        C[i][j] = 0

    uf = UnionFind()
    for v in res.connects:
        i, j, i2, j2 = v
        p1 = (i, j)
        p2 = (i2, j2)
        assert 1 <= C[i][j] <= K
        assert 1 <= C[i2][j2] <= K
        uf.unite(p1, p2)

    computers = []
    for i in range(N):
        for j in range(N):
            if 1 <= C[i][j] <= K:
                computers.append((i, j))

    score = 0
    for i in range(len(computers)):
        for j in range(i + 1, len(computers)):
            c1 = computers[i]
            c2 = computers[j]
            if uf.find(c1) != uf.find(c2):
                continue

            if C[c1[0]][c1[1]] == C[c2[0]][c2[1]]:
                score += 1
            else:
                score -= 1

    return max(score, 0)


def print_answer(res: Result):
    print(len(res.moves))
    for arr in res.moves:
        print(*arr)
    print(len(res.connects))
    for arr in res.connects:
        print(*arr)


def main():
    N, K = [int(v) for v in input().split(" ")]
    C = []

    for _ in range(N):
        C.append([int(v) for v in input()])

    solver = Solver(N, K, deepcopy(C))
    res = solver.solve()
    print(f"Score = {calc_score(N, K, deepcopy(C), res)}", file=sys.stderr)

    print_answer(res)


if __name__ == "__main__":
    main()
