package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

type pair struct {
	d, i, t int
}

func CF1272E(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n int
	Fscan(in, &n)
	g := make([][]int, n)
	a := make([]int, n)
	ans := make([]int, n)
	q := []pair{}
	for i := range a {
		Fscan(in, &a[i])
		if i+a[i] < n {
			g[i+a[i]] = append(g[i+a[i]], i)
		}
		if i-a[i] >= 0 {
			g[i-a[i]] = append(g[i-a[i]], i)
		}
		q = append(q, pair{0, i, a[i] & 1})
		ans[i] = -1
	}
	visit := make([][]int, 2)
	visit[0] = make([]int, n)
	visit[1] = make([]int, n)

	for len(q) > 0 {
		d, u, t := q[0].d, q[0].i, q[0].t
		q = q[1:]
		for _, v := range g[u] {
			if a[v]&1 != t && (ans[v] == -1 || ans[v] > d+1) {
				ans[v] = d + 1
			}
			if visit[t][v] == 0 || visit[t][v] > d+1 {
				visit[t][v] = d + 1
				q = append(q, pair{d + 1, v, t})
			}
		}
	}

	for _, v := range ans {
		Fprintln(out, v, " ")
	}
}

func main() { CF1272E(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
