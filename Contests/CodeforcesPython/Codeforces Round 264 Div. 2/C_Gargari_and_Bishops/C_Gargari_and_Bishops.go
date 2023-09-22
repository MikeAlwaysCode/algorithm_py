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

	// var n int
	// Fscan(in, &n)
	n := r()
	g := make([][]int, n)
	dia1 := make([]int, n*2)
	dia2 := make([]int, n*2)
	for i := range g {
		g[i] = make([]int, n)
		for j := 0; j < n; j++ {
			// Fscan(in, &g[i][j])
			g[i][j] = r()
			dia1[i+j] += g[i][j]
			dia2[i-j+n] += g[i][j]
		}
	}
	ans := [2]int{-1, -1}
	x := [2]int{}
	y := [2]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			c := (i + j) & 1
			res := dia1[i+j] + dia2[i-j+n] - g[i][j]
			if res > ans[c] {
				ans[c], x[c], y[c] = res, i+1, j+1
			}
		}
	}
	Fprintln(out, ans[0]+ans[1])
	Fprintln(out, x[0], y[0], x[1], y[1])
}

func main() { solve(os.Stdin, os.Stdout) }
