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
	rd := func() (x int64) {
		b := rc()
		for ; '0' > b; b = rc() {
		}
		for ; '0' <= b; b = rc() {
			x = x*10 + int64(b&15)
		}
		return
	}

	a, k := rd(), rd()
	a %= 2
	k %= 2

	for q := rd(); q > 0; q-- {
		l, r := rd(), rd()
		if k == 0 {
			if a == 0 {
				Fprintln(out, -1)
			} else {
				Fprintln(out, 1)
			}
		} else {
			l = ((l + 1) % 2) ^ a
			r = ((r + 1) % 2) ^ a
			if l == r {
				if l == 0 {
					Fprintln(out, -1)
				} else {
					Fprintln(out, 1)
				}
			} else {
				Fprintln(out, 0)
			}
		}
	}

}

func main() { solve(os.Stdin, os.Stdout) }
