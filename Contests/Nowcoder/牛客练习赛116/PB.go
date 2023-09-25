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

	for q := r(); q > 0; q-- {
		n, k := r(), r()
		mn := n + 1
		mx := mn + (n-1)/4*4
		if k < mn || k > mx || (k-mn)%2 != 0 {
			Fprintln(out, -1)
		} else {
			Fprintln(out, (k-mn)/4*4+((k-mn)%4)/2*3)
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
