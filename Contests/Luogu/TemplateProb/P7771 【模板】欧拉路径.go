package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, m, u, v int
	Fscan(in, &n, &m)
	g := make([][]int, n+1)

	incnt := make([]int, n+1)
	for i := 0; i < m; i++ {
		Fscan(in, &u, &v)
		g[u] = append(g[u], v)
		incnt[v]++
	}

	start, end := -1, -1
	for i, ic := range incnt {
		if len(g[i]) == ic+1 {
			if start > 0 {
				Fprintln(out, "No")
				return
			}
			start = i
		} else if ic == len(g[i])+1 {
			if end > 0 {
				Fprintln(out, "No")
				return
			}
			end = i
		} else if ic != len(g[i]) {
			Fprintln(out, "No")
			return
		}
		sort.Ints(g[i])
	}

	if start == -1 {
		start = 1
	}

	ans := make([]int, 0, m+1)
	var dfs func(x int)
	dfs = func(x int) {
		for len(g[x]) > 0 {
			y := g[x][0]
			g[x] = g[x][1:]
			dfs(y)
		}
		ans = append(ans, x)
	}
	dfs(start)

	for i := m; i >= 0; i-- {
		Fprint(out, ans[i], " ")
	}
	Fprintln(out)
}

func main() { solve(os.Stdin, os.Stdout) }
