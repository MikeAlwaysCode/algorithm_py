package main

import (
	"bufio"
	"container/heap"
	. "fmt"
	"io"
	"os"
	"sort"
)

func CF229B(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	type p struct{ v, w int }

	var n, m, u, v, w, kc int
	Fscan(in, &n, &m)
	g := make([][]p, n)
	for i := 0; i < m; i++ {
		Fscan(in, &u, &v, &w)
		u--
		v--
		g[u] = append(g[u], p{v, w})
		g[v] = append(g[v], p{u, w})
	}
	k := make([][]int, n)
	for i := range k {
		Fscan(in, &kc)
		if kc == 0 {
			continue
		}
		k[i] = make([]int, kc)
		for j := range k[i] {
			Fscan(in, &k[i][j])
		}
	}
	h := &hp{pair{0, -1, 0}}
	visit := make([]int, n)
	for i := range visit {
		visit[i] = -1
	}
	visit[0] = 0

	for h.Len() > 0 {
		cur := heap.Pop(h).(pair)
		u, fa, t := cur.x, cur.fa, cur.t
		j := sort.SearchInts(k[u], t)
		// for j < len(k[u]) && k[u][j] == t {
		// 	t++
		// 	j = sort.SearchInts(k[u], t)
		// }
		if j < len(k[u]) && k[u][j] == t {
			l, r := j, len(k[u])-1
			for l < r {
				mid := (l + r) >> 1
				// if mj-j < mid-t {
				if mid-j < k[u][mid]-t {
					r = mid
				} else {
					l = mid + 1
				}
			}
			if l < len(k[u]) && k[u][l]-t <= l-j {
				t = k[u][l] + 1
			} else {
				t = k[u][l-1] + 1
			}
		}

		for _, q := range g[u] {
			if q.v == fa {
				continue
			}
			v, w := q.v, q.w

			if visit[v] >= 0 && visit[v] <= t+w {
				continue
			}
			visit[v] = t + w
			heap.Push(h, pair{v, u, t + w})
		}
	}

	Fprintln(out, visit[n-1])
}

func main() { CF229B(os.Stdin, os.Stdout) }

type pair struct{ x, fa, t int }
type hp []pair

func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { a, b := h[i], h[j]; return a.t < b.t }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.(pair)) }
func (h *hp) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }
