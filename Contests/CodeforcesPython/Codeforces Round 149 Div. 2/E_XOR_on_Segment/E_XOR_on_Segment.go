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

	var ans, left, right, x int
	n := r()
	a := make([]int, n)
	for i := range a {
		a[i] = r()
	}
	for q := r(); q > 0; q-- {
		op := r()
		if op == 1 {
			left, right = r(), r()
			ans = 0
			for i := left - 1; i < right; i++ {
				ans += a[i]
			}
			Fprintln(out, ans)
		} else {
			left, right, x = r(), r(), r()
			for i := left - 1; i < right; i++ {
				a[i] ^= x
			}
		}
	}

}

func main() { solve(os.Stdin, os.Stdout) }
