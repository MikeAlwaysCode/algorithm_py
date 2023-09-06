package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	// in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
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

	// var n, m, k, w, b, u, v int
	var n, m, k, b, u, v int
	// Fscan(in, &n, &m, &k, &w)
	n, m, k = r(), r(), r()
	r()
	a := make([]int64, n)
	for i := range a {
		// Fscan(in, &a[i])
		a[i] = int64(r())
	}
	for i := 0; i < n; i++ {
		// Fscan(in, &b)
		b = r()
		if b != 1 {
			a[i] = 0
		}
	}
	fa := make([]int, n+1)
	rank := make([]int, n+1)
	for i := range fa {
		fa[i] = i
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
			x, y = y, x
		} else if rank[x] == rank[y] {
			rank[x]++
		}
		a[y] += a[x]
		a[x] = 0
		fa[x] = y
	}

	for ; m > 0; m-- {
		// Fscan(in, &u, &v)
		u, v = r()-1, r()-1
		// u--
		// v--
		u, v = find(u), find(v)
		if a[u] > 0 && a[v] > 0 && u != v {
			union(u, v)
		}
	}
	sort.SliceStable(a, func(i, j int) bool {
		return a[i] >= a[j]
	})
	var ans int64
	for i := 0; i < n && i < k; i++ {
		ans += a[i]
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
