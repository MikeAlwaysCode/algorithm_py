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
	type edge struct{ u, v, w int }

	var n int
	Fscan(in, &n)
	edges := make([]edge, n-1)
	for i := range edges {
		Fscan(in, &edges[i].u, &edges[i].v, &edges[i].w)
	}
	sort.Slice(edges, func(i, j int) bool {
		return edges[i].w <= edges[j].w
	})

	fa := make([]int, n+1)
	sz := make([]int, n+1)
	for i := range fa {
		fa[i] = i
		sz[i] = 1
	}

	var find func(x int) int
	find = func(x int) int {
		if fa[x] != x {
			fa[x] = find(fa[x])
		}
		return fa[x]
	}
	// find := func(x int) int {
	// 	cur := x
	// 	for fa[x] != x {
	// 		x = fa[x]
	// 	}
	// 	for fa[cur] != x {
	// 		fa[cur], cur = x, fa[cur]
	// 	}
	// 	return x
	// }
	union := func(x, y int) {
		sz[y] += sz[x]
		fa[x] = y
	}

	ans := 0
	for _, e := range edges {
		fu, fv := find(e.u), find(e.v)
		ans += sz[fu] * sz[fv] * e.w
		union(fu, fv)
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
