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

	n := r()
	a := make([]int, n)
	b := make([]int, n)
	c := make([]int, n)
	pres_b := make([]int, n+1)
	for i := range a {
		a[i] = r()
	}
	for i := range b {
		b[i] = r()
		pres_b[i+1] = pres_b[i] + b[i]
	}
	for i := range c {
		c[i] = r()
	}

	for q := r(); q > 0; q-- {
		m := r()
		p := make([]int, m)
		// pres_p = make([]int, m)
		cs := 0
		// remind_b := pres_b[n]
		for i := 0; i < m; i++ {
			p[i] = r() - 1
			// 	if p[i] > 0 {
			// 		pres_p[i] = min(a[i-1])
			//	}
			cs += c[p[i]]
			// 	remind_b -= b[p[i]]

		}
		ans := pres_b[n] + cs
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
