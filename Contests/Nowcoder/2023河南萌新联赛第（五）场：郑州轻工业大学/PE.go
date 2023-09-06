package main

import (
	"bufio"

	// "container/heap"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	type edge struct{ v, w int }

	var n, u, v, w int
	Fscan(in, &n)
	g := make([][]edge, n)
	for i := 1; i < n; i++ {
		Fscan(in, &u, &v, &w)
		u--
		v--
		g[u] = append(g[u], edge{v, w})
		g[v] = append(g[v], edge{u, w})
	}

	cnt := make([][]int, n)
	for i := range cnt {
		cnt[i] = make([]int, 2)
	}

	var dfs1 func(x, p int)
	dfs1 = func(x, p int) {
		for _, e := range g[x] {
			if e.v != p {
				dfs1(e.v, x)
			}
		}
		for _, e := range g[x] {
			if e.v != p {
				if e.w == 1 {
					cnt[x][0] += cnt[e.v][0] + cnt[e.v][1] + 1
				} else {
					cnt[x][0] += cnt[e.v][0]
					cnt[x][1] += cnt[e.v][1] + 1
				}
			}
		}
	}
	dfs1(0, -1)
	ans := cnt[0][0] + 2*cnt[0][1]

	var dfs2 func(x, p, c0, c1 int)
	dfs2 = func(x, p, c0, c1 int) {
		res := cnt[x][0] + 2*cnt[x][1] + c0 + 2*c1
		ans = min(ans, res)
		for _, e := range g[x] {
			if e.v != p {
				if e.w == 1 {
					dfs2(e.v, x, cnt[x][0]+cnt[x][1]+c0+c1-cnt[e.v][0]-cnt[e.v][1], 0)
				} else {
					dfs2(e.v, x, cnt[x][0]+c0-cnt[e.v][0], cnt[x][1]+c1-cnt[e.v][1])
				}
			}
		}
	}
	dfs2(0, -1, 0, 0)

	Fprintln(out, ans)

}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
