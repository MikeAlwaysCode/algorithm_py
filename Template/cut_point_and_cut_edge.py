class HashTable:  # 边表
    def __init__(self, edges: list, undirected: bool, n: int):
        self.hash_map = {}
        for i in range(n):
            self.hash_map.setdefault(i, set())
        for edge in edges:
            self.hash_map[edge[0]].add(edge[1])
            if (undirected):  # 无向图
                self.hash_map[edge[1]].add(edge[0])


class Tarjan:
    # 强连通分量Strong Connected Component，简称SCC
    # 割点/边问题Cut Point/Edge
    def __init__(self, n: int, edges: list):
        self.n = n
        self.edges = [None, None, None]
        self.edges[1] = HashTable(edges, False, n)
        self.edges[2] = HashTable(edges, True, n)
        self.stack = []
        self.dfn = [0 for _ in range(self.n)]
        self.low = [0 for _ in range(self.n)]
        self.index = 0
        self.answer_set = []  # 最终的SCC群
        self.answer_point = set()  # 最终的割点
        self.answer_edge = set()  # 最终的割边
        self.mode = 0  # 为了方便对照，两个问题使用mode变量区分，1为SCC，2为割点边

    def reload(self): # 重置
        self.stack = []
        self.dfn = [0 for _ in range(self.n)]
        self.low = [0 for _ in range(self.n)]
        self.index = 0
        self.answer_set = []
        self.answer_point = set()
        self.answer_edge = set()

    def scc(self):  # 强连通分量
        self.mode = 1
        for i in range(self.n):  # 防止漏点
            if (self.dfn[i]):
                continue
            self.targan(i, i)

    def cut_point_and_cut_edge(self):  # 割点/边问题
        self.mode = 2
        for i in range(self.n):  # 防止漏点（其实这是句废话，初始图不是连通的是啥情况？）
            if (self.dfn[i]):
                continue
            self.targan(i, i)

    def targan(self, now: int, father: int):
        self.index += 1  # 访问时间戳加1
        self.dfn[now] = self.low[now] = self.index  # 初始化当前节点的DFN和LOW

        if (self.mode == 1):
            self.stack.append(now)  # 压栈

        child_cnt = 0
        for i in self.edges[self.mode].hash_map[now]:  # 枚举边所能到的点
            if (self.dfn[i]):  # 已经被处理过
                if (i in self.stack and self.mode == 1):  # 如果i在栈内，now点能到达的最小时间戳是它自己能到达点的最小时间戳和i的时间戳的min
                    self.low[now] = min(self.low[now], self.dfn[i])
                    # 关于为什么是dfn[i]，这是因为low[i]可能被搜索树的其它子树更新过了，而
                    # dfn[i]并不会改变，在强连通分量里，这里改成now[i]没有任何问题，因为强连通分量只关注是不是同一个连通集合，但割点问题不行！
                    # 割点问题关心的是子树而不是集合，如果改成low[i]会导致子树的low和父树的low一致，导致子树合二为一，从而使得原本子树多于2的子节点无法被找到，从而出现遗漏

                if (self.mode == 2):
                    if (i == father):  # 注意不能回头
                        continue
                    self.low[now] = min(self.low[now], self.dfn[i])

            else:  # 没被处理过
                child_cnt += 1
                self.targan(i, now)  # DFS的本质
                self.low[now] = min(self.low[now], self.low[i])

        if (self.mode == 1):
            # 所有的边都访问过后，检查是否为强连通分量根节点（low == dfn）
            if (self.low[now] == self.dfn[now]):
                scc = set()
                while (self.stack[-1] != now):  # 开始弹栈
                    scc.add(self.stack.pop())
                scc.add(self.stack.pop())  # 不要忘记了它自己
                self.answer_set.append(scc)

        if (self.mode == 2):
            # 所有的边都访问过后，检查周围是否有low[i] > dfn[now]
            if (child_cnt >= 2 and father == now):  # 是根且子树多于2个，有割点没割边
                self.answer_point.add(now)
            for i in self.edges[self.mode].hash_map[now]:
                if (self.low[i] >= self.dfn[now] and father != now): # 有割点没割边 注意不能是根节点
                    self.answer_point.add(now)
                    if (self.low[i] > self.dfn[now]):
                        self.answer_edge.add((now, i))



if __name__ == '__main__':
    edges = [[0, 2], [2, 1], [1, 0], [2, 3], [3, 4], [4, 5], [3, 6], [6, 2], [2, 7], [7, 6]]
    #edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 0], [0, 5], [5, 4], [0, 6], [6, 7], [7, 0]]
    test = Tarjan(8, edges)
    # 强连通分量
    test.scc()
    print("强连通分量个数：", len(test.answer_set), "\n所有的强连通分量：", test.answer_set, "\n")

    test.reload()
    # 割点/边问题
    test.cut_point_and_cut_edge()
    print("割点集合：", test.answer_point, "\n割边集合：", test.answer_edge)