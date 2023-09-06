package main

import (
	"bufio"
	"container/heap"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	type point struct{ x, y int }
	dir4 := [...]point{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	var n, m, q int
	Fscan(in, &n, &m, &q)
	g := make([][]int, n)
	for i := range g {
		g[i] = make([]int, m)
		for j := range g[i] {
			Fscan(in, &g[i][j])
		}
	}
	mx := n * m
	di := make([][]int, mx)
	for i := range di {
		di[i] = make([]int, mx)
		for j := range di[i] {
			di[i][j] = 1e9 + 7
		}
	}
	var dijkstra func(x, y int)
	dijkstra = func(x, y int) {
		p := x*m + y
		di[p][p] = g[x][y]
		h := hp{{p, di[p][p]}}
		for len(h) > 0 {
			top := heap.Pop(&h).(pair)
			if top.dis > di[p][top.v] {
				continue
			}
			x, y := top.v/m, top.v%m
			for _, d := range dir4 {
				nx, ny := x+d.x, y+d.y
				if nx < 0 || nx >= n || ny < 0 || ny >= m {
					continue
				}
				newD := max(top.dis, g[nx][ny])
				if newD < di[p][nx*m+ny] {
					di[p][nx*m+ny] = newD
					heap.Push(&h, pair{nx*m + ny, newD})
				}
			}
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			dijkstra(i, j)
		}
	}
	var x1, y1, x2, y2 int
	for ; q > 0; q-- {
		Fscan(in, &x1, &y1, &x2, &y2)
		Fprintln(out, di[(x1-1)*m+y1-1][(x2-1)*m+y2-1])
	}
}

func main() { solve(os.Stdin, os.Stdout) }

type pair struct{ v, dis int }
type hp []pair

func (h hp) Len() int              { return len(h) }
func (h hp) Less(i, j int) bool    { return h[i].dis < h[j].dis }
func (h hp) Swap(i, j int)         { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{})   { *h = append(*h, v.(pair)) }
func (h *hp) Pop() (v interface{}) { a := *h; *h, v = a[:len(a)-1], a[len(a)-1]; return }
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
