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
	step := (n&1)*2 - 1
	for i := n / 2; i >= 0 && i < n; {
		a[i] = r()
		a[i] ^= (n - abs(step) + 1) & 1
		i += step
		step = -step
		if step > 0 {
			step++
		} else {
			step--
		}
	}
	for _, v := range a {
		Fprint(out, v, " ")
	}
	Fprintln(out)

}

func main() { solve(os.Stdin, os.Stdout) }
func abs(a int) int {
	if a < 0 {
		return -a
	} else {
		return a
	}
}
