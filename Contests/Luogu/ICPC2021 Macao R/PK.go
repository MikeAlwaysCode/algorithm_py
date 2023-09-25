package main

import (
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	// in := bufio.NewReader(_r)
	// out := bufio.NewWriter(_w)
	// defer out.Flush()
	buf := make([]byte, 4096)
	_i := len(buf)
	rc := func() byte {
		if _i == len(buf) {
			_r.Read(buf)
			_i = 0
		}
		b := buf[_i]
		_i++
		return b
	}
	r := func() (x int) {
		b := rc()
		for ; '0' > b; b = rc() {
		}
		for ; '0' <= b; b = rc() {
			x = x*10 + int(b&15)
		}
		return
	}
	type e struct{ x, y, i int }
	deg := make([]int, int(1e5)+1)
	fa := make([]int, int(1e5)+1)
	rank := make([]int, int(1e5)+1)

	T := r()
	for ; T > 0; T-- {
		n, m := r(), r()
		ans := []int{}

		for i := 1; i <= n; i++ {
			fa[i] = i
			deg[i] = 0
			rank[i] = 0
		}

		var find func(x int) int
		find = func(x int) int {
			if fa[x] != x {
				fa[x] = find(fa[x])
			}
			return fa[x]
		}
		union := func(x, y int) {
			if rank[x] < rank[y] {
				fa[x] = y
			} else if rank[x] > rank[y] {
				fa[y] = x
			} else {
				fa[x] = y
				rank[y]++
			}
		}

		g := make([][]int, n+1)
		edges := make([]e, n+1)
		for i := 1; i <= m; i++ {
			u, v := r(), r()
			if len(ans) > 0 {
				continue
			}
			deg[u]++
			deg[v]++
			g[u] = append(g[u], v)
			g[v] = append(g[v], u)
			fu, fv := find(u), find(v)
			edges = append(edges, e{u, v, i})
			if fu == fv {
				seen := make([]bool, n+1)
				q := []int{}
				for j := 1; j <= n; j++ {
					if find(j) == fv {
						seen[j] = true
						if deg[j] == 1 {
							q = append(q, j)
						}
					}
				}
				for len(q) > 0 {
					x := q[0]
					q = q[1:]
					seen[x] = false
					for _, y := range g[x] {
						if !seen[y] {
							continue
						}
						deg[y]--
						if deg[y] == 1 {
							q = append(q, y)
						}
					}
				}

				for _, e := range edges {
					if seen[e.x] && seen[e.y] {
						ans = append(ans, e.i)
					}
				}

				sort.Ints(ans)
			} else {
				union(fu, fv)
			}
		}

		if len(ans) > 0 {
			for i := 0; i < len(ans); i++ {
				if i > 0 {
					Print(" ")
				}
				Print(ans[i])
			}
			Println()
		} else {
			Println(-1)
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
