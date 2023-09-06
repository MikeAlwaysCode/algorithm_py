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

	// var n, m, k, s, e int
	// Fscan(in, &n, &m, &k)
	n, m, k := r(), r(), r()
	d := make([]int, n+1)
	ans := 0
	for ; m > 0; m-- {
		// Fscan(in, &s, &e)
		s, e := r(), r()
		d[s]++
		d[e]--
	}
	cnt := 0
	for i := 1; i <= n; i++ {
		cnt += d[i]
		ans = max(ans, (cnt+k-1)/k)
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
