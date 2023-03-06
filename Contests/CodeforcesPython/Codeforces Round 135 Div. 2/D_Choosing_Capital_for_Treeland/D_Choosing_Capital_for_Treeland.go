package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func CF219D(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	type edge struct{ to, dir int }
	var n, u, v int
	Fscan(in, &n)
	tree := make([][]edge, n+1)
	for i := 1; i < n; i++ {
		Fscan(in, &u, &v)
		tree[u] = append(tree[u], edge{v, 1})
		tree[v] = append(tree[v], edge{u, -1})
	}

	inv, ans := 0, []int{}
	var dfs func(u, p int)
	dfs = func(u, p int) {
		for _, e := range tree[u] {
			if e.to != p {
				if e.dir < 0 {
					inv++
				}
				dfs(e.to, u)
			}
		}
	}
	dfs(1, 0)
	var reroot func(u, p, uc int)
	reroot = func(u, p, uc int) {
		if uc < inv {
			inv = uc
			ans = []int{u}
		} else if uc == inv {
			ans = append(ans, u)
		}
		for _, e := range tree[u] {
			if e.to != p {
				reroot(e.to, u, uc+e.dir)
			}
		}
	}

	reroot(1, 0, inv)

	Fprintln(out, inv)
	sort.Ints(ans)
	for _, v := range ans {
		Fprint(out, v, " ")
	}
}

func main() { CF219D(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
