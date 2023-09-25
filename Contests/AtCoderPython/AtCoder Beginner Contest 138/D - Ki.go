package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
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

	// var n, q, u, v, p, x int
	// Fscan(in, &n, &q)
	n, q := r(), r()
	ans := make([]int, n)
	g := make([][]int, n)
	for i := 0; i < n-1; i++ {
		// Fscan(in, &u, &v)
		u, v := r(), r()
		u--
		v--
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	for i := 0; i < q; i++ {
		// Fscan(in, &p, &x)
		p, x := r(), r()
		ans[p-1] += x
	}

	var dfs func(x, p int)
	dfs = func(x, p int) {
		for _, y := range g[x] {
			if y == p {
				continue
			}
			ans[y] += ans[x]
			dfs(y, x)
		}
	}
	dfs(0, -1)
	for _, v := range ans {
		Fprint(out, v, " ")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
