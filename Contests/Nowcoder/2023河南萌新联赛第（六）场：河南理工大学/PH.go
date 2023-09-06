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

	// var n, m, k, a int
	// Fscan(in, &n, &m, &k)
	n, m, k := r(), r(), r()
	mx := make([]int, n)
	for i := 0; i < n; i++ {
		if i > 0 {
			mx[i] = mx[i-1]
		}
		for j := 0; j < m; j++ {
			// Fscan(in, &a)
			a := r()
			if i == 0 {
				mx[i] = max(mx[i], a)
			}
			if i >= k {
				mx[i] = max(mx[i], mx[i-k]+a)
			}
		}
	}
	Fprintln(out, mx[n-1])
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
